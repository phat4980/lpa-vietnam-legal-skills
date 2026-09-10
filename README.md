# LPA Vietnam Legal Skills

Agent Skills pack for Vietnamese legal research and B2B commercial contracts.

## Primary use

This repository is designed to be added to an agent workspace and used by ZCode or other coding agents that support `SKILL.md`.

It focuses on:

- Vietnamese legal research
- current-law verification
- B2B contract intake
- commercial contract drafting
- contract review
- legal/commercial risk analysis
- DOCX contract workflows
- Lưu Phát Anh sales-contract workflows

## Structure

```text
lpa-vietnam-legal-skills/
├── SKILL.md
├── skills/
│   ├── legal-research/SKILL.md
│   ├── contract-intake/SKILL.md
│   ├── contract-drafting/SKILL.md
│   ├── contract-review/SKILL.md
│   ├── legal-risk/SKILL.md
│   ├── contract-docx/SKILL.md
│   └── lpa-sales-contract/SKILL.md
├── references/
│   ├── evidence-policy.md
│   ├── temporal-validity.md
│   ├── legal-source-hierarchy.md
│   ├── vietnam-commercial-contract-topics.md
│   └── contract-quality-gate.md
├── company/
│   ├── company-profile.md
│   ├── contracting-policy.md
│   └── approval-matrix.md
├── templates/
│   ├── contract-intake.yaml
│   ├── legal-research-report.md
│   └── contract-risk-report.md
├── scripts/
│   └── validate_skill.py
└── LICENSE
```

## ZCode installation

Recommended project-local layout:

```text
your-project/
└── .agent/
    └── skills/
        └── lpa-vietnam-legal-skills/
```

If your ZCode configuration uses another skills directory, place the repository there.

The important part is that the root `SKILL.md` remains present and the sub-skill folders are kept intact.

## Company configuration

The repository contains editable company files:

- `company/company-profile.md`
- `company/contracting-policy.md`
- `company/approval-matrix.md`

These are intentionally separated from legal knowledge.

Do not put passwords, API keys, banking credentials, customer credentials, or other secrets in this repository.

## Important legal-safety model

The agent must:

1. Prefer authoritative Vietnamese legal sources.
2. Verify legal status and effective dates.
3. Check amendments, repeal, replacement, and transitional rules.
4. Never invent article numbers or legal citations.
5. Mark unverified claims as `[CẦN XÁC MINH]`.
6. Distinguish mandatory law, contract terms, company policy, and business preference.
7. Escalate material/high-risk matters to qualified legal counsel.

This skill is an AI workflow and is not a substitute for legal advice.
