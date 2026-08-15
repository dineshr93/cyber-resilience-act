# Dogfood QA Report

**Target:** ~/repos/cyber-resilience-act/ (CRA compliance-consultant Agent Skills knowledge base)
**Date:** 2026-08-15
**Scope:** Content-quality + factual-accuracy QA of the full knowledge base: SKILL.md, chapters/ch01–ch08, cheatsheet.md, patterns.md, glossary.md, artifacts/, and sources/ (CELEX consolidated + OJ L 2847 + Commission FAQs v13)
**Tester:** Hermes Agent (automated exploratory QA)

> **Adaptation note:** This target is a markdown/Agent-Skills knowledge base, not a browser-driven web application, so the dogfood browser toolset (browser_navigate, browser_vision, screenshots) does not apply. QA was performed by reading every file and fact-checking the highest-stakes compliance claims directly against the authoritative CELEX source text. No screenshots were produced; evidence is cited as source-file line references instead.

---

## Executive Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | 0 |
| 🟠 High | 0 |
| 🟡 Medium | 2 |
| 🔵 Low | 3 |
| **Total** | **5** |

**Overall Assessment:** The knowledge base is structurally complete and factually strong on the core high-stakes numbers — fine tiers, application dates, support/update-retention periods, and the reporting clock all verify exactly against the CELEX consolidated text — but it contains a small number of content-precision issues: an oversimplified incident final-report clock, a stale "reporting live now" claim in one artifact, a pattern-count discrepancy, and a mislabeled regulation chapter.

---

## Issues

### Issue #1: Severe-incident final-report clock oversimplified as "14 days" (one-month clock omitted)

| Field | Value |
|-------|-------|
| **Severity** | 🟡 Medium |
| **Category** | Content |
| **URL** | SKILL.md (line 43), chapters/ch04 (line 10), cheatsheet.md (lines 44, 51), patterns.md (line 30), artifacts/04-reporting-runbook.md (line 17), artifacts/00-executive-summary.md (line 51) |

**Description:**
The skill presents a single universal reporting ladder of "24h / 72h / 14-day" for both actively exploited *vulnerabilities* and severe *incidents*. That 14-day final-report deadline is correct **only for vulnerabilities** — CELEX Art 14(2)(c): "a final report, no later than 14 days after a corrective or mitigating measure is available." For severe **incidents**, Art 14(4)(c) requires the final report "within one month after the submission of the incident notification." The one-month incident clock is never mentioned anywhere in the skill. A compliance consultant relying on this would state the wrong final-report deadline for a severe incident.

**Steps to Reproduce:**
1. Open ch04-reporting-obligations.md and read the "Three-stage reporting ladder" section.
2. Open cheatsheet.md §5 "Reporting clocks" and artifacts/04-reporting-runbook.md "The three-stage ladder" table.
3. Compare the stated final-report deadline to CELEX Art 14(2)(c) vs Art 14(4)(c).

**Expected Behavior:**
Two distinct final-report clocks: 14 days after fix availability (vulnerabilities, Art 14(2)(c)) and within one month after the incident notification (severe incidents, Art 14(4)(c)).

**Actual Behavior:**
A single "≤ 14 days after fix available" final-report deadline applied to both event types, with no mention of the one-month incident clock.

**Screenshot:** N/A (content QA; no browser capture)

**Console Errors:** N/A

---

### Issue #2: Artifact claims reporting is "already in force / LIVE NOW" before the 11 Sep 2026 start date

| Field | Value |
|-------|-------|
| **Severity** | 🟡 Medium |
| **Category** | Content |
| **URL** | artifacts/00-executive-summary.md (lines 46, 48, 73, 90), artifacts/04-reporting-runbook.md (line 3) |

**Description:**
The worked-example artifacts assert reporting is already mandatory: "Reporting duties are **already in force since 11 September 2026**" (00-executive-summary line 48), "**LIVE NOW**" (00 line 46, 04 line 3), and "already mandatory for in-scope products" (00 line 80). The knowledge base is dated **Generated: 2026-08-15** (SKILL.md line 9), and today is 15 Aug 2026 — **before** the 11 Sep 2026 start date. So these absolute claims about a future compliance deadline being already in force are stale/overstated relative to the content's own generation date. The main SKILL.md (line 43) and cheatsheet correctly frame reporting as "live **from** 11 Sep 2026" (future), so the artifacts contradict the rest of the base.

**Steps to Reproduce:**
1. Read artifacts/00-executive-summary.md §5 "Reporting — the highest-stakes obligation (Art 14, LIVE NOW)".
2. Cross-check the generation date in SKILL.md (line 9) and the current date.

**Expected Behavior:**
Frame reporting as applicable from 11 Sep 2026 (consistent with SKILL.md), or update the generation date.

**Actual Behavior:**
Artifacts claim reporting is "already in force since 11 September 2026" and "LIVE NOW" — a date that had not yet arrived as of the base's 2026-08-15 generation.

