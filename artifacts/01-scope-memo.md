# Scope Memo — Component Supplier to Automotive OEMs

**Purpose:** defensible scope + bucket classification for ECU SW / Infotainment SW / ECU HW.
**Basis:** Regulation (EU) 2024/2847 Art 2(1)–(8), Art 3(1)–(2), (21)–(22); Commission FAQs v13 (preliminary).
**Status:** guidance, not legal advice. Bucket boundary per product line needs counsel.

## The 3-question scope test (Art 2(1))

| # | Question | Answer for your products | Consequence |
|---|---|---|---|
| 1 | Product with digital elements (software/hardware + remote data processing)? | Yes — ECU SW, infotainment SW, ECU HW (Art 3(1)) | In candidate scope |
| 2 | Made available on the EU market? | Yes for EU sales (Art 3(21)–(22)); No for non-EU-only sales | EU in scope; non-EU NOT directly |
| 3 | Intended purpose / reasonably foreseeable use includes a direct or indirect data connection to a device/network? | Yes — ECUs and infotainment connect to vehicle networks (CAN/vehicle bus), telematics, and cloud backends | In scope |

## Exclusion ladder (Art 2(2)–(8)) — check in order

| Ground | Applies? | Detail |
|---|---|---|
| MDR/IVDR (2017/745, /746) | No | Not a medical device |
| **Vehicle type-approval (2019/2144)** — Art 2(2)(c) | **MAYBE — the crux** | See buckets below. 2019/2144 covers vehicles + systems/components/STUs; mandates CSMS + software updates; UNECE R155 operative at vehicle level |
| EASA-certified (2018/1139) | No | Not aviation |
| Marine equipment (2014/90) | No | Not marine |
| Sectoral carve-out (Art 2(5)) | Possible for parts where 2019/2144/R155 gives equal/higher protection | Commission may specify via delegated acts; not yet settled |
| Spare parts (Art 2(6)) | No (unless replacing identical component to same spec) | Applies to aftermarket spare parts only |
| National security/defence (Art 2(7)) | No | Not your use |

## The two buckets

**Bucket A — part of a type-approved vehicle** (ECU hardware, ECU software, infotainment SW integrated into a type-approved vehicle):
- Likely OUT of CRA scope via Art 2(2)(c) — type-approval framework (2019/2144 + R155 + CSMS) addresses the cybersecurity.
- Your exposure shifts to supporting the OEM's type-approval obligations.
- **Flag for counsel:** boundary for a component *supplier* vs vehicle manufacturer doing type-approval is unsettled. Commission may clarify via delegated acts under Art 2(5).

**Bucket B — placed on the market separately / remote data processing** (standalone infotainment/telematics apps, update packages, cloud/SaaS backends, components sold standalone):
- **IN CRA scope** — Art 3(1) expressly covers "software or hardware components being placed on the market separately."
- Standalone software and SaaS are in scope — "CRA is for hardware" is wrong.
- Full manufacturer duty set applies (Art 13+14).

## Decision
- Run this memo once per product line. Record the bucket, the exclusion reasoning, and the counsel flag.
- Keep it as your first audit artifact — MSAs may demand it under Art 53.

## Related artifacts
- 02-role-matrix.md — who is the manufacturer per contract
- 03-annex-i-matrix.md — applicability matrix template
- 04-reporting-runbook.md — 24h/72h/14d pipeline
