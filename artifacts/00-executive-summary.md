# CRA Executive Summary — Component Supplier (ECU SW / Infotainment SW / ECU HW) to Automotive OEMs

**Regulation (EU) 2024/2847 (Cyber Resilience Act, "CRA")**
Scope: ECU software, infotainment software, ECU hardware sold to OEMs — EU and non-EU markets.
Status: guidance, not legal advice. One genuinely borderline call is flagged for counsel (§5).

---

## 1. Scope verdict — you fall into TWO buckets, treat them separately

The single most important fact: CRA does NOT apply to products "to which" Regulation (EU) 2019/2144 (vehicle type-approval) applies — **Art 2(2)(c)**. 2019/2144 covers the type-approval of vehicles AND their *systems, components and separate technical units*, and it mandates cybersecurity requirements including a certified Cybersecurity Management System (CSMS) and software-update rules — **Recital 27** confirms this. UNECE R155 (cybersecurity) is the operative framework at vehicle level.

The exclusion is **product-by-product**, turning on whether 2019/2144 applies to that specific product:

- **Bucket A — ECU hardware / ECU software / infotainment software that is part of a type-approved vehicle**: likely OUT of CRA scope (Art 2(2)(c)), because the type-approval framework (2019/2144 + UNECE R155 + CSMS) addresses their cybersecurity. Exposure shifts to the OEM's type-approval obligations, which you must *support* (§6).
- **Bucket B — software placed on the market separately**, not yet part of a type-approved vehicle: e.g. infotainment/telematics apps, update packages, remote-data-processing (cloud/SaaS) backends, or components sold standalone. These are **IN CRA scope** — Art 3(1) expressly includes "software or hardware components being placed on the market separately." Standalone software and SaaS are in scope; "CRA is for hardware" is wrong.

**Flag for counsel:** the exact boundary of "covered by 2019/2144" for a component *supplier* (vs. the vehicle manufacturer doing type-approval) is not settled — the Commission may clarify via delegated acts under Art 2(5). Treat the classification of each product line as a legal call until then. Cost of being wrong is the full penalty ladder (§8).

## 2. Your role = MANUFACTURER of the components (Art 3(13), Art 13+14)

For everything in scope, you are not an importer/distributor — you develop and supply under your own name. You carry the **full manufacturer duty set** (Art 13 + 14): risk assessment, SBOM, support period, vulnerability handling, conformity assessment, technical documentation, DoC, CE marking. The OEM is a **downstream integrator** — a "reasonably foreseeable user" whose integration risk you must assess (FAQ 4.1.4). You must ship secure-installation/configuration instructions for the OEM's integration.

**Contract trap:** if an OEM/integrator sells your component under their own name/trademark OR substantially modifies it, **they** become the manufacturer (Art 21–22) and inherit full duties. Conversely, if YOU rebrand or substantially modify, you inherit the full set. Map who brands/modifies what in every OEM contract.

## 3. Classification / tier (Art 7–8, Annex III/IV) — per core functionality, not product name

- Most automotive ECU/infotainment software defaults to the **default tier** → self-declaration (module A) is permitted.
- Check core functionality against Annex III/IV — automotive components are heavily represented:
  - **Important Class I** (Annex III): operating systems, network management/SIEM, network interfaces, and notably **"security microprocessors/controllers/MCUs"** — many ECU microcontrollers land here. Class I needs a notified-body route (B+C or H) UNLESS you fully apply harmonised standards.
  - **Important Class II** (Annex III): **tamper-resistant microprocessors/MCUs** — notified body or EUCC *always*, no self-declaration.
  - **Critical** (Annex IV): HSMs/secure elements, smartcards — EUCC where a scheme exists, else the Class II route. If ECU hardware contains a secure element/HSM, check this.
- Integrating an important/critical component into a vehicle does NOT auto-reclassify the host, but does add integrator duties.

**Bottom line:** classification memo per product line *before* planning conformity. A Class II or critical product planned around self-declaration is non-compliant by design.

## 4. The four standing artifacts (all in-scope products, all tiers)

1. **Living risk assessment** (Art 13(2)–(7)) — intended purpose + reasonably foreseeable use + misuse + conditions of use + expected lifetime; updated through support period; every Annex I requirement deemed N/A needs a written justification inside the assessment.
2. **Annex I Part I(2)(a)–(m) applicability matrix** — the 13 product-property requirements mapped to controls + evidence.
3. **SBOM** (Annex I II(1)) — machine-readable (CycloneDX/SPDX), ≥ top-level dependencies, regenerated per build, feeding vulnerability handling.
4. **Vulnerability pipeline** (Annex I II(2)–(8)) — CVD policy + public contact → triage/remediate without delay → secure free updates → public fix disclosure — all for the whole support period.