**Screenshot:** N/A

**Console Errors:** N/A

---

### Issue #3: Pattern count mismatch — "10 patterns" claimed, patterns.md has 11

| Field | Value |
|-------|-------|
| **Severity** | 🔵 Low |
| **Category** | Content |
| **URL** | SKILL.md (line 93), README.md (line 80), patterns.md |

**Description:**
patterns.md contains **11** `## ` pattern sections (Scope & Classification Memo, Role Matrix, Vehicle Type-Approval/Component Supplier, Requirement Applicability Matrix, Vulnerability-Handling Pipeline, Reporting Runbook, Standards-Coverage Tracker, Interplay Obligation Register, Support-Period Cost Model, Audit-Readiness Evidence Repository, Marketing-Claims Gate). Both SKILL.md line 93 and README line 80 state "**10 reusable engagement patterns**." Git log shows a commit "Fix pattern count (10)" (891474a), but the count in the file was not actually aligned — it is 11. A minor documentation discrepancy.

**Steps to Reproduce:**
1. `grep -c '^## ' patterns.md` → 11.
2. Read SKILL.md line 93 and README line 80 → both say "10 reusable engagement patterns".

**Expected Behavior:**
The claimed pattern count matches the number of `## ` sections (11), or the count is corrected.

**Actual Behavior:**
11 patterns in the file, but SKILL.md and README both claim 10.

**Screenshot:** N/A

**Console Errors:** N/A

---

### Issue #4: Chapter IV mislabeled as "notification/market-surveillance machinery"

| Field | Value |
|-------|-------|
| **Severity** | 🔵 Low |
| **Category** | Content |
| **URL** | SKILL.md (line 47), chapters/ch07 (line 20), cheatsheet.md (line 36) |

**Description:**
The skill calls Chapter IV "notification/market-surveillance machinery" (SKILL.md line 47 "Ch IV machinery 11 Jun 2026"; ch07 line 20 "Chapter IV (Arts 35–51, notification/market-surveillance machinery)"; cheatsheet line 36 "Ch IV (notification/market surveillance machinery)"). Per CELEX, **Chapter IV is titled "NOTIFICATION OF CONFORMITY ASSESSMENT BODIES"** (the notified-body notification framework, Arts 35–51), while **Chapter V is "MARKET SURVEILLANCE AND ENFORCEMENT"** (Arts 52–58). The label conflates Chapter IV with Chapter V. The 11 Jun 2026 application date for Ch IV is correct; only the label is imprecise.

**Steps to Reproduce:**
1. Search CELEX source for "CHAPTER IV" and "CHAPTER V" headings (lines 978–980 and 1242–1244).
2. Compare to the skill's chapter labels.

**Expected Behavior:**
Ch IV = notified-body notification framework; market surveillance = Ch V.

**Actual Behavior:**
Ch IV described as "notification/market-surveillance machinery," merging Ch IV with Ch V.

**Screenshot:** N/A

**Console Errors:** N/A

---

### Issue #5: Annex III Class I item 16/19 paraphrased imprecisely (smart-home "general purpose" assistants; health-wearable qualifiers)

| Field | Value |
|-------|-------|
| **Severity** | 🔵 Low |
| **Category** | Content |
| **URL** | chapters/ch01 (lines 14, 34) |

**Description:**
ch01 lists "smart-home assistants" as an Annex III Class I category, but Annex III item 16 is specifically "Smart home **general purpose** virtual assistants" — only *general-purpose* assistants qualify, not all smart-home assistants. ch01 also lists "health wearables," but Annex III item 19 is narrower: personal wearables with a *health-monitoring purpose* **to which MDR/IVDR do not apply**, or wearables intended for children. The paraphrase drops the "general purpose" and the MDR/IVDR-exclusion qualifiers, which could slightly mislead a core-functionality classification.

**Steps to Reproduce:**
1. Read ch01 line 14 (Class I list) and line 34 (anti-pattern on classification).
2. Compare to CELEX Annex III items 16 and 19 (lines 1822, 1828).

**Expected Behavior:**
Match Annex III wording: "Smart home general purpose virtual assistants" and the health-wearable MDR/IVDR-exclusion nuance.

**Actual Behavior:**
Simplified "smart-home assistants" and "health wearables" without the qualifying language.

**Screenshot:** N/A

**Console Errors:** N/A

---

## Issues Summary Table

| # | Title | Severity | Category | URL |
|---|-------|----------|----------|-----|
| 1 | Severe-incident final-report clock oversimplified as "14 days" (one-month clock omitted) | Medium | Content | SKILL.md, ch04, cheatsheet, patterns, artifacts |
| 2 | Artifact claims reporting "already in force / LIVE NOW" before 11 Sep 2026 start | Medium | Content | artifacts/00, artifacts/04 |
| 3 | Pattern count mismatch — "10 patterns" claimed, patterns.md has 11 | Low | Content | SKILL.md, README, patterns.md |
| 4 | Chapter IV mislabeled as "notification/market-surveillance machinery" | Low | Content | SKILL.md, ch07, cheatsheet |
| 5 | Annex III Class I items 16/19 paraphrased imprecisely | Low | Content | ch01 |

