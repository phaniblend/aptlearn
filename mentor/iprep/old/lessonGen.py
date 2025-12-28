import os
import sys
import re
import json
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
OUTPUT_DIR = Path("output")

LESSON_ENGINE_TEMPLATE = {
    "lessonId": "",
    "language": "",
    "challengeTitle": "",
    "flow": [
        {
            "stepId": "problem-statement",
            "type": "static",
            "content": ""
        },
        {
            "stepId": "technology-check",
            "type": "knowledge-check",
            "concept": "technology"
        },
        {
            "stepId": "solution-flow",
            "type": "ai-assisted"
        },
        {
            "stepId": "final-solution",
            "type": "static"
        }
    ]
}

# ----------------------------
# CHALLENGE PARSER
# ----------------------------
def extract_challenges(markdown_text):
    """
    Extract challenges based on headings like:
    ### 1. Hello World Function ⭐
    """
    pattern = re.compile(
        r"(###\s+\d+\.\s+.+?)(?=\n###\s+\d+\.|\Z)",
        re.DOTALL
    )

    matches = pattern.findall(markdown_text)
    challenges = []

    for block in matches:
        lines = block.strip().splitlines()
        title_line = lines[0]

        title = re.sub(r"###\s+\d+\.\s+", "", title_line).strip()
        body = "\n".join(lines[1:]).strip()

        challenges.append({
            "title": title,
            "body": body
        })

    return challenges


# ----------------------------
# LESSON GENERATOR
# ----------------------------
def generate_lessons(md_path):
    language = md_path.stem.lower()
    OUTPUT_LANG_DIR = OUTPUT_DIR / language
    OUTPUT_LANG_DIR.mkdir(parents=True, exist_ok=True)

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    challenges = extract_challenges(content)

    if not challenges:
        print("❌ No challenges found in markdown file.")
        return

    print(f"✅ Found {len(challenges)} challenges in {md_path.name}")

    for idx, ch in enumerate(challenges, start=1):
        lesson = json.loads(json.dumps(LESSON_ENGINE_TEMPLATE))

        lesson["lessonId"] = f"{language}-{idx:02d}"
        lesson["language"] = language
        lesson["challengeTitle"] = ch["title"]

        lesson["flow"][0]["content"] = (
            f"Challenge: {ch['title']}\n\n{ch['body']}"
        )

        out_file = OUTPUT_LANG_DIR / f"{language}-{idx:02d}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(lesson, f, indent=2)

    print(f"📁 Lessons written to {OUTPUT_LANG_DIR}")


# ----------------------------
# ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lessonGen.py <file.md>")
        sys.exit(1)

    md_file = Path(sys.argv[1])
    if not md_file.exists():
        print("❌ File not found:", md_file)
        sys.exit(1)

    generate_lessons(md_file)
