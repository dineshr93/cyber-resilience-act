# Chapter 4: Reporting Obligations (Art 14–17)

## Core Idea
Manufacturers must report actively exploited vulnerabilities and severe security incidents to the national CSIRT coordinator + ENISA via the EU single reporting platform, on a strict 24h / 72h clock plus a final-report stage whose deadline differs by event type — 14 days after a fix for vulnerabilities, one month after the incident notification for severe incidents. As consultant, deliverable = an incident-response runbook that knows these clocks, plus detection triggers for "actively exploited" so the clock starts correctly.

## Frameworks Introduced
- **Three-stage reporting ladder (Art 14)**:
  - Stage 1 — Early warning: within **24 hours** of becoming aware of an actively exploited vulnerability or severe incident affecting product security; include Member States where product is known to be available, and for incidents whether unlawful/malicious acts are suspected.
  - Stage 2 — Vulnerability/incident notification: within **72 hours**; general info on product, nature of exploit/vulnerability, corrective/mitigating measures taken or users can take, sensitivity assessment of the info.
  - Stage 3 — Final report: deadline differs by event type. **Vulnerabilities (Art 14(2)(c))**: no later than **14 days after** a corrective/mitigating measure is available; vulnerability description + severity + impact, malicious-actor info where known, details of the security update/remediation. **Severe incidents (Art 14(4)(c))**: within **one month after** the incident notification under stage 2; detailed description of the incident (severity + impact), likely trigger/root cause, corrective/mitigating measures.
  - How to operationalize: define "becoming aware" (detection trigger), assign an on-call who can file within 24h, pre-draft templates for all three stages, rehearse once before go-live.
- **Dual notification channel**: simultaneously to the CSIRT designated as coordinator (per Art 14(7)) and ENISA, via the single reporting platform (Art 16). One event → two recipients → one platform.
- **Voluntary reporting (Art 15)**: any economic operator (incl. users/researchers) may voluntarily report; manufacturers should design their CVD intake so voluntary reports flow into the same pipeline and don't accidentally start a mandatory clock without triage.
- **Scope nuance for third-party components (FAQ 5.4)**: if an actively exploited vulnerability sits in a third-party component, each manufacturer integrating it has reporting duties to the extent of its own product — coordinate with the component vendor rather than assume someone else reports.

## Key Concepts
- **Actively exploited vulnerability** (Art 3(42)): reliable evidence a malicious actor exploited it without owner permission — your detection trigger should look for this quality of evidence, not any CVE mention.
- **Severe incident having an impact on the security of the product** (Art 3(44)): negatively affects (or can affect) the product's ability to protect availability/authenticity/integrity/confidentiality of data or functions.
- **Single reporting platform** (Art 16): the EU-wide portal; expect it to be mandatory channel by application date — build integration/credentials now.
- **Near miss** (Art 3(45), via DORA def.): relevant context for incident severity assessment.

## Mental Models
- Use "clock starts at awareness, not at confirmation": the 24h early warning is deliberately low-threshold — file early with what you have, refine in stage 2/3. Don't wait for full triage.
- Think of reporting as *one pipeline, three outputs*: intake → triage (is it actively exploited? severe incident?) → staged notifications. The CVD channel, threat-intel feeds, and user reports all feed the same intake.
- Use "who integrates it reports it" for components: each layer in the supply chain owns its product's exposure to a known exploit.

## Anti-patterns
- **Waiting for full root cause before first notification**: stage 1 exists precisely so regulators hear from you within 24h with partial info.
- **Confusing "vulnerability discovered" with "actively exploited"**: a newly published CVE in your SBOM is not automatically reportable; reliable evidence of real-world malicious exploitation is the trigger (FAQ 5.1/5.3).
- **Assuming the component vendor's report covers you**: duties attach per product placed on market (FAQ 5.4); coordinate, don't delegate.
- **No platform account/credentials ready**: filing under time pressure with zero access to the single reporting platform is a guaranteed failure mode.

## Worked Example
Client: router maker (Class I). A CVE for an integrated open-source library is published; threat-intel feed shows active exploitation in the wild matching their product line. T+0h: on-call confirms reliable evidence of malicious exploitation → clock starts. T+3h: early warning filed to national CSIRT coordinator + ENISA via single reporting platform (product, affected versions, MS where sold). T+20h: 72h notification with exploit nature, mitigation (config hardening), user actions. Patch ships T+5d; T+19d max: final report with severity, actor indicators, update details. Concurrently: public advisory per Annex I II(4) after users could patch; SBOM-based check confirms no other products use the vulnerable version. Total: 3 filings, one runbook, zero missed clocks.

## Key Takeaways
1. Clocks are 24h / 72h awareness-triggered; final report is 14 days after fix for vulnerabilities (Art 14(2)(c)) but one month after the incident notification for severe incidents (Art 14(4)(c)).
2. Report to CSIRT coordinator AND ENISA simultaneously via the single reporting platform.
3. "Actively exploited" needs reliable evidence of malicious exploitation — build detection that distinguishes it from ordinary CVE noise.
4. Component exploits: you report for your product even if the vendor also reports (FAQ 5.4).
5. Micro/small enterprises get a fine waiver only for missing the Art 14(2)(a)/(4)(a) early-warning deadlines — no other relief (Art 64(10)).

## Connects To
- **ch03**: Annex I II(4) public disclosure is the user-facing twin of this chapter's regulator-facing duties.
- **ch06**: OSS stewards carry a reduced version of Art 14(1)/(3)/(8) (Art 24).
- **ch07**: fines for reporting failures sit in the €15M/2.5% tier (Art 64(2)).