## Verified-Correct Fact Check (evidence of accuracy)

The following high-stakes compliance facts were checked line-by-line against `sources/CELEX_02024R2847-20241120_EN_TXT.md` and all **pass**:

- **Fine tiers (Art 64)**: €15M/2.5% (line 1558), €10M/2% with the exact article list Arts 18–23, 28, 30(1)–(4), 31(1)–(4), 32(1),(2),(3), 33(5), 39, 41, 47, 49, 53 (line 1560), €5M/1% (line 1562). ✓
- **Application dates (Art 71)**: in force 10 Dec 2024; apply from 11 Dec 2027; Art 14 from 11 Sep 2026; Ch IV (Arts 35–51) from 11 Jun 2026 (lines 1670–1674). ✓
- **Art 14 applies to pre-Dec-2027 products** (Art 69(3), line 1656). ✓
- **Support period ≥5 years** (Art 13(8), line 408). ✓
- **Security updates retained ≥10 years** (Art 13(9), line 416). ✓
- **Reporting early-warning 24h / notification 72h** (Art 14(2)(a)/(b), lines 480–482); vulnerability final report ≤ 14 days after fix (Art 14(2)(c), line 488). ✓
- **SME waiver** for Art 14(2)(a)/14(4)(a) early-warning deadlines only (Art 64(10)(a), line 1588). ✓
- **OSS steward fine exemption** (Art 64(10)(b), line 1590). ✓
- **OSS steward duties** incl. Art 14(1)/(3)/(8) scope (Art 24, lines 746–752). ✓
- **Notified-body sufficiency by 11 Dec 2026** (Art 35(2), line 988). ✓
- **Annex III Class I (items 1–19) and Class II (items 1–4) lists** — match ch01/ch05 claims (lines 1790–1838). ✓
- **Manufacturer definition "payment, monetisation or free of charge"** (Art 3(13), line 140). ✓
- **All internal markdown links resolve**; no broken `ch01–ch08` / cheatsheet / patterns / glossary references; no common typos detected. ✓

## Testing Coverage

### Files Reviewed
- SKILL.md (106 lines) — full
- chapters/ch01–ch08 — full
- cheatsheet.md — full
- patterns.md — full
- glossary.md — full
- artifacts/00–04 (executive summary, scope memo, role matrix, annex-I matrix, reporting runbook) — full
- sources/CELEX_02024R2847-20241120_EN_TXT.md — targeted fact-check (~12 passages)
- README.md — full

### Checks Performed
- Structure: SKILL.md chapter/topic/supporting-file indexes vs actual files on disk
- Cross-reference integrity: all relative markdown links and `chNN`/file refs resolve
- Factual accuracy: fine tiers, dates, support/update periods, reporting clocks, SME/OSS waivers, Annex III/IV lists, OSS-steward duties, notified-body dates — verified against CELEX source
- Quality: typo scan, pattern-count consistency, chapter-label accuracy, classification-wording precision

### Not Tested / Out of Scope
- **Browser-driven UI testing**: N/A — no web application; target is a local markdown knowledge base.
- **Full CELEX/OJ/FAQ text read**: sources/ are ~750KB; only the cited passages were verified, not every synthesized claim. Spot-checks were representative.
- **Sectoral-interplay accuracy** (RED/Machinery/GDPR/AI Act specifics): referenced but not independently verified against those regulations.

### Blockers
- None. All files were readable and all fact-checks were resolvable against the authoritative source.

---

## Notes

- The base is well-structured and internally consistent; the five issues found are content-precision items, not structural failures.
- **Recommendation (Issue #1)**: split the reporting ladder into two final-report deadlines — 14 days after fix (vulnerabilities, Art 14(2)(c)) and one month after incident notification (severe incidents, Art 14(4)(c)) — across SKILL.md, ch04, cheatsheet, patterns.md, and artifacts/04. This is the highest-value correction given reporting obligations are the Tier-1 fine area.
- **Recommendation (Issue #2)**: re-date the artifacts or re-frame "already in force / LIVE NOW" as "from 11 Sep 2026" to match the base's generation date (2026-08-15) and the rest of the skill.
- **Recommendation (Issues #3–5)**: correct the pattern count to 11 (or trim to 10), relabel Ch IV as the conformity-assessment-body notification framework (Ch V = market surveillance), and tighten Annex III items 16/19 wording.
- No Critical or High findings: the core penalty/dates/reporting numbers are accurate against the regulation text, which matters most given the "high-stakes penalties for bad advice" use case.
