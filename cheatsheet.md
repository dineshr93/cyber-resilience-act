# CRA Compliance Cheatsheet — Decision Rules & Quick Reference

## 1. Scope decision (first question, always)
| If… | Then… | Basis |
|---|---|---|
| Software/hardware + its remote data processing, sold on EU market, with direct/indirect data connection in intended purpose or foreseeable use | **In scope** | Art 2(1), Art 3(1)–(2) |
| MDR/IVDR medical device, vehicle type-approval product, EASA-certified, marine equipment (2014/90) | **Out of scope** (CRA displaced) | Art 2(2)–(4) |
| Other sectoral EU law covers the risks at equal/higher protection | CRA may be limited/excluded — verify per requirement | Art 2(5) |
| Spare part replacing identical component, same specs | Out of scope | Art 2(6) |
| National security/defence/classified-only | Out of scope | Art 2(7) |
| Internal tool never "placed on the market" | Arguably out — but white-labelling it in = in | Art 3(21), Art 21 |

## 2. Classification → conformity route (the money table)
| Tier | Examples (Annex III/IV core functionality) | Allowed routes | Notified body needed? |
|---|---|---|---|
| Default | most PDEs | A, B+C, H | No |
| Important Class I | VPN, browsers, password mgrs, SIEM, OSes, routers/switches, smart-home security, health wearables | A **only if** harmonised standards fully applied; else B+C or H | Yes (if no full standard coverage) |
| Important Class II | hypervisors/container runtimes, firewalls/IDS-IPS, tamper-resistant MCUs/MPUs | B+C, H, or EUCC ≥ substantial | **Always** |
| Critical | HSMs/security boxes, smart meter gateways, smartcards/secure elements | EUCC where scheme available; else Class II routes | **Always** (or certifier) |

Rule: **standards coverage is the escape hatch** — full application of OJ-published harmonised standards keeps Class I on module A. Track publication status per requirement.

## 3. Fine tiers (price your risk against these)
| Tier | Amount | Covers |
|---|---|---|
| 1 | **€15M or 2.5%** worldwide turnover (higher wins) | Annex I requirements + Art 13 manufacturer duties + **Art 14 reporting** |
| 2 | €10M or 2% | importers/distributors/DoC/CE/tech-doc/conformity-procedure failures (Arts 18–23, 28, 30, 31, 32…) |
| 3 | €5M or 1% | incorrect/misleading info to notified bodies & MSAs |

Waivers (narrow): micro/SME — only Art 14 early-warning deadline misses; OSS stewards — their own infringements. Everything else: full force, SME status affects fine *sizing* only.

## 4. Hard dates
| Date | What happens |
|---|---|
| **10 Dec 2024** | Entry into force |
| **11 Jun 2026** | Ch IV (notification/market surveillance machinery) applies; MSAs to have enough notified bodies |
| **11 Sep 2026** | **Art 14 reporting obligations apply — incl. products placed on market before Dec 2027.** Reporting pipeline must be live by now. |
| **11 Dec 2027** | General application of the whole Regulation |
| 11 Dec 2030 (+ every 4y) | Commission evaluation/review reports — expect rule evolution |

## 5. Key thresholds & defaults (commit to these numbers)
- Support period: **≥ 5 years** minimum (or expected use time if shorter) — Art 13(8).
- Security update retention: **≥ 10 years** after issuance (or remainder of support period, whichever longer) — Art 13(9).
- Reporting clocks from awareness: **24h** early warning → **72h** notification → **14 days after fix available** final report.
- SBOM minimum: **top-level dependencies**, machine-readable (CycloneDX/SPDX recommended).
- Security updates: **free of charge** for standard products; auto-update default-on with easy opt-out for consumer-facing products.

## 6. Tells & smells (fast heuristics)
- Client says "we're just reselling" but puts their logo on it → they are the **manufacturer** (Art 21). Stop, re-scope.
- "It's open source, so CRA doesn't apply" → wrong if shipped as a product under their name; steward exemption ≠ product exemption.
- Risk assessment is a one-off PDF from design phase → non-compliant: must be updated through support period (Art 13(7)).
- No security@ contact / no CVD policy page → Part II(5)/(6) gap; also a reporting-pipeline gap.
- "We'll charge for critical patches" on standard products → Part II(8) violation.
- Marketing claims features the risk assessment never covered → intended purpose just grew (FAQ 4.1.4); update assessment or pull the claim.
- Class II product planned around self-declaration → route is illegal; engage notified body early (lead time is the bottleneck).
- No single-reporting-platform credentials by mid-2026 → guaranteed failure on first real incident.

## 7. Decision tree — "what do I owe?"
1. In scope? (table §1) → No: done. Yes ↓
2. My role? (manufacturer / importer / distributor / steward) → duties from Art 13+14 / Art 19 / Art 20 / Art 24.
   - Own brand or substantial modification on the table? → you inherit **full manufacturer** duties regardless of other answers.
3. Tier? (§2) → picks conformity route + whether a notified body is mandatory.
4. Build the four standing artifacts: risk assessment (living), Annex I matrix, SBOM pipeline, reporting runbook.
5. Check dates (§4): reporting live by Sep 2026; everything else by Dec 2027.
