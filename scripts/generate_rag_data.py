#!/usr/bin/env python3
"""
Generate backend RAG JSON data from portfolio frontend sources.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_TS = ROOT / "src" / "lib" / "data" / "projects.ts"
HONOURS_TS = ROOT / "src" / "lib" / "data" / "honours.ts"
PROJECT_MARKDOWN_DIR = ROOT / "static" / "projects"
RAG_DATA_DIR = ROOT / "portfolio-backend" / "data" / "portfolio"


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_array_source(source: str, export_name: str) -> str:
    marker = f"export const {export_name}"
    marker_index = source.index(marker)
    assignment_index = source.index("=", marker_index)
    array_start = source.index("[", assignment_index)
    depth = 0
    for index in range(array_start, len(source)):
        char = source[index]
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return source[array_start + 1:index]
    raise ValueError(f"Could not find array body for {export_name}")


def split_top_level_objects(array_source: str) -> list[str]:
    objects: list[str] = []
    depth = 0
    start: int | None = None
    quote: str | None = None
    escaped = False

    for index, char in enumerate(array_source):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue

        if char in ("'", '"', "`"):
            quote = char
        elif char == "{":
            if depth == 0:
                start = index
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0 and start is not None:
                objects.append(array_source[start:index + 1])
                start = None

    return objects


def get_string_field(obj_source: str, field: str) -> str | None:
    pattern = rf"{field}\s*:\s*(['\"])(.*?)\1"
    match = re.search(pattern, obj_source, flags=re.DOTALL)
    if not match:
        return None
    return normalize_text(match.group(2))


def get_number_field(obj_source: str, field: str) -> int | None:
    match = re.search(rf"{field}\s*:\s*(\d+)", obj_source)
    return int(match.group(1)) if match else None


def get_string_array_field(obj_source: str, field: str) -> list[str]:
    match = re.search(rf"{field}\s*:\s*\[(.*?)\]", obj_source, flags=re.DOTALL)
    if not match:
        return []
    return [normalize_text(item) for _, item in re.findall(r"(['\"])(.*?)\1", match.group(1))]


def get_period(obj_source: str) -> dict[str, str]:
    match = re.search(r"period\s*:\s*\{(.*?)\}", obj_source, flags=re.DOTALL)
    if not match:
        return {}
    period_source = match.group(1)
    period: dict[str, str] = {}
    for field in ("from", "to"):
        value = get_string_field(period_source, field)
        if value:
            period[field] = value
    return period


def read_project_detail(slug: str) -> str:
    path = PROJECT_MARKDOWN_DIR / f"{slug}.md"
    if not path.exists():
        return ""
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", raw)
    raw = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", raw)
    raw = raw.replace("#", " ")
    return normalize_text(raw)


def content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def generate_projects() -> list[dict]:
    source = PROJECTS_TS.read_text(encoding="utf-8")
    objects = split_top_level_objects(extract_array_source(source, "projects"))
    items: list[dict] = []

    for obj in objects:
        slug = get_string_field(obj, "slug")
        title = get_string_field(obj, "title")
        description = get_string_field(obj, "description")
        if not slug or not title or not description:
            continue

        tags = get_string_array_field(obj, "tags")
        details = read_project_detail(slug)
        content_parts = [
            f"Project: {title}.",
            f"Deskripsi: {description}",
            f"Kategori: {get_string_field(obj, 'category') or 'project'}.",
            f"Tahun: {get_number_field(obj, 'year') or ''}.",
            f"Tech stack: {', '.join(tags)}." if tags else "",
            f"Detail: {details}" if details else "",
        ]
        content = normalize_text(" ".join(part for part in content_parts if part))
        items.append({
            "id": f"project-{slug}",
            "category": "project",
            "title": title,
            "content": content,
            "slug": slug,
            "year": get_number_field(obj, "year"),
            "project_category": get_string_field(obj, "category"),
            "tech_stack": tags,
            "demo_url": get_string_field(obj, "demoUrl"),
            "github_url": get_string_field(obj, "githubUrl"),
            "source": "src/lib/data/projects.ts",
            "content_hash": content_hash(content),
        })

    return items


def generate_honours() -> list[dict]:
    source = HONOURS_TS.read_text(encoding="utf-8")
    objects = split_top_level_objects(extract_array_source(source, "honours"))
    items: list[dict] = []

    for obj in objects:
        item_id = get_string_field(obj, "id")
        item_type = get_string_field(obj, "type")
        title = get_string_field(obj, "title")
        if not item_id or not item_type or not title:
            continue

        org = get_string_field(obj, "org")
        description = get_string_field(obj, "description")
        period = get_period(obj)
        tags = get_string_array_field(obj, "tags")
        period_text = " - ".join(value for value in (period.get("from"), period.get("to")) if value)
        content_parts = [
            f"{item_type.title()}: {title}.",
            f"Organisasi: {org}." if org else "",
            f"Periode: {period_text}." if period_text else "",
            f"Deskripsi: {description}" if description else "",
            f"Tags: {', '.join(tags)}." if tags else "",
        ]
        content = normalize_text(" ".join(part for part in content_parts if part))
        items.append({
            "id": item_id,
            "category": item_type,
            "title": title,
            "content": content,
            "org": org,
            "period": period,
            "tags": tags,
            "source": "src/lib/data/honours.ts",
            "content_hash": content_hash(content),
        })

    return items


def write_json(filename: str, data: list[dict]) -> None:
    RAG_DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = RAG_DATA_DIR / filename
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    write_json("projects.json", generate_projects())
    write_json("honours.json", generate_honours())


if __name__ == "__main__":
    main()