**Support period: ≥5 years** (Art 13(8)). **Security updates retained ≥10 years** (Art 13(9)). **Security updates free** for standard products (Part II(8); only tailor-made B2B agreements excepted).

## 5. Reporting — the highest-stakes obligation (Art 14, LIVE NOW)

Reporting duties are **already in force since 11 September 2026** — before general application — and apply to ALL in-scope products, **including products placed before 11 Dec 2027** (Art 69(3)). If Bucket B products are in scope, your incident pipeline must be live now.

On **awareness** of an actively exploited vulnerability or severe product-security incident (not any CVE — reliable evidence of malicious exploitation, Art 3(42)):
- **24h** early warning → **72h** notification → **final report ≤ 14 days after a fix is available**
- File to the **national CSIRT coordinator AND ENISA** via the EU **single reporting platform** (Art 14(7), Art 16).
- **Component exploits: you report for YOUR product even if the vendor/OEM also reports** (FAQ 5.4). Do not rely on the OEM or component vendor to cover you.

If the vehicle type-approval exclusion applies (Bucket A), reporting for those components sits in the OEM's type-approval/UNECE R155 framework instead — but keep the pipeline ready for Bucket B.

## 6. Non-EU market — CRA does NOT apply there, but flow-down does

CRA attaches only to **placing/making available on the Union market** (Art 3(21)–(22)). Sales outside the EU are **not directly subject to CRA**. BUT: UNECE R155 is a **global UN regulation**, not EU-only — the OEM will flow it down to you contractually for worldwide type approvals, including CSMS certification and software-update requirements. EU-based OEMs may flow CRA requirements into purchase agreements even for non-EU builds. Treat non-EU exposure as **contractual**, EU exposure as **regulatory** — one compliance program satisfying both.

## 7. Penalties & dates (price the risk against these)

**Fine tiers (Art 64):**
- **Tier 1 — €15M or 2.5% of worldwide turnover** (higher wins): Annex I essential requirements + Art 13 manufacturer duties + **Art 14 reporting** — where you live.
- **Tier 2 — €10M or 2%**: importer/distributor/DoC/CE/technical-doc/conformity-procedure failures.
- **Tier 3 — €5M or 1%**: incorrect/misleading info to notified bodies or MSAs.
- SME relief is **narrow**: only a fine waiver for missing the Art 14 early-warning deadlines, plus fine *sizing* — no structural relief (Art 64(10)).
- Fines can **stack** with corrective/restrictive measures (Art 64(9)). MSAs can demand deep access to design/dev/vulnerability-handling **internal documentation** on reasoned request (Art 53) — audits reach your SDLC.

**Dates (Art 71):**
- 10 Dec 2024 — entry into force
- **11 Jun 2026** — Ch IV notification/market-surveillance machinery applies
- **11 Sep 2026** — **Art 14 reporting applies (LIVE)** — including pre-Dec-2027 products
- **11 Dec 2027** — general application
- Products placed before 11 Dec 2027 caught only on substantial modification (Art 69(2)), **except reporting**, which always applies (Art 69(3)).

## 8. Action list (priority order)

1. **Now (urgent):** scoped counsel opinion on Art 2(2)(c) exclusion per product line — Bucket A vs Bucket B. Determines everything downstream.
2. **Now (urgent):** stand up the **Art 14 reporting pipeline** (single-platform credentials, 24h/72h/14d runbook, detection triggers, on-call) — already mandatory for in-scope products.
3. **Per in-scope product line:** classification memo (Art 7/8, Annex III/IV) → conformity route (module A vs B+C/H vs EUCC), notified body if mandatory. Start notified-body engagement early — body bottleneck (Art 35(2)) makes lead time the constraint.
4. **Build the four standing artifacts** (risk assessment, Annex I matrix, SBOM, vulnerability pipeline) with a single source of truth, audit-ready for Art 53 access.
5. **Commit support-period + update-retention cost** (≥5y / ≥10y) in the business case before launch.
6. **Align marketing/contract claims with the risk assessment** — overclaiming expands obligation surface (FAQ 4.1.4).
7. **Contract review with OEMs:** define who is the manufacturer (Art 21–22), flow R155/CSMS + CRA requirements down, carve responsibility for reporting on shared vulnerabilities.

---

**Two highest-stakes facts:**
- **Reporting (Art 14) is live now** (since 11 Sep 2026) and applies to pre-2027 in-scope products — a missed clock is a Tier-1 fine (€15M/2.5%).
- **The Art 2(2)(c) vehicle type-approval exclusion** is your best and worst news: it likely removes type-approved ECU/infotainment components from CRA scope, but the boundary for a component supplier is not fully settled — get counsel per product line, and treat Bucket B (standalone software/remote data processing) as firmly in scope.

This is guidance based on the regulation text and Commission technical FAQs (preliminary, ~2 years pre-application; re-verify for time-sensitive decisions). Route borderline classification/exclusion calls to counsel.
