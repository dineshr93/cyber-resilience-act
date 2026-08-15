# Chapter 6: Importers, Distributors & Open-Source Stewards (Art 18–25)

## Core Idea
CRA obligations follow the *role in the supply chain*, not just the factory. Importers and distributors carry verification + escalation duties, and either becomes a full manufacturer if they rebrand or substantially modify. Open-source stewards have a lighter, policy-based duty set plus partial reporting. As consultant, map every client stakeholder to a role before assigning obligations — mis-assignment is a top compliance gap.

## Frameworks Introduced
- **Importer duties (Art 19)**: place on market only conforming products; *before* placing, verify the manufacturer did conformity assessment, drew up technical documentation, affixed CE, and provided DoC + Annex II instructions in an understandable language; be able to produce documents proving all of this. If they believe a product is non-conforming → don't place it until fixed; if significant cybersecurity risk → inform manufacturer AND market surveillance authorities (also for non-technical risk factors). Add their name/address/contact on the product/packaging/docs.
- **Distributor duties (Art 20)**: act with due care; verify CE present and that manufacturer/importer met Art 13(15),(16),(18),(19),(20) + Art 19(4) and provided necessary docs; if non-conforming → stop making available until fixed, and on significant risk inform manufacturer + MSAs without undue delay; on learning of a vulnerability → tell the manufacturer without undue delay (and MSAs immediately if significant risk); provide info/docs to MSA on reasoned request; if the manufacturer ceases operations → notify MSAs and, where possible, users.
- **Role escalation to manufacturer (Art 21–22)**: an importer or distributor is treated as a *manufacturer* (full Art 13 + 14) when it places a PDE on the market under its own name/trademark OR carries out a substantial modification of an already-placed product. This is the trap for white-labelers, resellers who rebrand, and integrators who modify.
- **Open-source software steward duties (Art 24)**: put in place + document (verifiably) a cybersecurity policy fostering secure development and effective vulnerability handling by developers; foster voluntary reporting (Art 15); cooperate with MSAs on request and provide the documentation. Art 14(1) applies to stewards to the extent they're involved in development; Art 14(3)/(8) apply where severe incidents affect their own dev networks. Note: OSS *stewards* are exempt from administrative fines (Art 64(10)(b)) — but manufacturers of OSS products are not.
- **Authorised representative (Art 18)**: a Union-established person mandated in writing by a non-EU manufacturer to act on its behalf for specified tasks — the standard vehicle for non-EU makers to have an EU anchor.

## Key Concepts
- **Economic operator** (Art 3(12)): manufacturer, authorised rep, importer, distributor, or other person subject to CRA obligations in relation to making a PDE available.
- **Placing on the market** (Art 3(21)) vs **making available on the market** (Art 3(22)): first EU availability vs supply for distribution/use — importers "place", distributors "make available".
- **Substantial modification** (Art 3(30)): post-market change affecting Annex I Part I compliance or intended purpose — the trigger that reassigns manufacturer status.
- **Significant cybersecurity risk** (Art 3(38)): the threshold that escalates importer/distributor duties to "inform MSAs".

## Mental Models
- Use a *role matrix*: rows = stakeholders (OEM, your client, reseller, integrator, OSS foundation), columns = {place/make available?, own brand?, modify?} → output = role + duty set. Fill it before drafting any contract or compliance plan.
- Think of "brand or modify" as the two switches that flip someone into manufacturer status (Art 21) — everything else stays in their lighter lane.
- For OSS, separate *steward* (policy + cooperation duties, fine-exempt) from *manufacturer of an OSS product* (full Art 13/14, not exempt) — same codebase, different legal hats.

## Anti-patterns
- **Assuming "we just resell" means no duties**: distributors have real verification + vulnerability-relay + MSA-cooperation obligations (Art 20); pure pass-through is not a thing in CRA.
- **White-labelling without realizing you became the manufacturer**: rebranding triggers full Art 13+14 on the reseller/integrator (Art 21) — the original maker's CE doesn't transfer automatically to your branded version.
- **Treating "substantial modification" as cosmetic**: any change affecting Annex I Part I compliance or intended purpose counts; a firmware feature add can qualify.
- **Conflating OSS steward exemption with product exemption**: the fine waiver (Art 64(10)(b)) is for stewards' own infringements, not for companies shipping OSS-based products under their name.

## Worked Example
Client: EU systems integrator that buys a Class I router from a non-EU OEM and sells it to enterprise customers under its own brand with a custom management overlay. Role analysis: (1) selling under own trademark → Art 21 makes the integrator the *manufacturer* for that product; (2) the custom overlay is very likely a substantial modification → independently triggers manufacturer status; (3) the non-EU OEM should appoint an authorised representative (Art 18). Deliverable: re-scope the client as a full manufacturer (risk assessment, SBOM, support period, reporting duties all now theirs), draft the Art 18 mandate with the OEM, and stand up the Annex I matrix for the integrated product — not just a reseller verification checklist.

## Key Takeaways
1. Map every stakeholder to a role first; obligations attach to role, not company size (Art 3(12)).
2. Rebranding or substantial modification makes that party the manufacturer with full Art 13/14 duties (Art 21–22).
3. Importers verify + can block non-conforming product + escalate significant risk to MSAs (Art 19).
4. Distributors verify CE/docs, relay vulnerabilities to the maker, and notify MSAs on manufacturer disappearance (Art 20).
5. OSS stewards owe a documented cybersecurity policy + MSA cooperation, and are fine-exempt; OSS-product manufacturers are not (Art 24, Art 64(10)).
6. Non-EU manufacturers typically need an authorised representative to anchor EU obligations (Art 18).

## Connects To
- **ch01**: classification of the underlying product still drives which duties are "full".
- **ch02/ch04**: once escalated to manufacturer, all of those chapters apply to the rebranding/modifying party.
- **ch07**: importer/distributor/DoC/CE failures map to specific fine tiers (Art 64(3)).
