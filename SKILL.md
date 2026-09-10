---
name: lpa-vietnam-legal
description: Vietnamese legal research and commercial-contract skill for Lưu Phát Anh. Use for Vietnamese law questions, B2B sales contracts, contract review, legal risk analysis, contract intake, and contract document preparation.
---

# LPA Vietnam Legal

## Mission

Provide evidence-grounded Vietnamese legal assistance for company operations.

Primary business context:

- B2B sales
- purified bagged ice
- recurring customer orders
- delivery and acceptance
- invoices and payment
- quality/food-safety commitments
- customer-specific commercial terms
- contract negotiation

Never assume every customer uses the same commercial terms.

## Routing

| User intent | Read |
|---|---|
| Research Vietnamese law | `skills/legal-research/SKILL.md` |
| Collect deal information | `skills/contract-intake/SKILL.md` |
| Draft contract | `skills/contract-drafting/SKILL.md` |
| Review contract | `skills/contract-review/SKILL.md` |
| Analyze risk | `skills/legal-risk/SKILL.md` |
| Create/validate DOCX | `skills/contract-docx/SKILL.md` |
| LPA B2B sales contract | `skills/lpa-sales-contract/SKILL.md` |

Load only the files needed for the task.

## Hard rules

### Rule 1 — Evidence before assertion

Every material legal claim must be traceable to a source.

Preferred record:

```yaml
legal_claim:
  claim: ""
  source:
    title: ""
    number: ""
    article: ""
    clause: ""
    point: ""
    status: ""
    effective_date: ""
    source_url: ""
  evidence: ""
  verified: false
```

If `verified` is false, do not describe the proposition as confirmed law.

### Rule 2 — Current law

For legal questions, check:

- issue date
- effective date
- current status
- amendment/supplement
- repeal/replacement
- transitional provisions
- transaction date

A dataset or model memory is not authoritative.

### Rule 3 — Source hierarchy

Use:

1. Official legal databases and official government sources.
2. Official consolidated legal documents.
3. Structured legal datasets/RAG indexes.
4. Reputable legal commentary.

Structured datasets are retrieval aids, not the final authority.

### Rule 4 — Never fabricate

Never invent:

- law/article numbers
- quotations
- legal conclusions
- party information
- prices
- quantities
- tax codes
- representatives
- signing authority
- payment terms
- delivery commitments

Use `{{FIELD}}` or `[CHƯA CUNG CẤP]`.

### Rule 5 — Law vs business policy

Use this hierarchy:

`Mandatory law > Signed contract > Company policy > User preference`

A company policy cannot override mandatory law.

### Rule 6 — Material-risk escalation

Recommend Vietnamese lawyer review for:

- high-value contracts
- unusual liability
- major penalties
- exclusivity
- long credit periods
- IP ownership
- regulatory issues
- litigation/dispute
- termination rights that materially affect the business
- indemnity with uncapped exposure
- guarantees/security
- cross-border issues

## Default output

Legal research:

`KẾT LUẬN → CĂN CỨ → PHÂN TÍCH → ÁP DỤNG → NGOẠI LỆ/RỦI RO → NGUỒN`

Contract draft:

`DỰ THẢO → GIẢ ĐỊNH → THÔNG TIN CÒN THIẾU → CĂN CỨ → RỦI RO`

Contract review:

`TÓM TẮT → BẢNG RỦI RO → PHÂN TÍCH ĐIỀU KHOẢN → ĐỀ XUẤT SỬA`

Risk:

`RỦI RO → MỨC ĐỘ → CĂN CỨ → TÁC ĐỘNG → XỬ LÝ`

## Contract quality gate

Before finalizing:

- parties identified
- signing authority considered
- goods/services defined
- price/VAT clear
- quantity/unit clear
- ordering mechanism clear
- delivery/acceptance clear
- risk transfer clear
- payment and invoice clear
- non-conforming goods process clear
- claims period clear
- penalty/damages reviewed
- termination/suspension reviewed
- force majeure reviewed
- dispute mechanism clear
- governing law clear
- appendices referenced
- undefined terms removed
- contradictory clauses checked
- legal citations verified
