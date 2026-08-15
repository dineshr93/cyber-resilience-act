# Cyber Resilience Act — Compliance Consultant Skill

An [Agent Skills](https://github.com/virgiliojr94/book-to-skill) knowledge base generated from the **Cyber Resilience Act — Regulation (EU) 2024/2847** (consolidated CELEX text + Official Journal L 2847) and the **European Commission's technical FAQs v13**, built for companies implementing full CRA compliance.

The skill is written as a **compliance consultant toolkit**: scope tests, product classification (default / important Class I & II / critical), manufacturer/importer/distributor duty maps, Annex I requirement matrices, vulnerability-handling pipelines, the 24h/72h/14-day reporting ladder, conformity-assessment route selection (modules A / B+C / H), penalties and key dates — plus reusable engagement patterns and a decision-rule cheatsheet.

## Install on any Agent Skills host

```bash
npx skills add https://github.com/dineshr93/cyber-resilience-act --skill cyber-resilience-act
```

Or copy the folder into your agent's skill directory (e.g. `~/.hermes/skills/`, `~/.claude/skills/`, `.agents/skills/`).

## Usage

Ask your agent for `cyber-resilience-act` to load the core decision rules, or ask about a topic:

- "Is my product in scope under CRA?"
- "We white-label a Class I router — what are our obligations?"
- "What must be done by 11 September 2026 (reporting) and 11 December 2027 (general application)?"
- "Build the Annex I applicability matrix for a smart thermostat"

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | Core decision rules, chapter + topic indexes |
| `chapters/ch01–ch08` | Scope & classification · manufacturer duties (Art 13) · Annex I requirements · reporting (Art 14–17) · conformity assessment & CE · importers/distributors/OSS stewards · penalties, surveillance & dates · Commission FAQ guidance |
| `cheatsheet.md` | Decision tables: scope test, tier→route matrix, fine tiers, hard dates, tells & smells |
| `patterns.md` | 9 reusable engagement patterns (scope memo, role matrix, reporting runbook…) |
| `glossary.md` | Key terms with article references |

## Notes

- Content is **synthesized summaries and decision rules**, not the raw regulation text. The authoritative texts are [EUR-Lex: Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) and the Commission's CRA FAQs.
- This is compliance guidance, **not legal advice**. Borderline classification or sectoral-interplay calls should be routed to counsel.
- Harmonised-standard coverage (the Class I self-declaration escape hatch) and FAQ content evolve — re-verify current state for time-sensitive decisions.

## License

MIT — see [LICENSE](LICENSE). Free to use, modify, and redistribute; the underlying EU regulatory text is the property of the European Union and is freely reproducible per EUR-Lex terms.
