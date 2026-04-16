## What does this PR do?

<!-- One or two sentences. What changed and why? Link to the relevant ticket or issue if applicable. -->

## Type of change

- [ ] New topic or page
- [ ] Update to existing content (accuracy, freshness)
- [ ] Restructure or move content
- [ ] Screenshot or image update
- [ ] Bug fix (broken link, typo, formatting)
- [ ] Automated sync (API docs, error catalog)

---

## Content quality checklist

### Writing rules
- [ ] Active voice used throughout
- [ ] Present tense (no "will be," "currently")
- [ ] No filler words ("just," "simply," "please," "actually")
- [ ] No Latin phrases ("e.g." → "for example," "i.e." → "that is," "via" → "through")
- [ ] No future tense ("will appear" → "appears")
- [ ] No modal verbs used for certainty ("should" → remove or rewrite)
- [ ] No AI buzzwords ("synergy," "cutting-edge," "leveraging," "seamless")

### Snyk terminology
- [ ] Projects, Groups, Organizations capitalized
- [ ] Product names correct: Snyk Code, Snyk Open Source, Snyk Web UI
- [ ] Tech names correct: Node.js, .NET, npm, GitHub, GitLab, CI/CD, DevOps
- [ ] No brand possessives ("Snyk's" → rewrite)

### Structure
- [ ] H1 heading matches the file's entry in SUMMARY.md
- [ ] Heading hierarchy is correct (no skipped levels)
- [ ] Numbered lists used for procedures; bulleted for unordered items
- [ ] Parallel construction in all lists

### Links and navigation
- [ ] All internal links verified (relative paths resolve correctly)
- [ ] No "click here" link text — descriptive text used
- [ ] Navigation uses "Navigate to X > Y" pattern
- [ ] If content was moved, a redirect added to `.gitbook.yaml`
- [ ] If a new page was added, it appears in `SUMMARY.md`

### Images and media
- [ ] All images have descriptive alt text
- [ ] Screenshots are current and reflect the live UI
- [ ] Images hosted in `.gitbook/assets/` (not Google Drive or external CDN)
- [ ] Image filenames are descriptive (not "image (12).png")
- [ ] No color used as the only way to convey information

### Accessibility
- [ ] No directional cues used alone ("see below" → use a link or heading)
- [ ] UI instructions don't rely on color ("click the green button" → use element name)

---

## Screenshots updated?

- [ ] Yes — screenshots reflect the current UI
- [ ] No screenshots in this change
- [ ] Screenshots not updated — existing ones are still accurate

## Tested locally?

- [ ] Previewed in GitBook (internal contributors)
- [ ] Links manually verified
- [ ] Vale run locally: `vale docs/<changed-file>.md`

---

<!-- For internal contributors: tag @docs-team for review via #request-ux-content -->
