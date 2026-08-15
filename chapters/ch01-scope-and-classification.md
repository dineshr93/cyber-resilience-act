# Chapter 1: Scope, Definitions & Product Classification (Ch I–II)

## Core Idea
CRA applies to any product with digital elements (PDE) made available on the EU market whose intended purpose or reasonably foreseeable use includes a direct or indirect logical/physical data connection to a device or network — and your first consulting deliverable is always a defensible scope + classification memo, because it drives everything downstream (obligations level, conformity route, penalties exposure).

## Frameworks Introduced
- **Scope test (Art 2(1))**: PDE = software or hardware product *and its remote data processing solutions*, placed on the market separately.
  - When to use: every engagement, first question.
  - How: (1) Is it a product with digital elements? (2) Is it made available on the EU market (first making available, Art 3(21))? (3) Does intended purpose or reasonably foreseeable use include a data connection — direct or indirect (Art 3(9)–(10))? If yes to all → in scope.
- **Exclusion ladder (Art 2(2)–(8))**: check in order — MDR/IVDR (2017/745, /746), vehicle type approval (2019/2144), EASA-certified products (2018/1139), marine equipment (2014/90); then sectoral carve-outs where other Union rules achieve equal/higher protection (Art 2(5)); spare parts replacing identical components; national security/defence/classified.
- **Vehicle type-approval exclusion is product-by-product (Art 2(2)(c))**: the operative wording is that CRA does not apply to PDEs *"to which"* Regulation (EU) 2019/2144 applies. 2019/2144 covers type-approval of vehicles AND their systems, components and separate technical units, and mandates cybersecurity requirements (CSMS, software-update rules; UNECE R155 operative at vehicle level). **Component principle (FAQ 2.1.1/2.2.1, same logic applies to 2019/2144):** components *intended for integration into* a type-approved product but **not themselves type-approved** under that framework are **covered by the CRA** if they are PDEs made available on the market. So: a component that is itself part of the type-approval is OUT of scope; a component placed on the market separately (standalone software, update packages, remote data processing backends, or a component not individually type-approved) is IN scope (Art 3(1)). Also note Delegated Regulation (EU) 2025/1535 (first Art 2(5) delegated act) extends the exclusion to PDEs within Regulation (EU) No 168/2013 (L-category two-/three-wheel vehicles & quadricycles), except L1e pedal-assisted. Boundary for a component supplier remains a counsel call — FAQs are preliminary guidance.
- **Tiered classification (Art 7–8, Annex III–IV)**:
  - *Default*: most PDEs — internal control (module A) suffices.
  - *Important Class I* (Annex III): identity mgmt/PAM, browsers, password managers, AV, VPN, network mgmt, SIEM, boot managers, PKI/cert issuance, network interfaces, OSes, routers/modems/switches, security microprocessors/MCUs/ASICs/FPGAs, smart-home assistants & security products, connected toys with social/location features, health wearables. → Notified-body route if harmonised standards not (fully) applied.
  - *Important Class II* (Annex III): hypervisors/container runtimes, firewalls/IDS-IPS, tamper-resistant microprocessors/MCUs. → Notified body or EUCC always.
  - *Critical* (Annex IV): hardware security modules/security boxes, smart meter gateways & advanced-security devices, smartcards/secure elements. → European cybersecurity certification (EUCC) at ≥ "substantial" where available; else Class II route.

## Key Concepts
- **Product with digital elements** — software/hardware + its remote data processing solutions; components placed on the market separately count (Art 3(1)).
- **Remote data processing** — cloud/SaaS processing designed by the manufacturer, absence of which prevents a product function (Art 3(2)) → SaaS backends can be in scope.
- **Manufacturer** — anyone who develops/manufactures or has developed and markets under own name/trademark, free or paid (Art 3(13)). White-labelling = you are the manufacturer.
- **Intended purpose / reasonably foreseeable use / misuse** (Art 3(23)–(25)) — scope of your risk analysis; defined by *your* documentation and marketing claims.
- **Substantial modification** (Art 3(30)) — post-market change affecting Annex I Part I compliance or intended purpose → re-triggers full manufacturer obligations.
- **Support period** (Art 3(20)) — the window in which vulnerability handling must work; drives lifetime cost modeling for clients.

## Mental Models
- Think of scope as a *funnel*: product? market? connection? → then exclusions → then tier. Each "yes" narrows obligations; each exclusion removes them.
- Use "who sells under whose name" to assign manufacturer status — the trademark, not the factory, decides (Art 21/22).
- Think of classification as a *risk ladder*: default < Class I < Class II < critical; higher rung = more external verification, not different requirements.

## Anti-patterns
- **Assuming "we're just software, CRA is for hardware"**: standalone software and SaaS are explicitly in scope (Art 3(1)–(2)).
- **Treating "own-use" products as out of scope**: only national security/defence and certified/spare-part categories are excluded; internal tools placed on the market still count.
- **Classifying by marketing category instead of core functionality** (Annex III tests *core functionality* of the listed categories).
- **Ignoring that integrating a Class I product into another PDE does not automatically make the host Class I** — but the integrator gets new duties (see ch06).

## Worked Example
Client: EU SaaS provider offering a VPN-as-a-service to businesses. Scope: in scope (software + remote processing, connection inherent). Classification check against Annex III Class I item 5 ("products with digital elements with the function of virtual private network (VPN)") → core functionality matches → **Important Class I**. Consequence: if harmonised standards don't yet fully cover it, conformity must go through module B+C or H (notified body), not self-declaration. Deliverable: one-page classification memo citing Art 7(1) + Annex III item 5, with fallback analysis for the standards gap.

Client: **automotive component supplier** selling ECU software, infotainment software, and ECU hardware to OEMs, EU + non-EU. Split by bucket: (1) ECU/infotainment software that is part of a type-approved vehicle → likely OUT of CRA scope via Art 2(2)(c); (2) software placed on the market separately (standalone infotainment/telematics apps, update packages, cloud/SaaS backends) or components not individually type-approved → **IN scope** per the FAQ 2.1.1/2.2.1 component principle + Art 3(1). Supplier is the **manufacturer** of its in-scope components (Art 13+14); the OEM is a downstream integrator/foreseeable user (FAQ 4.1.4). Classification per core functionality: ECU microcontrollers may hit Annex III Class I ("security microprocessors/controllers/MCUs") or Class II ("tamper-resistant MCUs"); secure elements/HSMs in ECU hardware may be Annex IV critical. Non-EU sales are not directly subject to CRA but UNECE R155 is global and flows down contractually. Deliverable: per-product-line scope memo (bucket A vs B) + role matrix + classification memo, with counsel flag on the Art 2(2)(c) boundary.

## Key Takeaways
1. Run the 3-question scope test before anything else; document it — it's your first audit artifact.
2. Check all eight exclusion grounds in order; sectoral carve-outs (Art 2(5)) are only valid if the other rules achieve equal/higher protection.
3. Classify by core functionality against Annex III/IV lists, not product names.
4. White-labelling or substantial modification makes your client a manufacturer regardless of who wrote the code (Art 21).
5. Remote data processing solutions are part of the product — cloud backends inherit CRA obligations.

## Connects To
- **ch02**: classification determines which obligations bite and how hard.
- **ch03**: Annex I requirements apply to all tiers; tier changes verification, not substance.
- **ch05**: tier selects the conformity assessment route (module A vs B+C/H).
