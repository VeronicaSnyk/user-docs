# Snyk User Docs — Claude Code Guide

## Project overview

This is a fork of the official [Snyk user documentation](https://docs.snyk.io) repository. Content lives in `docs/` and is published via GitBook.

## Git remotes

- `origin` — Fork: https://github.com/VeronicaSnyk/user-docs.git
- `upstream` — Official: https://github.com/snyk/user-docs.git

## Workflow

1. Always branch from a synced `main`:
   ```
   git fetch upstream && git merge upstream/main
   ```
2. Create a feature branch with a descriptive name (e.g., `fix-sso-typo`, `docs-manage-risk-overview`).
3. Push to `origin` (the fork), not `upstream`.
4. Open PRs targeting `upstream/main`, not `origin/main`.
5. Commits must be signed (repo requirement).

## Style and quality checks

- Full style guide: `writing-rules-style-guide.md` at the repo root
- Vale config: `.vale.ini` at the repo root
- Run Vale before committing: `vale docs/`
- Vale styles are in `.vale/`
- Fallback for anything not covered here: [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)

### Core writing rules (apply to all content)

**Voice and tense**
- Use active voice. Subject does the action.
- Write in present tense. Avoid "will be."
- Use second person ("you") or imperatives. Avoid "I."
- Avoid modal verbs (should, may, might) — they add uncertainty.

**Words to avoid**
- Filler: "just," "actually," "literally," "very," "really," "simply," "currently"
- Redundant: "please," "first of all," "in order to," "make sure," "is able to," "in the event that," "prior to," "and/or," "once" (use "after")
- Latin: "e.g." → "for example"; "i.e." → "that is"; "etc." → "and so on"; "via" → "through/using"; "N.B." → "note"
- AI buzzwords: "synergy," "in the ever-evolving landscape," "leveraging," "seamless," "cutting-edge"
- Brand possessives: not "Snyk's" → rewrite to avoid

**Snyk-specific capitalization**
- Always capitalize: **Projects**, **Groups**, **Organizations**, **Snyk Code**, **Snyk Open Source**, **Snyk Web UI**
- Correct product names: Node.js, .NET, npm, GitLab, GitHub, CI/CD, DevOps, DevSecOps, AppSec, AI-BOM
- Correct compound forms: webhook, codebase, lifecycle, runtime, dropdown, username, standalone, cybersecurity, Dockerfile

**Numbers**
- Spell out one through nine; use numerals for 10+
- Use commas as thousands separators: 1,000 not 1000
- Dates: "April 15, 2026" (not DD/MM/YYYY)

**Lists**
- Bulleted for unordered items; numbered for procedures
- Use imperative mood in steps ("Click Save", not "You should click Save")
- Parallel construction: if one item starts with a verb, all items start with a verb
- No trailing commas or semicolons on list items

**UI documentation**
- Bold UI elements: Click **Save**
- No element type unless needed: "Click **Update**" not "Click the **Update** button"
- Navigation: "Navigate to **Settings** > **Notifications**" (not "go to")
- Links: embed organically, never "click here"

**Inclusive language**
- Gender-neutral pronouns: they/them
- allowlist / denylist (not whitelist / blacklist) — unless the software uses those exact terms
- "people with disabilities" not "the disabled"
- No directional cues as the only locator ("above," "left," "below")

## Content structure

- All docs live under `docs/`
- Reusable content snippets are in `.gitbook/includes/`
- Planning notes are in `_planning/`
- GitBook summary and config are in `docs/SUMMARY.md` and `docs/.gitbook.yaml`

## CI/CD and automation

All workflows are in `.github/workflows/`. Do not modify the upstream sync workflows unless asked.

### Quality gate workflows (added for this fork)

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `docs-quality.yml` | PR touching `docs/**/*.md` | Vale style lint (inline PR comments), markdownlint syntax check, SUMMARY.md consistency |
| `link-checker.yml` | PR + weekly (Monday 6 AM UTC) | Internal broken links on PRs; external link rot weekly via lychee; creates a GitHub issue with report |
| `image-audit.yml` | PR + weekly (Tuesday 7 AM UTC) | Missing alt text (error), external image sources (warning), orphaned assets, generic filenames |

### Upstream sync workflows (do not modify)

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `sync-error-catalog.yml` | Monthly + manual | Syncs error catalog docs from `snyk/error-catalog` |
| `sync-api-docs.yml` | Hourly Mon–Fri + manual | Syncs API reference docs from OpenAPI spec |

### Running quality checks locally

```bash
# Style lint (Vale)
vale docs/<file>.md
vale docs/                        # full scan

# Markdown lint
npx markdownlint-cli2 "docs/**/*.md"

# Internal link check
python3 .github/scripts/check-links.py

# SUMMARY.md consistency
python3 .github/scripts/check-summary.py

# Image audit
python3 .github/scripts/audit-images.py
```

### Vale rules

Vale styles are in `.vale/styles/Snyk/`. Each file enforces one category:

| File | Level | What it flags |
|------|-------|--------------|
| `AIBuzzwords.yml` | error | "synergy," "cutting-edge," "leveraging," etc. |
| `PassiveVoice.yml` | warning | Passive constructions |
| `FutureTense.yml` | warning | "will be," "currently" |
| `ModalVerbs.yml` | warning | "should," "might," "may" |
| `Substitutions.yml` | warning | Latin, filler words, wrong compound forms, brand names |
| `SnykCapitalization.yml` | warning | Lowercase Snyk entities (projects, groups, orgs) |
| `HeadingStyle.yml` | suggestion | Vague heading openers |
| `Terms.yml` | warning | Snyk-specific terminology swaps |

### Scripts

All automation scripts are in `.github/scripts/`:

- `check-links.py` — validates all relative markdown links resolve to existing files
- `check-summary.py` — validates SUMMARY.md matches the docs/ file structure
- `audit-images.py` — audits alt text, orphaned assets, external image sources, generic names

### PR template

`.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` — all PRs get a pre-filled checklist covering writing rules, Snyk terminology, structure, links, images, and accessibility.

## Do not modify

- `upstream/main` — never push directly to upstream
- Signed commit requirement — do not use `--no-verify`
- `.github/workflows/sync-*.yml` — upstream-owned sync workflows
