# Cyber Resilience Act — Compliance Consultant Skill

An [Agent Skills](https://github.com/virgiliojr94/book-to-skill) knowledge base generated from the **Cyber Resilience Act — Regulation (EU) 2024/2847** (consolidated CELEX text + Official Journal L 2847) and the **European Commission's technical FAQs v13**, built for companies implementing full CRA compliance.

The skill is written as a **compliance consultant toolkit**: scope tests, product classification (default / important Class I & II / critical), manufacturer/importer/distributor duty maps, Annex I requirement matrices, vulnerability-handling pipelines, the 24h/72h/14-day reporting ladder, conformity-assessment route selection (modules A / B+C / H), penalties and key dates — plus reusable engagement patterns and a decision-rule cheatsheet.

## Install

The skill works on any Agent Skills host. Two options:

### Option A — `npx skills add` (book-to-skill / Agent Skills host)

```bash
npx skills add https://github.com/dineshr93/cyber-resilience-act --skill cyber-resilience-act
```

### Option B — copy the folder into your agent's skills directory

Clone (or download) the repo, then copy the `cyber-resilience-act/` folder into your agent's skills path:

```bash
git clone https://github.com/dineshr93/cyber-resilience-act.git
cp -r cyber-resilience-act ~/.hermes/skills/          # Hermes Agent
cp -r cyber-resilience-act ~/.claude/skills/          # Claude Code / Claude Desktop
cp -r cyber-resilience-act .agents/skills/            # other Agent Skills hosts
```

The folder is fully self-contained: `SKILL.md` is the entry point, with `chapters/`, `cheatsheet.md`, `patterns.md`, and `glossary.md` alongside it. No external dependencies and no runtime network calls — the knowledge base is read locally by the agent.

## Leverage — what to ask

Once installed, the agent auto-loads this skill whenever you ask anything CRA-related and answers as a compliance consultant — producing decisions, obligation maps, checklists, and tooling recommendations rather than summaries of the regulation. Ask for the skill by name, a topic, or a chapter:

| You ask… | The skill returns… |
|---|---|
| "Is my product in scope under CRA?" | The Art 2(1) scope test plus the exclusion chain, with citations |
| "We white-label a Class I router — what are our obligations?" | Role-escalation analysis: you become the manufacturer (Art 21–22) |
| "What must be done by 11 September 2026 and 11 December 2027?" | The 24h/72h/14-day reporting ladder and the application timeline |
| "Build the Annex I applicability matrix for a smart thermostat" | The (a)–(m) requirement matrix with N/A justifications |
| "Which conformity route do we need for a VPN client?" | Module A vs B+C vs H, keyed to harmonised-standard coverage |
| "What are the fines if we miss a reporting deadline?" | Fine tiers plus the narrow SME/OSS steward waivers |
| "We're an OSS foundation — do we have obligations?" | OSS steward vs OSS-product-manufacturer distinction |
| "What chapters do you have?" | The chapter + topic index for browsing |

For a quick answer start with `cheatsheet.md` (decision tables); for a deeper engagement ask for `patterns.md` (scope memo, role matrix, reporting runbook, …) or a specific `chXX` chapter.

### Worked example — component supplier to automotive OEMs

Invoke the skill by name with a real engagement prompt, and it returns a set of decision artifacts (not just a summary). Example:

```bash
/cyber-resilience-act what are the suppliers obligations who sells ECU and Infotainment software to OEMs both in EU and non-EU market. We are sell ECU hardare too for some OEMs. Provide an actionable executive summary. stick to facts as it is high stake penalities are involved for bad adise.
```

That run produces an `artifacts/` folder — the actionable deliverables the consultant would hand a client:

| File | What it is |
|---|---|
| `artifacts/00-executive-summary.md` | Top-line verdict: scope falls into two buckets (type-approved components likely out via Art 2(2)(c), standalone software/remote-data-processing firmly in), your role = manufacturer (Art 13+14), reporting is live now (Art 14, Tier-1 fines), non-EU exposure is contractual (UNECE R155 flow-down), plus a priority action list |
| `artifacts/01-scope-memo.md` | The Art 2(1) 3-question test + exclusion ladder, with the Bucket A vs Bucket B classification and the counsel flag |
| `artifacts/02-role-matrix.md` | Stakeholder → CRA role mapping (you, OEM, reseller, importer, distributor) with the Art 21–22 manufacturer-escalation traps and contract-review checklist |
| `artifacts/03-annex-i-matrix.md` | Requirement-by-requirement Annex I (a)–(m) + Part II(1)–(8) applicability template with control → evidence pairs |
| `artifacts/04-reporting-runbook.md` | The 24h/72h/14-day Art 14 ladder, channels (CSIRT + ENISA single platform), component-exploit rule, and operational checklist |

The same invocation pattern works for any engagement — swap the prompt and the skill writes the matching artifact set under `artifacts/`.

### Worked example

> **Prompt:** "We manufacture a smart-home security hub. Which conformity route do we need, and what standing artifacts must we keep?"
>
> The skill loads ch01 (classification) + ch05 (conformity) and returns: the hub's core functionality (smart-home security) lands it in **Important Class I**, so module A self-declaration is available **only if** you fully apply OJ-published harmonised standards; otherwise a notified body (B+C or H) is required. It then lists the four standing artifacts every manufacturer must keep — living risk assessment, the Annex I (a)–(m) applicability matrix, a machine-readable SBOM, and the vulnerability-handling pipeline — and flags that white-labelling would escalate your duties.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | Core decision rules, chapter + topic indexes |
| `chapters/ch01–ch08` | Scope & classification · manufacturer duties (Art 13) · Annex I requirements · reporting (Art 14–17) · conformity assessment & CE · importers/distributors/OSS stewards · penalties, surveillance & dates · Commission FAQ guidance |
| `cheatsheet.md` | Decision tables: scope test, tier→route matrix, fine tiers, hard dates, tells & smells |
| `patterns.md` | 10 reusable engagement patterns (scope memo, role matrix, reporting runbook…) |
| `glossary.md` | Key terms with article references |

## Notes

- Content is **synthesized summaries and decision rules**, not the raw regulation text. The authoritative texts are [EUR-Lex: Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) and the Commission's CRA FAQs.
- This is compliance guidance, **not legal advice**. Borderline classification or sectoral-interplay calls should be routed to counsel.
- Harmonised-standard coverage (the Class I self-declaration escape hatch) and FAQ content evolve — re-verify current state for time-sensitive decisions.

## License

MIT — see [LICENSE](LICENSE). Free to use, modify, and redistribute; the underlying EU regulatory text is the property of the European Union and is freely reproducible per EUR-Lex terms.
