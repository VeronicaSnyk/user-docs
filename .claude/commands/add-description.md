---
description: Generate and add a GitBook frontmatter description to one or more markdown files. Usage: /add-description <file-or-directory>
argument-hint: <file.md or docs/section/>
allowed-tools: Read, Glob, Edit, Write
---

Add a `description:` field to the GitBook YAML frontmatter of the markdown file(s) at: $ARGUMENTS

## What to do

1. If `$ARGUMENTS` is a single `.md` file, process that file only.
2. If `$ARGUMENTS` is a directory, find all `.md` files in it (non-recursively unless it has no `.md` files at the top level — then go one level deeper). Process up to 20 files at a time to avoid context overflow.
3. For each file:
   - Read the file
   - Write a `description:` value: one sentence, 15–25 words, present tense, active voice, no filler words ("just", "simply", "learn how to"), no brand possessives ("Snyk's")
   - The description should answer: "What will a reader accomplish or understand after reading this page?"
   - Good examples:
     - `Configure single sign-on for your Snyk organization using Okta as the identity provider.`
     - `Set up the Snyk Broker to connect Snyk to your on-premises source control manager.`
     - `Understand how the Deployed risk factor identifies vulnerabilities in running workloads.`
   - Bad examples (too vague): `This page covers Snyk settings.` / `Learn about integrations.`
   - If the file already has a `description:` field that is non-empty and specific, leave it unchanged.

4. Insert or update frontmatter:
   - If the file starts with `---`, it already has frontmatter — add `description: <value>` after the opening `---` line (before any other fields), or replace an existing empty/generic description
   - If the file does NOT start with `---`, prepend this block:
     ```
     ---
     description: <generated value>
     ---

     ```
   - Preserve all other frontmatter fields exactly as-is

5. After processing, report:
   - How many files were updated
   - How many were skipped (already had a good description)
   - List each file and its new description (or reason for skip)

## Style rules (from the repo writing guide)

- Active voice, present tense
- Second person where natural ("you" / "your")
- Capitalize: Projects, Organizations, Groups, Snyk Code, Snyk Open Source, Snyk Web UI
- No Latin abbreviations (use "for example" not "e.g.")
- No modal verbs ("should", "may", "might")
- No filler: "just", "simply", "currently", "please"
