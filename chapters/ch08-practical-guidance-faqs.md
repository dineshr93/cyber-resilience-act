# Chapter 8: Practical Guidance — Commission FAQ Insights (FAQs v13)

## Core Idea
The Commission's technical FAQs translate the regulation into how it will actually be applied. The highest-value consulting content here: risk-assessment expectations, what "all essential requirements" really means, interplay with other EU laws, and conformity-assessment mechanics — including what harmonised standards will (and won't) do for you by 2027.

## Frameworks Introduced
- **Risk assessment doctrine (FAQ 4.1.1–4.1.8)**:
  - No mandated methodology — but you must be able to *demonstrate* all relevant risks were identified, evaluated and mitigated; the method must support that documentation (4.1.2).
  - Threat modelling must match the product's threat profile: critical-infrastructure products → nation-state/APT scenarios; consumer products → lower risk profile (4.1.2).
  - The assessment covers the *entire* PDE including in-scope remote data processing and supporting functions (4.1.1) — not just the device.
  - It spans all lifecycle phases, incl. production/delivery/maintenance, not only design (4.1.1).
  - Not-applicable requirements need clear written justification inside the risk assessment; example: no personal-data processing in intended purpose → (g) may be N/A, but check reasonably foreseeable misuse first (4.1.3).
  - Intended purpose is defined by *your* docs/marketing claims — overclaiming expands your obligation surface (4.1.4); keep marketing and compliance aligned.
  - Downstream integrators are foreseeable users for components: assess integration risk + ship secure-installation instructions (4.1.4).
  - Harmonised standards never replace the assessment; they only provide means to meet requirements, and presumption of conformity requires correct application covering all relevant risks (4.1.7).
- **Interplay map with other EU law (FAQ section 2)**: CRA coexists with sectoral regimes — aviation (2018/1139), marine equipment (2014/90), machinery (2023/1230), GPSR (2023/988), RED (2014/53), GDPR, Data Act, Product Liability Directive (2024/2853). Where sectoral rules achieve equal/higher protection, CRA application may be limited/excluded (Art 2(5)); otherwise stack obligations. High-risk AI systems get a defined conformity interplay (Art 12, FAQ-referenced).
- **Classification mechanics (FAQ section 3)**: classification follows the product's *core functionality* vs Annex III/IV categories; integrating an important/critical product into another PDE does not by itself reclassify the host; multiple functions don't disqualify a category match.
- **Conformity assessment practice (FAQ section 6)**: module A = internal control based on Annex VIII; where harmonised standards are absent/partial for Class I, notified-body routes (B+C or H) become mandatory; harmonised-standard timing is tracked per FAQ 6.10 — plan the gap yourself until they land.

## Key Concepts
- **Blue Guide alignment**: CRA risk-assessment expectations mirror New Legislative Framework logic (single assessment can cover multiple laws if you can demonstrate compliance with each separately, FAQ 4.1.1).
- **Living-document status of FAQs**: v13 is preliminary, ~2 years pre-application; expect updates — cite version + date when relying on them, and treat as guidance not law.
- **Vulnerability researcher protection (recital 75, FAQ 4.1.5 footnote)**: MSAs encouraged to address researcher criminal/civil liability exposure — relevant context for your CVD policy tone.

## Mental Models
- Use "FAQ = regulator's reading of the text": when a client asks "does X count?", the FAQ section is the best predictor of how an MSA will answer — cite it in memos.
- Think of interplay as *layered compliance*: one product can carry CRA + sectoral + GDPR obligations simultaneously; build a single obligation register with per-law columns rather than siloed projects.
- Use "standards are a moving target": track CEN/CENELEC JTC 13 (CRA standardisation) publication status as a standing task; each new OJ-published standard can change your cheapest conformity route.

## Anti-patterns
- **Relying on FAQ wording in legal arguments**: FAQs explicitly disclaim official position — use them to inform, not as authority.
- **Marketing-driven scope creep**: every capability you advertise becomes part of "intended purpose" (FAQ 4.1.4) and pulls new Annex I requirements into applicability; align go-to-market claims with the risk assessment.
- **Assuming one harmonised standard solves everything**: presumption applies only to what published standards actually cover, correctly applied (FAQ 4.1.7); map coverage per requirement.
- **Ignoring sectoral interplay**: a product already under machinery/RED/AI rules still needs the CRA delta analysis — "we're compliant with X" is not a CRA answer.

## Worked Example
Client: maker of an industrial machine controller (already RED + Machinery Regulation territory). FAQ-driven analysis: (1) interplay check — sectoral rules cover radio + machinery safety but not the full Annex I set → CRA applies to the delta (FAQ section 2 pattern); (2) risk assessment scoped to critical-infrastructure threat profile per FAQ 4.1.2, covering the controller *and* its remote management cloud (4.1.1); (3) marketing review — datasheet claims "edge AI inference" → that becomes intended purpose → Annex I applicability widens; sales asked to align claims with compliance before launch (4.1.4); (4) conformity route: check current harmonised-standard coverage per requirement (6.10); gaps → notified-body plan. Deliverable: obligation register (CRA + RED + Machinery columns), updated risk assessment, and a marketing-claims gate process.

## Key Takeaways
1. No mandated risk-assessment method — but demonstrability of full-risk coverage is mandatory; pick a method that produces audit-grade evidence (FAQ 4.1.2).
2. Threat model must match deployment context: consumer vs critical infrastructure get different threat profiles (FAQ 4.1.2).
3. Your marketing claims define intended purpose and therefore your obligation surface — gate go-to-market language through compliance (FAQ 4.1.4).
4. Justify N/A requirements in writing, inside the risk assessment (FAQ 4.1.3).
5. Harmonised standards = presumption for what they cover, correctly applied; track publication status as a live task (FAQ 4.1.7, 6.10).
6. Build one obligation register spanning CRA + sectoral law + GDPR; interplay is the norm, not the exception (FAQ section 2).

## Connects To
- **ch01**: classification mechanics in FAQ section 3 operationalize Annex III/IV matching.
- **ch02/ch03**: this chapter is the "how the regulator reads it" layer over Art 13 and Annex I.
- **ch05**: FAQ section 6 drives route-selection decisions when standards are missing.
