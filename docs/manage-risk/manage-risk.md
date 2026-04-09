# Overview

After you scan with Snyk, use these capabilities to understand, prioritize, govern, and track your application security posture across projects and teams.

## Get oriented

- **AppSec leads and security managers** → [Analytics overview](analytics/overview-tab.md), [Reports](analytics/reports-tab/), [Policies](policies/), [Risk Score](prioritize-issues-for-fixing/risk-score.md)
- **Developers** → [Prioritize issues](prioritize-issues-for-fixing/), [Ignore issues](prioritize-issues-for-fixing/ignore-issues/), [View dependencies](dependencies-and-licenses/view-dependencies.md)

## Prioritize issues

- Use scores to rank what to fix first: [Risk Score](prioritize-issues-for-fixing/risk-score.md) and [Priority Score](prioritize-issues-for-fixing/priority-score.md). See how they differ in [Priority Score vs Risk Score](prioritize-issues-for-fixing/priority-score-vs-risk-score.md).
- Improve accuracy with contextual signals:
  - [Reachability analysis](prioritize-issues-for-fixing/reachability-analysis.md)
  - [Exploit maturity](prioritize-issues-for-fixing/view-exploits.md)
  - [Malicious packages](prioritize-issues-for-fixing/malicious-packages.md)
- Bring application context with [Assets and risk factors](prioritize-issues-for-fixing/assets-and-risk-factors/) and [Set up Insights](prioritize-issues-for-fixing/set-up-insights/).

{% hint style="info" %}
Feature availability

Prioritization with Insights and assets and risk factors is available with Snyk Essentials. Risk Score is in Early Access as described in the docs above. See [Snyk Essentials](../scan-with-snyk/snyk-essentials.md) or contact Snyk for details.
{% endhint %}

## Policies

- Govern how issues are treated using [Security policies](policies/security-policies/) and [License policies](policies/license-policies/). Apply actions such as changing severity or ignoring issues that match conditions.
- Use the [`.snyk` file](policies/the-.snyk-file.md) to define local policy and ignores for CLI and CI/CD.
- Classify and automate actions on your inventory with [Assets policies](policies/assets-policies/).

{% hint style="info" %}
Feature availability

Policies are available only with Snyk Enterprise plans and apply to relevant products as noted in each policy area. See the policy pages for details.
{% endhint %}

## Analytics and reports

- Start with the [Overview tab](analytics/overview-tab.md) to track KPIs and drill into coverage, exposure, remediation, and prevention.
- Use the [Reports tab](analytics/reports-tab/) to analyze and share data across your tenant, Groups, or Organizations. Report categories include:
  - [Exposure and coverage](analytics/reports-tab/exposure-and-coverage-reports.md)
  - [Remediation](analytics/reports-tab/remediation-reports.md)
  - [Prevention](analytics/reports-tab/prevention-reports.md)
  - [Compliance](analytics/reports-tab/compliance-reports.md)
  - [Education](analytics/reports-tab/education-reports.md)
- For advanced BI, connect your data warehouse with [Reporting and BI integrations: Snowflake Data Share](analytics/reports-tab/reporting-and-bi-integrations-snowflake-data-share/).

{% hint style="info" %}
Feature availability

Analytics and Reporting are available only with Snyk Enterprise plans (permissions apply). See the Analytics and Reports docs for details.
{% endhint %}

## Dependencies and licenses

- Use the [Dependencies](dependencies-and-licenses/view-dependencies.md) tab for a bill of materials across Projects. Filter by product, health, and deprecation to focus investigations.
- Audit the [Licenses](dependencies-and-licenses/view-licenses.md) tab to monitor license compliance. Severity is governed by your [license policies](policies/license-policies/create-a-license-policy-and-rules.md).
