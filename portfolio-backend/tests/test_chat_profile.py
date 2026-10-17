import sys
import unittest
import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch


# Keep context-selection tests independent of model downloads and Qdrant.
with patch.dict(sys.modules, {
    "app.embed": SimpleNamespace(embed_text=Mock()),
    "app.qdrant_client": SimpleNamespace(hybrid_search=Mock(), list_payloads_by_category=Mock()),
}):
    from app.routers import chat as chat_router

from app.schemas import ChatCreate


class ProfileContextTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = SimpleNamespace(id=uuid.uuid4(), updated_at=None)
        self.db = SimpleNamespace(
            execute=AsyncMock(return_value=SimpleNamespace(scalar_one_or_none=lambda: self.session)),
            add=Mock(),
            flush=AsyncMock(),
        )
        self.profile = {
            "category": "about",
            "title": "Bio",
            "content": "AI Engineer dan Data Scientist. Cactus Prize 2026. Magang Divistant sudah selesai.",
        }
        self.project = {"category": "project", "title": "Old project", "content": "A project from 2024."}
        self.embedding = patch.object(chat_router, "embed_text", return_value=([0.0], {}))
        self.search = patch.object(chat_router, "hybrid_search", return_value=[SimpleNamespace(payload=self.project, score=0.8)])
        self.payloads = patch.object(chat_router, "list_payloads_by_category", return_value=[self.profile])
        self.answer = patch.object(chat_router, "generate_answer", return_value="Answer from context")
        self.embedding.start()
        self.search_mock = self.search.start()
        self.payloads_mock = self.payloads.start()
        self.answer_mock = self.answer.start()
        self.addCleanup(patch.stopall)

    async def ask(self, message):
        return await chat_router.chat(ChatCreate(message=message, session_id=self.session.id), self.db)

    async def test_general_introduction_gets_current_profile_even_when_search_only_finds_old_project(self):
        response = await self.ask("Ceritakan tentang Pradana")
        context = self.answer_mock.call_args.args[1]
        self.assertTrue(context.startswith("PROFIL TERBARU PRADANA:\n" + self.profile["content"]))
        self.assertIn(self.project["content"], context)
        self.assertEqual(response.sources[0]["title"], "Bio")
        self.assertEqual(response.sources[1]["title"], "Old project")

    async def test_profile_source_is_not_duplicated(self):
        self.search_mock.return_value = [SimpleNamespace(payload=self.profile, score=0.8)]
        response = await self.ask("Siapa Dana?")
        self.assertEqual(len(response.sources), 1)
        self.assertEqual(response.sources[0]["title"], "Bio")

    async def test_category_listing_keeps_its_full_context(self):
        self.payloads_mock.side_effect = lambda category: [self.profile] if category == "about" else [self.project]
        response = await self.ask("Sebutkan semua project Pradana")
        context = self.answer_mock.call_args.args[1]
        self.assertIn(self.profile["content"], context)
        self.assertIn(self.project["content"], context)
        self.search_mock.assert_not_called()
        self.assertEqual([source["title"] for source in response.sources], ["Bio", "Old project"])

    async def test_missing_profile_preserves_search_results(self):
        self.payloads_mock.return_value = []
        response = await self.ask("Jelaskan project tahun 2024")
        self.assertEqual(self.answer_mock.call_args.args[1], self.project["content"])
        self.assertEqual(response.sources[0]["title"], "Old project")


if __name__ == "__main__":
    unittest.main()
