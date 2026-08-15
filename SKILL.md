---
name: cyber-resilience-act
description: "CRA compliance consultant knowledge base from Regulation (EU) 2024/2847 (Cyber Resilience Act) + Commission FAQs v13. Use when advising companies on CRA scope, product classification, manufacturer/importer/distributor obligations, vulnerability handling, reporting duties, conformity assessment, CE marking, penalties, or building compliance measures and tooling for full CRA compliance."
---

<!-- argument-hint: [topic, obligation, article number, or chapter ch01-ch08] -->

# Cyber Resilience Act — Compliance Consultant
**Source**: Regulation (EU) 2024/2847 (CELEX consolidated + OJ L 2847) & Commission technical FAQs v13 | **Chapters**: 8 | **Generated**: 2026-08-15

## How to Use This Skill
- **Without arguments** — load the decision rules below; start with scope + role + tier.
- **With a topic** — ask about `scope`, `SBOM`, `reporting deadlines`, `class I vs II`, `support period`; I read the relevant chapter before answering.
- **With chapter** — ask for `ch03` etc.; I load that file.
- **Browse** — "what chapters do you have?"

Act as a compliance consultant: produce decisions, checklists, obligation maps, and tooling recommendations a company can implement — not summaries of the law. Cite articles/annexes. This is guidance, not legal advice; flag borderline calls for counsel.

### Example engagements
- "Is my product in scope under CRA?" → run the Art 2(1) scope test + exclusion chain (ch01).
- "We white-label a Class I router — what are our obligations?" → role escalation to manufacturer, Art 21–22 (ch01, ch06).
- "We sell ECU/infotainment software + ECU hardware to automotive OEMs — what do we owe?" → vehicle type-approval exclusion buckets + supplier-as-manufacturer + reporting (ch01, ch06, patterns.md).
- "Which conformity route for a VPN client?" → module A vs B+C vs H, keyed to harmonised-standard coverage (ch05, ch08).
- "Build the Annex I applicability matrix for a smart thermostat" → the (a)–(m) matrix with N/A justifications (ch03, patterns.md).
- "What fines if we miss a reporting deadline?" → fine tiers + SME/OSS waivers (ch07).

---

## Core Decision Rules (the toolkit)

**1. Scope test (Art 2(1))** — in scope if ALL: product with digital elements (software/hardware + its remote data processing solutions) → made available on the EU market → intended purpose or reasonably foreseeable use includes a direct/indirect data connection to a device/network. Then check exclusions in order: MDR/IVDR, vehicle type-approval, EASA-certified, marine equipment; sectoral carve-out (Art 2(5), only if other rules give equal/higher protection); spare parts; national security/defence. Standalone software and SaaS are IN scope — "CRA is for hardware" is wrong. **Vehicle type-approval (Art 2(2)(c)) is product-by-product** — CRA does not apply to PDEs "to which" Regulation (EU) 2019/2144 applies; a component *not itself type-approved* but intended for integration into a type-approved vehicle is IN scope (FAQ 2.1.1/2.2.1 component principle + Art 3(1)); Delegated Regulation (EU) 2025/1535 extends the exclusion to Regulation (EU) No 168/2013 L-category vehicles except L1e pedal-assisted. **Non-EU sales** are not directly subject to CRA, but UNECE R155 is global and flows down contractually.

**2. Role determines duties (Art 3(12))** — manufacturer: full Art 13+14. Importer: verify conformity artifacts, block non-conforming product, escalate significant risk to MSAs (Art 19). Distributor: due care, verify CE/docs, relay vulnerabilities to maker, notify MSAs if maker disappears (Art 20). **Trap**: selling under your own name/trademark OR substantial modification = you BECOME the manufacturer with full duties (Art 21–22) — white-labelling and rebranding integrators inherit everything.

**3. Tier determines route (Art 7–8, Annex III/IV)** — Default: module A self-declaration OK. Important Class I (VPN, browsers, password mgrs, SIEM, OSes, routers/switches, smart-home security, health wearables): notified body (B+C or H) UNLESS harmonised standards fully applied. Important Class II (hypervisors, firewalls/IDS-IPS, tamper-resistant MCUs): notified body ALWAYS. Critical (HSMs/security boxes, smart meter gateways, smartcards/secure elements): EUCC where available, else Class II routes. Classification follows CORE FUNCTIONALITY vs the Annex lists, not product names; integrating a Class I product doesn't auto-reclassify the host.

**4. The four standing artifacts (every manufacturer, all tiers)** —
- **Living risk assessment** (Art 13(2)–(7)): no mandated method, but must demonstrably cover intended purpose + reasonably foreseeable use + misuse + conditions of use + lifetime; updated through support period; written justification for every Annex I requirement deemed N/A.
- **Annex I Part I(2)(a)–(m) applicability matrix**: (a) no known exploitable vulns at release, (b) secure by default, (c) auto-updates default-on w/ opt-out, (d) access control/IAM, (e) confidentiality+encryption, (f) integrity, (g) data minimisation, (h) availability/DoS resilience, (i) no harm to other devices' availability, (j) attack-surface reduction, (k) exploitation mitigation, (l) security logging w/ opt-out, (m) secure user data removal.
- **SBOM** (Annex I II(1)): machine-readable (CycloneDX/SPDX), ≥ top-level deps, per build, feeding vulnerability handling.
- **Vulnerability pipeline** (Part II): CVD policy + public contact → triage/remediate w/o delay → secure distribution → free timely updates w/ advisories → public fix disclosure (delay only if justified) — all for the whole support period.

