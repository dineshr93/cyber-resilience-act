# Reporting Runbook — Art 14 (24h / 72h / 14-day)

**Status:** MANDATORY from 11 Sep 2026 for all in-scope products, including placed before 11 Dec 2027 (Art 69(3)). Live now for Bucket B.
**Basis:** Regulation (EU) 2024/2847 Art 14–17, Art 3(42)/(44), Art 16 (single platform); Commission FAQs v13 (5.1/5.3/5.4).

## Trigger — when does the clock start?
- **Actively exploited vulnerability** (Art 3(42)): reliable evidence a malicious actor exploited it without owner permission. Not any CVE — distinguish from ordinary CVE noise (FAQ 5.1/5.3).
- **Severe incident impacting product security** (Art 3(44)): negatively affects or can affect ability to protect availability/authenticity/integrity/confidentiality of data or functions.
- **Clock starts at AWARENESS, not at full triage.** File early with partial info; refine in stages 2/3.

## The three-stage ladder (Art 14)

| Stage | Deadline (from awareness) | Contents |
|---|---|---|
| 1 — Early warning | **24h** | Member States where product is known to be available; whether unlawful/malicious acts suspected |
| 2 — Notification | **72h** | General product info, nature of exploit/vulnerability, corrective/mitigating measures taken or user-available, sensitivity assessment |
| 3 — Final report | **≤ 14 days after fix available** | Vulnerability description + severity + impact, malicious-actor info where known, details of the security update/remediation |

## Channels (Art 14(7), Art 16)
- Simultaneously to: **national CSIRT designated as coordinator** AND **ENISA**.
- Via the EU **single reporting platform** — get credentials/access NOW (missing under time pressure = guaranteed failure).

## Component exploits (FAQ 5.4)
- If an actively exploited vulnerability sits in a third-party component you integrate, **you report for YOUR product** even if the component vendor or OEM also reports. Coordinate, don't delegate.

## Operational checklist
1. Define "becoming aware" detection triggers (intake from CVD channel, threat-intel feeds, user reports — one intake).
2. Assign an on-call who can file within 24h.
3. Pre-draft templates for all three stages.
4. Rehearse once before go-live (dry run against a mock incident).
5. Micro/small enterprises: fine waiver ONLY for missing the Art 14(2)(a)/(4)(a) early-warning deadlines — no other relief (Art 64(10)).

## Anti-patterns
- Waiting for full root cause before first notification — stage 1 exists to file within 24h with partial info.
- Treating "vulnerability discovered" as "actively exploited" — wrong trigger.
- Assuming the component vendor's report covers you — duties attach per product (FAQ 5.4).

## Failure cost
- Reporting failures sit in **Tier 1 fines — €15M or 2.5% of worldwide turnover** (Art 64(2)).
