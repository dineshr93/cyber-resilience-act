# Chapter 2: Manufacturer Obligations (Ch II — Art 13)

## Core Idea
The manufacturer is the compliance center of gravity: documented risk-based design, SBOM, secure-by-default, a ≥5-year support period with vulnerability handling, user instructions, and documentation that survives market surveillance. As consultant, your job is to turn this article into a buildable checklist + tooling map for the client's SDLC.

## Frameworks Introduced
- **Risk-based design loop (Art 13(2)–(4))**: cybersecurity risk assessment → outcome feeds planning, design, development, production, delivery, maintenance.
  - When to use: core of every compliance program; required for *all* tiers, not just important/critical.
  - How: assess risks from intended purpose + reasonably foreseeable use + conditions of use (operational environment, assets protected) + expected lifetime; document which Annex I Part I(2)(a)–(m) requirements apply and how each is implemented; justify in the risk assessment any requirement deemed not applicable (Art 13(4)); update during support period.
- **SBOM obligation (Annex I II(1))**: draw up a software bill of materials in a commonly used, machine-readable format covering at least top-level dependencies; identify and document vulnerabilities *and components*.
  - How: adopt CycloneDX/SPDX; generate per-build; feed into vulnerability handling pipeline.
- **Support period rule (Art 13(8))**: ≥5 years minimum (or expected use time if shorter), proportionate to product nature, user expectations, ecosystem/component lifetimes, ADCO/Commission guidance.
  - How: model the full cost of patching for that window *before* committing; it's a lifetime liability decision, not an afterthought.
- **Component due diligence (Art 13(6), Annex I II)**: when you find a vulnerability in an integrated component (incl. OSS): report to the component maintainer, remediate per Part II; share any fix code/docs with the maintainer where appropriate (machine-readable if possible).
- **Update retention (Art 13(9))**: every security update made available must remain downloadable for ≥10 years or remainder of support period, whichever is longer.
- **Versioning relief (Art 13(10))**: for software with subsequent substantially modified versions, Part II(2) compliance may target only the last version placed on market — if older users can get it free without extra hardware/software costs.

## Key Concepts
- **Cybersecurity risk** (Art 3(37)): magnitude of loss/disruption × likelihood of incident — express both dimensions in your assessment.
- **Significant cybersecurity risk** (Art 3(38)): high likelihood + severe negative impact — the threshold that triggers importer/distributor escalation duties.
- **Technical documentation** (Art 31, Annex VII): must exist at placing on market; includes the risk assessment; reflects all product versions and changes (Blue Guide logic per FAQ 4.1.8).
- **Information & instructions to user** (Annex II): clear, understandable, legible; must cover secure installation/operation, reasonably foreseeable misuse risks that lead to significant cybersecurity risk, support period, update mechanisms.

## Mental Models
- Think of Art 13 as *one document family with many consumers*: the risk assessment is the spine; technical documentation, DoC, instructions, and SBOM all derive from it. Keep a single source of truth.
- Use "would a market surveillance authority be able to verify this?" as the test for every artifact (FAQ 4.1.2: methodology choice is free, but you must *demonstrate* all risks were addressed).
- Think of support period as pricing: it's a 5–10+ year cost line item; surface it in the client's business case early.

## Anti-patterns
- **One-off risk assessment**: Art 13(7) requires updating during the support period; a static PDF is non-compliant by design.
- **Skipping not-applicable justifications**: if you don't implement Part I(2)(g) data minimisation because the product doesn't process personal data, say so *in the risk assessment* (FAQ 4.1.3 example) — silence reads as omission.
- **SBOM as a one-time export**: it must cover components and feed vulnerability handling; regenerate per release.
- **Assuming harmonised standards replace the assessment**: they provide presumption of conformity for what they cover, but you still assess all risks (FAQ 4.1.7).

## Worked Example
Client: maker of an industrial IoT sensor gateway (default tier). Program built: (1) threat model scoped to intended purpose + integration into other products (FAQ 4.1.4 — downstream integrators are foreseeable users); (2) requirement-by-requirement applicability matrix for Annex I Part I(2)(a)–(m), e.g. (e)/(f) data protection implemented via TLS + integrity checks, (g) justified N/A if no personal data in intended use; (3) CycloneDX SBOM per build from CI; (4) support period set at 7 years (product expected life ~8y, component vendors patch 5y — documented rationale); (5) update retention pipeline keeping security patches downloadable 10y. Result: one risk-assessment doc + four tooling artifacts that answer every Art 13 paragraph.

## Key Takeaways
1. The risk assessment is mandatory for every product in scope, all tiers — it's the spine of compliance.
2. SBOM (machine-readable, top-level deps minimum) is a hard requirement, not best practice.
3. Support period ≥5 years is a lifetime liability decision; cost it before launch.
4. Security updates must stay available 10+ years — plan storage/distribution now.
5. Justify every "not applicable" requirement in writing inside the risk assessment.
6. White-label or substantial-modification clients inherit all of this (Art 21/22, ch06).

## Connects To
- **ch03**: the Annex I requirements that Art 13(2)–(4) operationalize.
- **ch04**: vulnerability findings from this machinery feed reporting duties.
- **ch05**: risk assessment + SBOM are inputs to technical documentation and conformity assessment.
