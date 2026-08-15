# Role Matrix — Economic Operators in Your Supply Chain

**Purpose:** map every stakeholder to a CRA role before assigning obligations. Obligations attach to role, not company size (Art 3(12)).
**Basis:** Regulation (EU) 2024/2847 Art 3(12)–(17), Art 13+14 (manufacturer), Art 19 (importer), Art 20 (distributor), Art 21–22 (role escalation), Art 24 (OSS steward), Art 18 (authorised rep).

## Decision switches (Art 21–22)
- **Own brand / trademark on the product** → that party is the manufacturer (full Art 13+14).
- **Substantial modification** (change affecting Annex I Part I compliance or intended purpose, Art 3(30)) → that party is the manufacturer.
- Otherwise: importer (place on market, non-EU maker) or distributor (make available, no property change).

## Matrix

| Stakeholder | Place/make available on EU market? | Own brand? | Modify? | Role | Duty set |
|---|---|---|---|---|---|
| **You (component supplier)** | Yes (EU sales) | Yes (your name on your components) | Possibly | **Manufacturer** of in-scope components (Bucket B) | Full Art 13+14 + conformity + CE + reporting (Art 14) |
| **OEM (vehicle maker)** | Yes (the vehicle) | Yes | Integrates your component | Manufacturer of the vehicle; **downstream integrator** of your component | Type-approval (2019/2144/R155/CSMS) for vehicle; foreseeable user of your component (FAQ 4.1.4) |
| **Reseller/integrator who rebrands your component** | Yes | Yes | Maybe | **Manufacturer** (Art 21) | Full Art 13+14 — NOT pass-through |
| **Importer** (non-EU supplier selling into EU) | Places | Non-EU maker's name | — | Importer | Verify conformity, block non-conforming, escalate significant risk to MSAs (Art 19) |
| **Distributor** | Makes available | No | No | Distributor | Due care, verify CE/docs, relay vulnerabilities to maker, notify MSAs if maker disappears (Art 20) |

## Contract traps to avoid
- "We just resell" but logo on it → you are the manufacturer (Art 21).
- OEM modifies your component → OEM becomes manufacturer of that modified product.
- You white-label / substantially modify → you inherit full duties.
- **Significant cybersecurity risk** (Art 3(38)) threshold: high likelihood + severe impact → importer/distributor must escalate to MSAs.

## Contract review checklist (per OEM agreement)
1. Define who brands/modifies what (Art 21–22) — avoid ambiguous manufacturer status.
2. Flow down UNECE R155 / CSMS requirements for worldwide type approvals.
3. Flow down CRA requirements for EU builds (and non-EU builds via contract).
4. Carve out responsibility for reporting on shared vulnerabilities (FAQ 5.4 — you report for YOUR product).
5. Specify secure-installation/configuration instructions you must ship to the OEM (FAQ 4.1.4).
