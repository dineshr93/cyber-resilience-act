# CRA Compliance Patterns & Techniques

Reusable engagement patterns. **When to use / How / Trade-offs** for each.

## Scope & Classification Memo
**When to use**: first deliverable of any CRA engagement, before scoping work.
**How**: run the 3-question scope test (PDE? EU market? data connection?) → check all Art 2(2)–(8) exclusions in order → match core functionality against Annex III Class I/II and Annex IV lists → write a one-page memo with article citations and the resulting obligation tier.
**Trade-offs**: fast to produce but legally consequential — wrong classification cascades into route selection and fines exposure; get it reviewed by counsel for borderline cases.

## Role Matrix (Supply-Chain Obligation Map)
**When to use**: client has OEMs, resellers, integrators, or OSS foundations in its chain.
**How**: table with rows = each stakeholder, columns = {places on EU market? makes available? sells under own brand? modifies product?} → output role (manufacturer/importer/distributor/steward) + duty set from Art 13/14/19/20/24. Flag every "own brand" or "modifies" cell as manufacturer-escalation (Art 21–22).
**Trade-offs**: exposes hidden manufacturer status (white-labelling) that clients often miss — can be an uncomfortable finding; pair with contract remediation (e.g., Art 18 mandates for non-EU OEMs).

## Vehicle Type-Approval / Automotive Component Supplier (Art 2(2)(c))
**When to use**: client supplies ECU/infotainment software, ECU hardware, or any component to automotive OEMs (EU + non-EU) — a recurring high-stakes scenario because the vehicle type-approval exclusion (Art 2(2)(c), Regulation (EU) 2019/2144) is often misread as removing *all* supplier obligations.
**How**: split each product line into buckets. (1) Part of a type-approved vehicle → likely OUT of CRA scope (2019/2144 applies to it; CSMS/software-update rules; UNECE R155 at vehicle level). (2) Placed on the market separately — standalone software, update packages, remote data processing backends, or a component **not itself type-approved** → IN scope per the FAQ 2.1.1/2.2.1 component principle (components intended for integration into a type-approved product but not themselves certified/type-approved are covered by CRA) + Art 3(1). The supplier is the **manufacturer** of its in-scope components (Art 13+14); the OEM is a downstream integrator/foreseeable user (FAQ 4.1.4). Classify per core functionality — ECU MCUs can be Annex III Class I ("security microprocessors/controllers/MCUs") or Class II ("tamper-resistant MCUs"); ECU secure elements/HSMs can be Annex IV critical. Non-EU sales: not directly subject to CRA, but UNECE R155 is a global regulation flowing down contractually; EU OEMs may flow CRA requirements into purchase agreements even for non-EU builds.
**Trade-offs**: the exclusion boundary for a component supplier vs the vehicle manufacturer doing type-approval is the highest-stakes, most uncertain call — get a scoped counsel opinion per product line; FAQs are preliminary guidance (also note Delegated Regulation (EU) 2025/1535 extending the exclusion to Regulation (EU) No 168/2013 L-category vehicles). Deliver: per-product scope memo + role matrix + classification memo + reporting-runbook readiness (Art 14 applies from 11 Sep 2026).

## Requirement Applicability Matrix (Annex I Part I(2)(a)–(m))
**When to use**: core build/compliance planning for any in-scope product.
**How**: one row per letter: applicable? | risks addressed (from risk assessment) | implementing control(s) | evidence/test | N/A justification if not applicable. Feed it into technical documentation (Annex VII).
**Trade-offs**: the central audit artifact — investment pays off across conformity assessment, MSA audits, and client onboarding; maintenance cost is real (must track product changes).

## Vulnerability-Handling Pipeline (Part II stages)
**When to use**: standing operational setup for every manufacturer.
**How**: build per stage — intake (CVD policy + public contact, Part II(5)/(6)) → triage & remediate (SBOM-driven, security updates separate from features where feasible, II(1)/(2)/(3)) → release (secure/automatic distribution, II(7); free, timely, with advisories, II(8)) → disclose (public fix info after users can patch; justified delay only, II(4)).
**Trade-offs**: tooling upfront cost; without it each vulnerability is a manual fire-fighting event that will miss the 24h/72h reporting clocks.

## Reporting Runbook (24h / 72h / 14d)
**When to use**: before 11 Sept 2026 for any in-scope product; mandatory thereafter (Art 14).
**How**: define the "awareness" trigger (what evidence counts as actively exploited); assign on-call filer; pre-draft stage-1/2/3 templates; obtain single-reporting-platform credentials; rehearse end-to-end once; route voluntary/third-party reports through the same intake.
**Trade-offs**: cheap to build, catastrophic to miss (Tier-1 fines); micro/SME waiver covers only the early-warning deadline misses.

## Standards-Coverage Tracker
**When to use**: Class I products, or any product where module A is desired; also a standing watch item.
**How**: per Annex I requirement, record: harmonised standard covering it? published in OJEU? correctly applied by us? → output = presumption of conformity coverage % and the remaining gap that forces notified-body work. Re-check quarterly as CEN/CENELEC JTC 13 standards land (FAQ 6.10).
**Trade-offs**: turns a moving legal target into a trackable table; requires someone to actually monitor publications — assign it explicitly.

## Interplay Obligation Register
**When to use**: product already subject to other EU law (RED, Machinery, GPSR, GDPR, AI Act, sectoral).
**How**: single register with per-law columns: requirement | CRA equivalent | covered by other law at equal/higher protection? (Art 2(5) test) | residual CRA delta | evidence. One risk assessment may serve multiple laws if demonstrable (FAQ 4.1.1/Blue Guide).
**Trade-offs**: avoids duplicated work and contradictory controls; harder to maintain than siloed projects — needs a single owner.

## Support-Period Cost Model
**When to use**: pre-launch product decisions; client business cases.
**How**: set support period (≥5y or expected life) → enumerate what it obligates: vulnerability handling for that window, security updates retained ≥10 years, risk-assessment updates, update distribution infrastructure → price the 5–10+ year run-cost and surface in the launch decision.
**Trade-offs**: turns an abstract legal minimum into a budget line; clients often underestimate — presenting it early prevents late-stage surprise.

## Audit-Readiness Evidence Repository (Art 53)
**When to use**: any product facing market surveillance; also de-risks notified-body assessment.
**How**: one repository containing: risk assessment (+ updates), Annex I matrix, SBOMs per release, test/review records, CVD log, reporting filings, DoC/CE records, version history of technical documentation (all versions reflected). Index it so an MSA's reasoned request can be answered in days.
**Trade-offs**: centralized evidence is the difference between passing and failing an access-based audit; requires discipline to keep current — automate ingestion from CI where possible.

## Marketing-Claims Gate
**When to use**: go-to-market for any in-scope product (FAQ 4.1.4).
**How**: route datasheets/website/sales decks through compliance before launch; each claimed capability becomes part of "intended purpose" and widens Annex I applicability; align claims with the risk assessment, or update the assessment first.
**Trade-offs**: friction on sales velocity in exchange for a smaller, defensible obligation surface — the cheapest scope control available.
