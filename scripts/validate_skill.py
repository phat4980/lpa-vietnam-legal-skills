from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "SKILL.md",
    "README.md",
    "skills/legal-research/SKILL.md",
    "skills/contract-intake/SKILL.md",
    "skills/contract-drafting/SKILL.md",
    "skills/contract-review/SKILL.md",
    "skills/legal-risk/SKILL.md",
    "skills/contract-docx/SKILL.md",
    "skills/lpa-sales-contract/SKILL.md",
]

missing = [p for p in required if not (ROOT / p).is_file()]

if missing:
    print("FAIL")
    for p in missing:
        print("  missing:", p)
    sys.exit(1)

for p in required:
    text = (ROOT / p).read_text(encoding="utf-8")
    if p.endswith("SKILL.md") and not text.startswith("---"):
        print("FAIL: missing frontmatter:", p)
        sys.exit(1)

print("PASS: skill repository structure is valid")
