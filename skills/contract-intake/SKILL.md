---
name: vietnam-contract-intake
description: Normalize business deal information into a structured contract intake before drafting.
---

# Contract Intake

Do not start drafting a final contract until the commercial model is understood.

## Intake schema

```yaml
contract:
  type: ""
  purpose: ""
  effective_date: ""
  duration: ""

seller:
  legal_name: ""
  tax_id: ""
  address: ""
  representative: ""
  title: ""

buyer:
  legal_name: ""
  tax_id: ""
  address: ""
  representative: ""
  title: ""

commercial:
  goods: ""
  specifications: ""
  quantity: ""
  unit: ""
  unit_price: ""
  vat: ""
  currency: ""

ordering:
  channel: ""
  lead_time: ""
  confirmation_method: ""

delivery:
  location: ""
  schedule: ""
  transport: ""
  delivery_documents: ""
  acceptance_method: ""
  risk_transfer: ""

payment:
  method: ""
  invoice_rule: ""
  payment_term: ""
  credit_limit: ""
  late_payment: ""

quality:
  specification: ""
  inspection: ""
  complaint_period: ""
  replacement_rule: ""

remedies:
  penalty: ""
  damages: ""
  liability_cap: ""

termination:
  notice: ""
  cure_period: ""
  immediate_termination_events: ""

dispute:
  negotiation: ""
  forum: ""
  governing_law: ""
```

## Missing information policy

Classify missing fields:

- BLOCKER — must be known before a final draft.
- IMPORTANT — should be confirmed.
- OPTIONAL — can be handled in appendix or later.

Use placeholders rather than guessing.

## Drafting handoff

Produce a normalized summary:

```text
PARTIES
COMMERCIAL TERMS
ORDER FLOW
DELIVERY
QUALITY
PAYMENT
REMEDIES
TERMINATION
DISPUTE
OPEN ITEMS
ASSUMPTIONS
```
