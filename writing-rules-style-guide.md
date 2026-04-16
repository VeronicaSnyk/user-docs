# Snyk writing rules

> The Snyk writing rules take precedence for all Snyk R&D content. For any stylistic or grammatical scenarios not explicitly covered here, defer to the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

## Table of contents

- [Audience (persona)](#audience-persona)
- [Core principles](#core-principles)
- [Global, inclusive, and bias-free communication](#global-inclusive-and-bias-free-communication)
- [Accessibility](#accessibility)
- [Grammar, style, and tone](#grammar-style-and-tone)
- [Lists](#lists)
- [Formatting and punctuation](#formatting-and-punctuation)
- [Word choice and usage](#word-choice-and-usage)
- [Documenting the user interface (UI)](#documenting-the-user-interface-ui)
- [Messages (success, warnings, errors)](#messages-success-warnings-errors)
- [Abbreviations and acronyms](#abbreviations-and-acronyms)
- [Quick-reference substitutions](#quick-reference-substitutions)

---

## Audience (persona)

If you reach for too many audiences, you'll miss them all. How you write to an advanced user will always differ from how you write to a novice.

- **Writing to a developer new to security?** Explain the basics clearly and provide easy-to-follow steps.
- **Writing to a CISO looking for a new SAST?** Don't waste time on basic definitions. Show how Snyk overcomes the limitations of existing tools.

---

## Core principles

- **Write for scannability:** Users scan, they don't read. Structure your content with clear headings, short paragraphs, and lists.
- **Give the conclusion first (inverted pyramid):** Write key points and answers first so users can decide whether to read the supporting details.
- **Use headings as keywords:** Headings should be short, use keywords users would search for, and make the topic clear at a glance. Avoid starting a topic with "This guide describes."
- **Use content chunks:** Use short, digestible paragraphs with enough white space between chunks.
- **Omit needless words:** Make every word count. Avoid filler words that don't add meaning.
  - **Good:** Follow these steps to change your password.
  - **Bad:** Follow these steps in order to change your password.

---

## Global, inclusive, and bias-free communication

Snyk reaches a global audience. Content must be respectful, inclusive, and easy to understand for everyone, including non-native English speakers.

- **Inclusive language:** Do not use terms that may show bias regarding gender, race, culture, ability, or age.
  - Use gender-neutral terms (for example, "chairperson" instead of "chairman").
  - Use "they/them" as the default non-gendered pronoun.
  - Portray people with disabilities positively. Use "people with disabilities" instead of "the disabled".
  - Use "allowlist" instead of "whitelist" and "blocklist" (or "denylist") instead of "blacklist". Do not modify these terms if the software uses them specifically.

- **Avoid slang, jargon, and idioms:** Do not use U.S.-centric sports or military metaphors (for example, avoid "hit a home run" or "demilitarized zone").

- **Avoid non-English words:** Do not use Latin or other non-English phrases, even if they seem common.
  - Use "for example" instead of "e.g."
  - Use "that is" instead of "i.e."
  - Use "and so on" instead of "etc."
  - Use "through" or "using" instead of "via"
  - Use "note" instead of "N.B."

- **Avoid AI-sounding buzzwords:** Do not use phrases like "in this new era," "in the ever-evolving landscape," "delivering seamless and intuitive user experiences," "driving innovation through cutting-edge technology," "leveraging advanced tools and methodologies," or "synergy."

- **Language (US English):** Default to US English spelling and grammar (for example, "analyze" not "analyse").

- **Be careful with art:** Avoid hand signs, holiday themes, or specific flags that could be offensive or misunderstood in other cultures.

---

## Accessibility

- **Provide alt text:** All non-text elements (graphics, video) must have descriptive alt text for screen readers.
- **Don't use color alone:** Do not use color as the only way to convey information.
- **Avoid vague directional cues:** Do not use "left," "right," "above," or "below" as the only clue to location.
  - **Good:** In the **Save As** dialog box, click **OK**.
  - **Bad:** In the dialog box on the left, click **OK**.
- **Document all keyboard shortcuts** for users who cannot use a mouse.

---

## Grammar, style, and tone

### Active voice

Use active voice. In active voice, the subject does the action.

- **Good:** Patch logged into the account.
- **Good:** You can change your password.
- **Bad:** The account was logged into by Patch.
- **Bad:** This functionality enables the users to change their passwords. → **Use:** You can change your password.

### Tense

Use the present tense unless you have no choice. Avoid "will be" and imprecise words like "currently."

- **Good:** After you click **Start**, the start screen appears.
- **Bad:** After you click **Start**, the start screen will appear.

### Pronouns

Write in the first person plural ("we," "us") or second person ("you"). Avoid "I." When possible, use imperatives instead.

- **Best:** Click **Start** to begin the scan.
- **Good:** Now we can see the full list of vulnerabilities.
- **Bad:** Now I can see the full list of vulnerabilities.

### Avoid modal verbs

Modal verbs (may, should, might) add uncertainty. Use them sparingly.

- **Good:** Snyk identifies vulnerabilities in your dependencies.
- **Bad:** Snyk should identify vulnerabilities in your dependencies.

### Avoid "please"

Avoid "please." It is often unnecessary and can sound condescending. Use it only when the situation is inconvenient for the user or when the software is at fault.

- **Good:** Click **Save**.
- **Bad:** Please click the **Save** button.

### Avoid subjective and filler words

Do not use "simply," "easy," "fast," "just," "actually," "literally," "very," or "really." What is easy for one user may be difficult for another.

- **Good:** To publish, click **Publish to Web**.
- **Bad:** To publish, simply click **Publish to Web**.

### Brand possessives

Avoid possessives for brand names.

- **Good:** The Priority Score feature in Snyk Code ranks vulnerabilities.
- **Bad:** Snyk Code's Priority Score ranks vulnerabilities.

---

## Lists

### List type

- Use **bulleted lists** when order is unimportant.
- Use **numbered lists** for a sequence of steps (procedures).

### Procedure steps

Use the imperative mood (a command) for steps in a numbered list.

**Good:**
1. Click **Start**.
2. Type your password.

**Bad:**
1. You should click the **Start** button.
2. Then you will type your password.

### Parallel construction

If you start one item with a verb, start all items with a verb of the same tense.

- **Good:** Snyk can find vulnerabilities, suggest fixes, and recommend updates.
- **Bad:** Snyk is great for finding vulnerabilities, base image update reporting, and secure coding.

### Punctuation and capitalization

- If items are complete sentences, capitalize the first word and end with a period.
- If items are fragments that complete the introductory sentence, start with a lowercase letter and use no end punctuation.
- Do not add commas (,) or semicolons (;) to the end of list items.

---

## Formatting and punctuation

### Placeholders

Use *italics* for placeholder values the user must replace with their own information.

- *Example:* `git clone https://github.com/`*`your-username`*`/`*`your-repo`*`.git`
- *Example:* Navigate to **Settings** > **Organization** > *your-org-name*.

### Spacing

Use one space after a period, not two.

### Ampersands (&)

Do not use ampersands unless required by a space limit. Use "and."

### Apostrophes (')

Do not use apostrophes in plurals of abbreviations or dates (for example, "APIs" or "1990s").

### Colons (:)

- Use colons to introduce lists.
- The first word after a colon in a sentence is lowercase unless it is a proper noun.
- Capitalize the first word after a colon in a title.

### Commas (,)

- Default to using the serial (Oxford) comma.
- Avoid comma splices.
  - **Good:** Snyk is a security platform. It helps developers code securely.
  - **Bad:** Snyk is a security platform, it helps developers code securely.

### Dashes and hyphens

- **Hyphen (-):** Use to combine compound modifiers (for example, "client-side" or "read-only"). Do not hyphenate adverbs ending in -ly.
- **En dash (–):** Use to indicate a range, meaning "through" (for example, "pages 37–59").
- **Em dash (—):** Use to create a strong break in a sentence. Put spaces on both sides.

### Exclamation points (!)

Use sparingly. Overexcitement reads as disingenuous. Prefer a period.

### Semicolons (;)

Use sparingly. They often signal an overcomplicated sentence.

### Plurals

Do not use parentheses to indicate a plural.

- **Good:** ...displays one or more repositories.
- **Bad:** ...displays the repository(s).

---

## Word choice and usage

### Names and capitalization

| Term | Correct form | Notes |
|------|-------------|-------|
| Snyk Projects | **Projects** | Always capitalized |
| Snyk Groups | **Groups** | Always capitalized |
| Snyk Organizations | **Organizations** | Always capitalized; spell out in full; use "company" where possible to reduce confusion |
| Snyk | **Snyk** | Not "snyk" |
| Snyk Code | **Snyk Code** | Not "snyk code" |
| Snyk Open Source | **Snyk Open Source** | Not "snyk open source" |
| Snyk Web UI | **Snyk Web UI** | Not "snyk app" or "snyk ui" |
| Node.js | **Node.js** | Not "NodeJS" |
| .NET | **.NET** | Not ".net" or ".Net" |
| Composer | **Composer** | |
| dep | **dep** | Lowercase |
| Fintech | **Fintech** | |
| infrastructure as code | **infrastructure as code** | Lowercase |
| DevOps | **DevOps** | Not "devops" |
| DevSecOps | **DevSecOps** | Not "devsecops" |
| AppSec | **AppSec** | Not "appsec" |
| GitLab | **GitLab** | Not "Gitlab" |
| GitHub | **GitHub** | Not "Github" |
| npm | **npm** | Not "NPM" |
| AI-BOM | **AI-BOM** | In commands, use `aibom` |
| CI/CD | **CI/CD** | Use a slash, not a space ("CI / CD") |

### Numbers

- Spell out numbers one through nine.
- Use numerals for 10 and greater.
- **Exception:** Always use numerals for measurements (3 cm), time, or in lists with other numerals.
- Spell out numbers that begin a sentence.
- Use commas as thousands separators for numbers with four or more digits (for example, 1,024 or 250,000).

### Decimals

- Use a period as the decimal separator (for example, 5.25 MB, not 5,25 MB).
- Avoid unnecessary trailing zeros (use 5% instead of 5.0%).

### Date and time

- Avoid purely numerical date formats. Use "April 15, 2026" or "04/15/2026" (not DD/MM/YYYY).
- Times: use a colon to separate hours and minutes (for example, 1:49 PM).
- Time ranges: use an en dash with no spaces (for example, 8:00 AM–5:00 PM).

### Prefer simple words

| Instead of | Use |
|-----------|-----|
| utilize / usage / utilization | use |
| commence / commencement | start |
| prior to / in advance of | before |
| in the event that | if |
| make sure | ensure |
| first of all | first |
| and/or | and |
| in order to | to |
| is able to | can |
| is required to | must |
| within | in |
| accordingly / furthermore / thereby / therefore | so |
| go to | navigate to |
| once (meaning "after") | after |
| via | through / using / by means of |

### Avoid "once" to mean "after"

- **Good:** After you enter the details, click **Submit**.
- **Bad:** Once you enter the details, click **Submit**.

### Place "only" carefully

"Only" comes immediately before the thing it limits.

### Verbs and nouns (common pairs)

| Verb form | Noun/adjective form |
|-----------|-------------------|
| back up | backup |
| click (action button) | — |
| select (checkbox/option) | — |
| log in | login |
| set up | setup |
| folder (UI) | directory (CLI) |

### Compound words and hyphenation

| Form | Adjective | Noun |
|------|-----------|------|
| client-side | client-side | client side |
| cloud-native | cloud-native | cloud native |
| open-source | open-source | open source |
| server-side | server-side | server side |
| real-time | real-time | real time |
| step-by-step | step-by-step | — |
| third-party | third-party | — |
| man-in-the-middle | man-in-the-middle | — |
| same-origin policy | same-origin policy | — |
| cross-site scripting | cross-site scripting | — |
| hard coded | hard coded | — |
| cheat sheet | — | cheat sheet |
| pull request | — | pull request |
| white paper | — | white paper |
| webhook | — | webhook |
| codebase | — | codebase |
| username | — | username |
| dropdown | dropdown | dropdown |
| lifecycle | — | lifecycle |
| runtime | runtime | runtime |
| standalone | — | standalone |
| cybersecurity | — | cybersecurity |
| knowledge base | — | knowledge base |
| data center | — | data center |
| web server | — | web server |
| website | — | website |
| email | — | email |
| Dockerfile | — | Dockerfile |

---

## Documenting the user interface (UI)

### Formatting UI elements

Use **bold** for UI elements. Match the capitalization of the UI element exactly.

- **Good:** Click **Start** to scan for vulnerabilities.
- **Good:** Navigate to **ORGANIZATION SETTINGS**.
- **Bad:** Click "Start" to scan for vulnerabilities.

### Be direct

Do not include the name of the UI element type ("button," "tab") unless needed for clarity.

- **Good:** Click **Update**.
- **Bad:** Click the **Update** button.

### Describing navigation

- Use "Navigate to" instead of "go to."
- Use a greater-than symbol (>) with spaces to separate sequential UI steps.
  - **Example:** Navigate to **Settings** > **Notifications**.

### Links

Add hyperlinks organically into sentences.

- **Good:** Learn more in the [Snyk IaC documentation](#).
- **Bad:** Click here to learn more about Snyk IaC.

---

## Messages (success, warnings, errors)

- **Success:** Tell the user what happened. If follow-up actions are needed, list them.
  - **Example:** Project monitoring was successfully stopped, but the webhook could not be removed. Ask the repository owner to delete the webhook.
- **Warnings:** Tell the user what the problem is and how to fix it.
  - **Example:** This organization is at the limit of the Starter plan. Any new Projects will be inactive. Upgrade your plan to continue.
- **Errors:** Be informative.
  - **Example:** Sorry, the page could not be found. It might be an old link or it may have moved.

---

## Abbreviations and acronyms

- Spell out an abbreviation or acronym the first time you use it, followed by the short version in parentheses.
  - First use: static application security testing (SAST)
  - Second use: SAST
- **Exception:** If the abbreviation is universally known (like API or HTML), you do not need to spell it out.
- CI/CD: Use a slash, not a space.

---

## Quick-reference substitutions

| Avoid | Use instead | Reason |
|-------|------------|--------|
| please | *(remove)* | Redundant and inconsistently used |
| simply / easy / fast | *(remove)* | Subjective; implies other things are hard |
| just / actually / literally / really / very | *(remove)* | Meaningless filler |
| once (meaning "after") | after | Clearer; avoids cultural ambiguity |
| will be | *(present tense)* | Write in present tense |
| currently | *(remove or rewrite)* | Lacks clear temporal placement |
| e.g. | for example | Avoid Latin for global readers |
| i.e. | that is | Avoid Latin for global readers |
| etc. / etc | and so on | Avoid Latin for global readers |
| N.B. | note | Avoid Latin for global readers |
| via | through / using | Via is geographic Latin |
| in order to | to | Shorter |
| make sure | ensure | Shorter |
| utilize / usage | use | Shorter |
| prior to / in advance of | before | Shorter |
| in the event that | if | Shorter |
| first of all | first | Shorter |
| and/or | and | Easier to parse |
| is able to | can | Shorter |
| is required to | must | Shorter |
| within | in | Shorter |
| go to | navigate to | Consistent UI language |
| (s) | *(plural form)* | Easier to parse |
| & | and | Avoid in body text |
| he / she | they / you | Gender-neutral |
| whitelist | allowlist | Inclusive language |
| blacklist | denylist | Inclusive language |
| NodeJS | Node.js | Correct casing |
| .net / .Net | .NET | Correct casing |
| Github | GitHub | Correct casing |
| Gitlab | GitLab | Correct casing |
| NPM | npm | Correct casing |
| drop-down | dropdown | Standardized form |
| pull-request | pull request | Standardized form |
| web-hook / web hook | webhook | Standardized form |
| code base | codebase | Standardized form |
| life cycle | lifecycle | Standardized form |
| run time / run-time | runtime | Standardized form |
| hard-coded | hard coded | Standardized form |
| step by step | step-by-step | Standardized form |
| third party (adj) | third-party | Standardized form |
| real time (adj) | real-time | Standardized form (adj only) |
| realtime (noun) | real time | Standardized form (noun only) |
| CI / CD | CI/CD | Standardized form |
| 1000 | 1,000 | Thousands separator |
| devsecops | DevSecOps | Correct casing |
| appsec | AppSec | Correct casing |
| snyk | Snyk | Correct casing |
| org / organization | Organization | Snyk-specific capitalization |
| project | Project | Snyk-specific capitalization |
| group | Group | Snyk-specific capitalization |
| snyk's | Snyk | Avoid brand possessives |
| This guide describes | *(use a descriptive title)* | Vague opener |
| in this new era | *(remove)* | AI-sounding buzzword |
| synergy | *(remove)* | AI-sounding buzzword |
| resonates | *(rephrase)* | Vague |
| not to mention / when it comes to | *(remove)* | Redundant filler |
