---
name: vietnam-contract-docx
description: Prepare a professional Vietnamese contract document after legal/commercial content has been approved.
---

# Contract DOCX Workflow

## Rule

Content approval comes before formatting.

## DOCX checklist

- Vietnamese Unicode font
- consistent heading hierarchy
- article numbering
- page numbers
- header/footer where needed
- signature blocks
- appendix references
- tables fit page width
- no clipped text
- no orphaned headings where practical
- consistent dates and number formatting
- final placeholder scan

## Recommended structure

```text
TITLE
Contract number
Legal basis if required/appropriate

PARTIES

ARTICLE 1 ...
ARTICLE 2 ...
...

SIGNATURES

APPENDICES
```

## Final validation

Search the document for:

- `{{`
- `}}`
- `[CHƯA CUNG CẤP]`
- `[CẦN XÁC MINH]`
- `TODO`
- inconsistent party names
- inconsistent contract number
- inconsistent dates

Do not remove `[CẦN XÁC MINH]` merely to make the document look finished.

## Generation

If the environment can generate DOCX, use a deterministic document-generation script and preserve the approved text.

For Python, use `python-docx`.
