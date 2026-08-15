# Chapter 7: Market Surveillance, Penalties & Key Dates (Ch V–VIII)

## Core Idea
Enforcement is real and tiered: administrative fines up to €15M / 2.5% of worldwide turnover for the core security obligations, with market surveillance authorities granted deep access rights — plus a hard application timeline (reporting duties from Sept 2026, general application Dec 2027). As consultant, use this chapter to price non-compliance risk and sequence the client's roadmap against the dates.

## Frameworks Introduced
- **Fine tier structure (Art 64)**:
  - Tier 1 — €15,000,000 or 2.5% of total worldwide annual turnover (whichever higher): non-compliance with Annex I essential requirements + Art 13 (manufacturer obligations) + Art 14 (reporting). This is the big one.
  - Tier 2 — €10,000,000 or 2%: failures around economic-operator documentation/CE/DoC/conformity-assessment duties (Arts 18–23, 28, 30(1)–(4), 31(1)–(4), 32(1)–(3), 33(5), 39, 41, 47, 49, 53).
  - Tier 3 — €5,000,000 or 1%: supplying incorrect/incomplete/misleading information to notified bodies or MSAs.
  - How to use: map each client obligation to its tier; weight compliance investment toward Tier-1 items (security + reporting) first.
- **Fine-setting factors (Art 64(5))**: nature/gravity/duration of infringement and consequences; prior fines for similar infringements; size/market share (explicit SME/startup consideration). Fines can stack with corrective/restrictive measures (Art 64(9)).
- **Waivers (Art 64(10))**: micro/small enterprises — no fine for missing the Art 14(2)(a) or 14(4)(a) early-warning deadlines; OSS stewards — exempt from fines for their infringements. Narrow relief, not general SME leniency.
- **Market surveillance powers (Ch V, Arts 52–58)**: Regulation (EU) 2019/1020 applies to PDEs; each MS designates MSA(s); authorities may demand access to data/documentation needed to assess design, development, production and vulnerability handling — including internal documentation — on reasoned request, in an understandable language (Art 53). Expect audits that go into your SDLC, not just paperwork.
- **Confidentiality (Art 63)**: parties must protect IP/confidential business info/trade secrets incl. source code when handling CRA matters — relevant to what you share with MSAs and how you structure disclosures.

## Key Concepts
- **Application timeline (Art 71 + Art 69/70)**:
  - Entry into force: 20 days after OJ publication → **10 December 2024**.
  - **Chapter IV (Arts 35–51, notification/market-surveillance machinery): applies from 11 June 2026.**
  - **Art 14 reporting obligations: apply from 11 September 2026** — before general application; your client's incident pipeline must be live by then.
  - **General application: 11 December 2027.**
- **Transitional rule (Art 69(2)–(3))**: products placed on market *before* 11 Dec 2027 are caught only upon substantial modification — but Art 14 reporting applies to ALL in-scope products regardless of placement date. Legacy fleets still need the reporting machinery.
- **Commission evaluation (Art 70)**: first review report by 11 Dec 2030, then every 4 years; single-reporting-platform effectiveness assessed by 11 Sept 2028 — expect rule evolution; build for change.

## Mental Models
- Use "fines follow the risk": the highest tier attaches to exactly the obligations that protect users (security + reporting) — so compliance budget should too.
- Think of enforcement as *access-based*: the MSA's strongest weapon is Art 53 document access; a client whose evidence is scattered across teams will fail an audit even if the product is secure.
- Use the timeline as a *sequencing tool*: reporting pipeline (Sept 2026) → full compliance (Dec 2027); anything touching notified bodies should start well before, given Art 35(2)'s push for enough bodies by Dec 2026 to avoid bottlenecks.

## Anti-patterns
- **"It applies in 2027, so nothing until then"**: Art 14 reporting is live from Sept 2026 and covers products placed on market before the general date — a 2025-shipped product exploited in 2027 must be reported.
- **Assuming SME status = fine immunity**: only the two narrow waivers in Art 64(10); everything else applies at full force (Art 64(5)(c) only affects fine *sizing*).
- **Treating MSA audits as paperwork reviews**: Art 53 reaches internal documentation of design/development/vulnerability handling — your process evidence is the audit surface.
- **Ignoring confidentiality strategy**: sharing source code or trade secrets with authorities without the Art 63 framing risks leaking competitive info; plan disclosure scope in advance.

## Worked Example
Client: mid-size SaaS (micro/SME) shipping a password manager (Annex III Class I). Risk pricing from this chapter: their core exposure is Tier-1 (€15M/2.5%) because security requirements + reporting are the heart of it; SME status only helps with fine *sizing* and the early-warning deadline waiver — no structural relief. Roadmap sequencing: (1) by 11 Sept 2026 — live 24h/72h/14d reporting pipeline with single-platform credentials, even for products shipped before Dec 2027; (2) by 11 Dec 2027 — full Annex I matrix, SBOM, support-period plan, conformity route (Class I → notified body unless harmonised standards fully applied); (3) audit-readiness: one evidence repository satisfying Art 53 access demands. Result: compliance spend concentrated on Tier-1 items, with dates as milestones in the project plan.

## Key Takeaways
1. Three fine tiers: €15M/2.5% (security + reporting), €10M/2% (docs/CE/conformity), €5M/1% (misleading info to authorities) — invest where Tier 1 lives.
2. Reporting duties apply from **11 Sept 2026**; general application **11 Dec 2027**; legacy products still reportable (Art 69(3)).
3. MSAs can demand deep access to design/dev/vulnerability-handling documentation on reasoned request (Art 53) — keep evidence centralized and current.
4. SME relief is narrow: fine sizing + two deadline waivers only (Art 64(5)(c), 64(10)).
5. Protect trade secrets/source code through the Art 63 confidentiality lens when dealing with authorities.
6. Rules will evolve — first Commission review due Dec 2030; design processes to absorb delegated-act changes (Annex III/IV updates).

## Connects To
- **ch01–ch05**: every obligation tiered here originates in those chapters.
- **ch04**: reporting is the highest-tier duty with its own early application date.
- **cheatsheet.md**: fine tiers + dates are the first rows of the decision table.
