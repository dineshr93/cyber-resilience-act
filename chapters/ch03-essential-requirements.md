# Chapter 3: Essential Cybersecurity Requirements (Annex I)

## Core Idea
Annex I is the compliance checklist itself — Part I (13 product-property requirements, applied *as far as applicable* per your risk assessment) and Part II (8 vulnerability-handling obligations, all mandatory for the whole support period). Consulting work here = mapping each point to concrete engineering controls + evidence, and documenting applicability decisions.

## Frameworks Introduced
- **Part I(2)(a)–(m) requirement matrix** — the 13 product-property requirements:
  - (a) no known exploitable vulnerabilities at market release
  - (b) secure by default configuration (+ reset to original state)
  - (c) security updates possible; automatic updates default-on where applicable, with easy opt-out, user notification, temporary postponement option
  - (d) protection from unauthorised access: authentication, IAM controls, reporting of possible unauthorised access
  - (e) confidentiality of stored/transmitted/processed data — encryption at rest & in transit by state-of-the-art mechanisms
  - (f) integrity of data, commands, programs, configuration + corruption reporting
  - (g) data minimisation — only adequate/relevant/necessary data for intended purpose
  - (h) availability of essential functions, also after an incident; DoS resilience/mitigation
  - (i) minimise negative impact on other devices'/networks' service availability
  - (j) limit attack surface incl. external interfaces
  - (k) reduce incident impact via exploitation mitigation mechanisms/techniques
  - (l) security-relevant logging & monitoring of internal activity, with user opt-out
  - (m) secure permanent removal of all data/settings by the user; secure transfer where possible
  - When to use: requirement-by-requirement applicability + control mapping for every product.
  - How: for each letter, record (1) applicable? (2) which risks from your assessment it addresses (3) implementing control(s) (4) evidence/test. N/A entries need written justification (Art 13(4)).
- **Part II(1)–(8) vulnerability-handling pipeline** — all mandatory:
  - (1) identify & document vulnerabilities + components; SBOM in common machine-readable format, ≥ top-level dependencies
  - (2) address & remediate without delay incl. security updates; separate security from functionality updates where technically feasible
  - (3) effective regular testing & reviews of product security
  - (4) after a fix: publicly disclose vulnerability info (description, affected products, impact, severity, remediation help); may delay disclosure only if publication risk outweighs benefit, until users can patch
  - (5) enforce a coordinated vulnerability disclosure (CVD) policy
  - (6) facilitate vulnerability reporting incl. third-party components; publish a contact address
  - (7) secure update distribution mechanisms, automatic where applicable
  - (8) disseminate available security updates without delay, free of charge (unless tailor-made B2B agreement), with advisory messages on user action
- **Presumption of conformity (Art 27)**: conforming to harmonised standards published in the OJEU → presumed compliant for what they cover. Use as an evidence accelerator, not a substitute for the risk assessment.

## Key Concepts
- **Exploitable vulnerability** (Art 3(41)) vs **actively exploited vulnerability** (Art 3(42)): the former is your release gate ((a)); the latter triggers reporting duties (ch04). Reliable evidence of malicious exploitation without owner permission = actively exploited.
- **Security update**: any change addressing a security issue — the unit of Part II(2)/(8) and of the 10-year retention rule.
- **Coordinated vulnerability disclosure (CVD)**: your public policy for how researchers report to you; required by Part II(5); also referenced in Art 13(19).
- **State-of-the-art mechanisms** ((e)): encryption choices must track current practice — a static "AES-256" claim needs an update story across the support period.

## Mental Models
- Think of Annex I as *two checklists with different logic*: Part I is applicability-driven (risk assessment selects which letters apply); Part II is universal (all 8, all the time). Design your compliance matrix so this asymmetry is visible to auditors.
- Use "control → evidence" pairs for every requirement: a control you can't produce evidence for doesn't exist for an auditor.
- Think of Part II as a *pipeline* with stages — intake (5,6) → triage/remediate (2,3) → release (7,8) → disclose (4) — and build tooling per stage rather than ad-hoc processes.

## Anti-patterns
- **Treating Part I(2)(a)–(m) as all-or-nothing**: the regulation expects applicability analysis; blanket "all apply" with generic controls is weaker than a reasoned matrix (FAQ 4.1.3).
- **CVD policy as a webpage stub**: Part II(5) says *enforce*; you need intake channel, triage SLA, researcher communication process.
- **Disclosing fixes before users can patch** without the justified-delay analysis of Part II(4): default is disclose-after-users-can-act; delay only with documented risk/benefit reasoning.
- **Charging for security updates** on standard products — Part II(8) makes them free (tailor-made B2B agreements are the exception).

## Worked Example
Client: consumer smart thermostat (default tier). Applicability matrix excerpt: (a) pass gate = no known exploitable vulns at release, evidence = pen-test report + CVE scan; (b) secure defaults: open ports disabled by default, Wi-Fi WPA3, factory-reset flow documented; (c) auto-update default-on with 72h postpone window + opt-out in app; (e)/(f) TLS 1.3 to cloud + signed firmware for integrity; (g) N/A personal-data processing beyond device config — justified in risk assessment per FAQ 4.1.3 pattern; (i) rate-limited cloud calls so a compromised unit can't DoS the hub network. Part II pipeline: security@ contact published, CVD policy with 90-day response target, CycloneDX SBOM from CI, update server retaining all firmware/security patches for 10 years, public advisory template pre-approved by legal.

## Key Takeaways
1. Build one requirement-by-requirement matrix (Part I letters × control × evidence × N/A justification) — it's the central compliance artifact.
2. Part II is non-negotiable and continuous: SBOM, CVD policy, free timely updates, public fix disclosures.
3. "No known exploitable vulnerabilities" is a release gate with a testable definition (Art 3(41)).
4. Auto-update default-on + easy opt-out is the expected pattern for consumer products ((c)).
5. Harmonised standards buy presumption of conformity only where published in OJEU and correctly applied — check coverage gaps per product (FAQ 4.1.7, 6.10).

## Connects To
- **ch02**: Art 13 is the procedural wrapper around these requirements.
- **ch04**: Part II(4) disclosure + "actively exploited" definition feed reporting duties.
- **ch05**: this matrix is core content of technical documentation (Annex VII).
