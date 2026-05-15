"""
LLM integration using BytePlus API (DeepSeek model)
"""
import requests

from .config import settings


SYSTEM_PROMPT = """Kamu adalah Latent, asisten AI yang ramah di website portfolio Pradana Yahya Abdillah.

Tugasmu adalah:
1. Menjawab pertanyaan tentang Pradana (skills, project, pengalaman, pendidikan)
2. Memberikan informasi berdasarkan KONTEKS yang diberikan
3. Bersikap ramah dan helpful

Aturan:
- Jawab HANYA berdasarkan konteks yang diberikan
- Jika tidak ada info di konteks, katakan dengan sopan bahwa kamu tidak punya info tersebut
- Gunakan bahasa Indonesia yang natural
- Jangan terlalu panjang, maksimal 2-3 paragraf
- Boleh pakai emoji sesekali untuk membuat percakapan lebih friendly"""


def generate_answer(question: str, context: str) -> str:
    """
    Generate answer using BytePlus DeepSeek model.
    
    Args:
        question: User's question
        context: Retrieved context from vector search
    
    Returns:
        Generated answer string
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.byteplus_api_key}"
    }
    
    payload = {
        "model": settings.byteplus_model,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""KONTEKS:
{context}

PERTANYAAN:
{question}"""
            }
        ],
        "temperature": 0.3,
        "max_tokens": 500
    }
    
    try:
        resp = requests.post(
            settings.byteplus_base_url,
            headers=headers,
            json=payload,
            timeout=30
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "Maaf, sepertinya aku butuh waktu lebih lama untuk berpikir. Coba tanya lagi ya! ⏳"
    except requests.exceptions.RequestException as e:
        print(f"LLM Error: {e}")
        return "Waduh, ada masalah teknis nih. Coba lagi nanti ya! 🙏"
    except (KeyError, IndexError) as e:
        print(f"LLM Response Error: {e}")
        return "Hmm, ada yang aneh dengan responsnya. Coba tanya lagi! 🤔"
