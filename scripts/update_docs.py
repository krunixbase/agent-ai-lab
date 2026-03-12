import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "architecture"

TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"

def generate_toc(content):
    lines = content.split("\n")
    toc = []
    for line in lines:
        if line.startswith("#"):
            level = line.count("#")
            title = line.replace("#", "").strip()
            anchor = re.sub(r"[^a-zA-Z0-9 -]", "", title).lower().replace(" ", "-")
            toc.append(f"{'  ' * (level-1)}- [{title}](#{anchor})")
    return "\n".join(toc)

def insert_toc(path):
    text = path.read_text(encoding="utf-8")
    toc = generate_toc(text)

    if TOC_START in text:
        new = re.sub(
            f"{TOC_START}.*?{TOC_END}",
            f"{TOC_START}\n{toc}\n{TOC_END}",
            text,
            flags=re.DOTALL
        )
    else:
        new = f"{TOC_START}\n{toc}\n{TOC_END}\n\n{text}"

    path.write_text(new, encoding="utf-8")

def generate_index():
    index = ["# Global Documentation Index\n"]
    for root, dirs, files in os.walk(ARCH):
        level = root.replace(str(ARCH), "").count(os.sep)
        indent = "  " * level
        folder = os.path.basename(root)
        index.append(f"{indent}- **{folder}/**")
        for f in files:
            if f.endswith(".md"):
                index.append(f"{indent}  - [{f}]({os.path.join(root, f)})")
    (ROOT / "INDEX.md").write_text("\n".join(index), encoding="utf-8")

def add_cross_links(path):
    text = path.read_text(encoding="utf-8")
    related = []

    for folder in ARCH.iterdir():
        if folder.is_dir() and folder.name != "_backup":
            readme = folder / "README.md"
            if readme.exists() and readme != path:
                related.append(f"- [{folder.name}]({readme.relative_to(ROOT)})")

    block = "\n".join(related)
    if "## Related Documents" in text:
        text = re.sub(r"## Related Documents.*", f"## Related Documents\n{block}", text, flags=re.DOTALL)
    else:
        text += f"\n\n## Related Documents\n{block}\n"

    path.write_text(text, encoding="utf-8")

def main():
    print("Updating documentation...")

    # TOC for all README.md
    for readme in ROOT.rglob("README.md"):
        insert_toc(readme)

    # Cross-linking
    for readme in ARCH.rglob("README.md"):
        add_cross_links(readme)

    # Global index
    generate_index()

    print("Done.")

if __name__ == "__main__":
    main()
