# Chapter 5: Conformity Assessment, Technical Documentation & CE Marking (Ch III–IV)

## Core Idea
Before a PDE can carry the CE mark and enter the EU market, the manufacturer must complete a conformity assessment proving Annex I is met, draw up technical documentation + an EU declaration of conformity, and affix CE. The *route* (module A vs B+C/H) depends on product tier and whether harmonised standards cover it — this is where classification from ch01 becomes money and schedule.

## Frameworks Introduced
- **Conformity assessment route selection (Art 32)**:
  - All products may use: module A (internal control, Annex VIII); or B+C (EU-type examination + conformity to type); or H (full quality assurance).
  - *Important Class I* (Annex III): if you have NOT applied harmonised standards / common specs / EUCC at ≥ "substantial" — or none exist — you MUST use B+C or H (notified body). If you fully apply qualifying standards, module A is available.
  - *Important Class II* (Annex III): always B+C or H or EUCC(≥ substantial) — no pure self-declaration.
  - *Critical* (Annex IV): EUCC where a scheme exists and is adopted; else the Class II routes.
  - *OSS products in Annex III categories*: may use any Art 32(1) route **if** technical documentation is made public at placing on market (Art 32(5)).
  - When to use: after classification, before build planning — it sets whether you need a notified body and how long.
  - How: map tier → allowed modules; check current harmonised-standard coverage per requirement (FAQ 6.10); pick the cheapest route that is legally permitted; budget notified-body lead time + fees (reduced for micro/SME, Art 32(6)).
- **Technical documentation (Art 31, Annex VII)**: minimum content includes general product description, design/development info, cybersecurity risk assessment, applied harmonised standards/common specs/certifications, and the conformity-assessment evidence. Must exist at placing on market; reflect all versions + changes; available to MSAs on reasoned request in an understandable language (Art 53).
- **EU declaration of conformity (Art 28, Annex V/VII)**: standard DoC (Annex V) or simplified DoC (Annex VI) for certain cases; states product identification, manufacturer, sole-responsibility statement, applicable legislation, standards/certifications referenced, notified body + certificate where used.
- **CE marking rules (Art 29–30)**: affix only after conformity assessment is complete and DoC drawn up; mark indicates conformity with Annex I + other Union harmonisation law requiring CE. Notified-body name/number applies where a body participated.

## Key Concepts
- **Presumption of conformity** (Art 27): applying OJ-published harmonised standards covering the relevant requirements → presumed compliant for those parts. The accelerator that lets Class I avoid a notified body.
- **Notified body / notifying authority** (Ch IV, Art 35–40): bodies designated by Member States to run B/C/H assessments; MSAs must ensure enough exist by 11 Dec 2026 to avoid bottlenecks (Art 35(2)).
- **EU type-examination certificate**: the artifact from module B that C then references for production conformity.
- **Full quality assurance (module H)**: a certified QMS covering design, production, final inspection — the heaviest route; suits high-volume or critical products.

## Mental Models
- Think of the three modules as *levels of external trust*: A = self-declare (trust your own process), B+C = one-time third-party type check + your production control, H = continuous third-party QMS audit. Higher tier / weaker standards coverage pushes you up this ladder.
- Use "standards coverage is the escape hatch": for Class I, full application of qualifying harmonised standards is what keeps you on module A — so track standard publication status per requirement and re-check as they land (FAQ 6.10).
- Think of technical documentation as a *living dossier*: every version, change, and risk-assessment update must be traceable in it (Blue Guide logic, FAQ 4.1.8).

## Anti-patterns
- **Defaulting to module A for a Class II product**: not permitted — B+C or H or EUCC is mandatory; planning around self-declaration is a compliance failure.
- **Letting technical documentation go stale after redesigns**: it must reflect all versions and how each was assessed (FAQ 4.1.8); a single "v1" doc fails audit.
- **Affixing CE before the assessment is actually done** or the DoC drawn up — sequencing matters; CE is a claim backed by completed artifacts, not a sticker you add at packaging.
- **Assuming OSS exemption**: open-source products in Annex III categories still need conformity assessment (Art 32(5) just relaxes the route if docs are public); "it's open source" ≠ out of scope.

## Worked Example
Client: firewall vendor (Annex III Class II item 2). Route analysis: Class II → cannot use module A alone; harmonised standards for firewalls not yet fully published at their launch window, so no presumption escape → must engage a notified body for B+C (EU-type examination + production conformity) or run module H. Decision: B+C, because volume is moderate and a one-time type exam beats maintaining an audited QMS. Plan: 6-month lead time for the notified-body assessment; technical documentation dossier assembled in parallel (risk assessment, SBOM, design files, test reports); DoC references the EU type-examination certificate + notified-body number; CE affixed only after certificate issued. Cost/schedule impact surfaced to client *before* build, not at launch.

## Key Takeaways
1. Pick the conformity route from tier + standards coverage — it determines whether you need a notified body and your timeline (Art 32).
2. Class II and critical products can never rely on pure self-declaration.
3. Full application of OJ-published harmonised standards is what lets Class I stay on module A — track standard publication per requirement.
4. Technical documentation must cover all versions/changes and be producible to MSAs (Art 31, Annex VII, Art 53).
5. CE marking is the final act, sequenced after assessment + DoC — not a parallel task (Art 29–30).
6. OSS in Annex III categories still needs assessment; public docs unlock route flexibility (Art 32(5)).

## Connects To
- **ch01**: tier classification is the input to route selection.
- **ch02/ch03**: risk assessment, SBOM, and the Annex I matrix are the core content of the technical documentation.
- **ch07**: CE + DoC failures sit in the €10M/2% fine tier (Art 64(3)).