**5. Reporting clocks (Art 14, live from 11 Sep 2026)** — on AWARENESS of actively exploited vulnerability or severe product-security incident: **24h** early warning → **72h** notification → final report ≤ **14 days after fix available**; to national CSIRT coordinator + ENISA via single reporting platform. "Actively exploited" = reliable evidence of malicious exploitation (not any CVE). Component exploits: you report for YOUR product even if the vendor also reports. Applies to products placed on market BEFORE Dec 2027 too.

**6. Key numbers** — support period **≥5 years**; security updates retained **≥10 years**; updates free for standard products; fines **€15M/2.5%** (security+reporting) > €10M/2% (docs/CE/conformity) > €5M/1% (misleading info); SME relief = fine sizing + 2 deadline waivers only; OSS stewards fine-exempt but OSS-product manufacturers are not.

**7. Timeline** — in force 10 Dec 2024 → Ch IV machinery 11 Jun 2026 → **reporting 11 Sep 2026** → general application **11 Dec 2027**. Products placed before Dec 2027: CRA bites only on substantial modification, EXCEPT reporting (always applies).

---

## Chapter Index
| # | Title | Key content |
|---|-------|-------------|
| [ch01](chapters/ch01-scope-and-classification.md) | Scope, Definitions & Classification | scope test, exclusions, Annex III/IV tiers |
| [ch02](chapters/ch02-manufacturer-obligations.md) | Manufacturer Obligations (Art 13) | risk assessment, SBOM, support period, component duties |
| [ch03](chapters/ch03-essential-requirements.md) | Essential Requirements (Annex I) | Part I(2)(a)–(m), Part II(1)–(8), presumption of conformity |
| [ch04](chapters/ch04-reporting-obligations.md) | Reporting (Art 14–17) | 24h/72h/14d ladder, single platform, triggers |
| [ch05](chapters/ch05-conformity-and-ce.md) | Conformity, Tech Docs & CE (Ch III–IV) | module A/B+C/H routes, Annex VII, DoC, CE rules |
| [ch06](chapters/ch06-economic-operators.md) | Importers, Distributors, OSS Stewards | Art 18–25, role escalation to manufacturer |
| [ch07](chapters/ch07-enforcement-penalties-dates.md) | Surveillance, Penalties & Dates | fine tiers, Art 53 access, application timeline |
| [ch08](chapters/ch08-practical-guidance-faqs.md) | Commission FAQ Insights | risk-assessment doctrine, interplay map, standards timing |

## Topic Index
- **Scope / in-scope test** → ch01
- **Exclusions (medical, defence, spare parts)** → ch01
- **Vehicle type-approval / automotive component supplier (2019/2144)** → ch01, patterns.md
- **Non-EU market sales** → ch01 (no direct CRA duty; UNECE R155/contractual flow-down)
- **Classification / important vs critical** → ch01, ch05, ch08
- **Manufacturer duties / Art 13** → ch02
- **Risk assessment methodology** → ch02, ch08
- **SBOM** → ch02, ch03
- **Support period** → ch02, ch07
- **Secure by default / auto-updates** → ch03
- **Vulnerability handling / CVD** → ch03, ch04
- **Reporting deadlines (24h/72h)** → ch04, ch07
- **Actively exploited vulnerability** → ch03, ch04
- **Conformity assessment / modules A, B+C, H** → ch05, ch08
- **Harmonised standards / presumption of conformity** → ch03, ch05, ch08
- **Technical documentation (Annex VII)** → ch05
- **EU declaration of conformity / CE marking** → ch05, ch07
- **Importer duties** → ch06
- **Distributor duties** → ch06
- **White-labelling / substantial modification** → ch01, ch06
- **Open-source steward vs OSS product** → ch06, ch07
- **Authorised representative (non-EU)** → ch06
- **Penalties / fines** → ch07
- **Market surveillance / Art 53 access** → ch07
- **Key dates (2026/2027)** → ch04, ch07
- **Interplay with RED/Machinery/GDPR/AI Act** → ch08

## Supporting Files
- [cheatsheet.md](cheatsheet.md) — decision tables, fine tiers, hard dates, tells & smells (start here for quick answers)
- [patterns.md](patterns.md) — 10 reusable engagement patterns (scope memo, role matrix, applicability matrix, reporting runbook…)
- [glossary.md](glossary.md) — all key terms with article references

## Authoritative Sources (lazy-load — read only when verifying a citation or time-sensitive call)
The distilled chapters above are synthesized from these primary texts. Load the specific file via skill_view/read only when you need to verify exact wording, a borderline call, or a date — do NOT pull them into context by default (~750KB).
- [sources/CELEX_02024R2847-20241120_EN_TXT.md](sources/CELEX_02024R2847-20241120_EN_TXT.md) — consolidated Regulation (EU) 2024/2847 (with corrigenda), the authoritative legal text.
- [sources/OJ_L_202402847_EN_TXT.md](sources/OJ_L_202402847_EN_TXT.md) — Official Journal L, 20 Nov 2024 (original publication).
- [sources/FAQs_on_the_CRA__v13_lgtY4iRgL7X1MmPV1MnSxvNwfTg_122331.md](sources/FAQs_on_the_CRA__v13_lgtY4iRgL7X1MmPV1MnSxvNwfTg_122331.md) — Commission technical FAQs v13 (preliminary guidance, not official position; cite version + date when relying).
Official links (EUR-Lex / EC): CELEX 32024R2847 — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 ; ELI — http://data.europa.eu/eli/reg/2024/2847/oj ; consolidated — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R2847-20241120 ; EC policy — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act ; implementation — https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation.

---

## Scope & Limits
Synthesized from the regulation text + Commission FAQs v13 (preliminary guidance, not official position). Covers CRA only — combine with sectoral-law skills for RED/Machinery/GDPR/AI Act specifics. Guidance, not legal advice; route borderline classification/interplay calls to counsel. Harmonised-standard status and FAQ content evolve — re-verify current state for time-sensitive decisions.
