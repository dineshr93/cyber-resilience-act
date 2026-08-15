# Annex I Applicability Matrix — Template

**Purpose:** the central compliance artifact: requirement-by-requirement applicability + control + evidence. Part I is applicability-driven (risk assessment selects letters); Part II is universal (all 8, all the time). N/A entries need written justification inside the risk assessment (Art 13(4)).
**Basis:** Regulation (EU) 2024/2847 Annex I Part I(2)(a)–(m), Part II(1)–(8); Art 13(2)–(4).

## Part I — Product-property requirements (apply "as far as applicable" per your risk assessment)

| Req | Requirement | Applicable? (Y/N/N-A) | Risks it addresses | Implementing control(s) | Evidence / test | N/A justification (if N/A) |
|---|---|---|---|---|---|---|
| (a) | No known exploitable vulnerabilities at market release | | | | Pen-test report + CVE scan | |
| (b) | Secure by default configuration (+ reset to original state) | | | | Config baseline + factory-reset flow | |
| (c) | Security updates possible; auto-update default-on w/ opt-out, user notification, postponement | | | | Update mechanism + opt-out UI | |
| (d) | Protection from unauthorised access: auth, IAM, reporting | | | | Auth/IAM controls + logging | |
| (e) | Confidentiality of data at rest & in transit (state-of-the-art encryption) | | | | TLS + encryption at rest | |
| (f) | Integrity of data, commands, programs, config + corruption reporting | | | | Signed firmware, integrity checks | |
| (g) | Data minimisation — only adequate/relevant/necessary data | | | | Data-flow review | (e.g. no personal data in intended purpose — but check reasonably foreseeable misuse first, FAQ 4.1.3) |
| (h) | Availability of essential functions, also after incident; DoS resilience | | | | DoS mitigation | |
| (i) | Minimise negative impact on other devices'/networks' availability | | | | Rate limiting, isolation | |
| (j) | Limit attack surface incl. external interfaces | | | | Interface hardening | |
| (k) | Reduce incident impact via exploitation mitigation | | | | Mitigation techniques | |
| (l) | Security-relevant logging & monitoring, with user opt-out | | | | Logging + monitoring | |
| (m) | Secure permanent removal of data/settings; secure transfer where possible | | | | Erase/transfer flow | |

## Part II — Vulnerability-handling pipeline (ALL mandatory, ALL the time)

| Req | Requirement | Implementation | Evidence |
|---|---|---|---|
| (1) | Identify & document vulnerabilities + components; SBOM machine-readable, ≥ top-level deps | CycloneDX/SPDX from CI | SBOM per build |
| (2) | Address & remediate without delay incl. security updates; separate security vs functionality where feasible | Patch pipeline | Release records |
| (3) | Effective regular testing & reviews of product security | Pen-test/SAST/DAST cadence | Reports |
| (4) | After fix: publicly disclose vulnerability info (description, products, impact, severity, remediation). Delay only if publication risk outweighs benefit until users can patch | Public advisory template | Published advisories |
| (5) | Enforce coordinated vulnerability disclosure (CVD) policy | Intake channel + triage SLA + researcher comms | CVD policy doc |
| (6) | Facilitate vulnerability reporting incl. third-party components; publish a contact address | security@ contact | Published contact |
| (7) | Secure update distribution mechanisms, automatic where applicable | Signed updates, secure transport | Distribution logs |
| (8) | Disseminate updates without delay, free of charge (unless tailor-made B2B agreement), with advisories on user action | Update infra, 10-y retention | Release + retention records |

## Notes
- Part I matrix must map to the risk assessment (Art 13(2)–(4)); keep a single source of truth.
- "Control → evidence" pairs: a control you can't evidence doesn't exist for an auditor (Art 53).
- Harmonised standards give presumption of conformity only where OJ-published and correctly applied (Art 27) — track coverage gaps per requirement.
