# Simple example of a Snyk task to run a code test

The following is a simple example of a Snyk task to run a Snyk Code test.

```yaml
- task: SnykSecurityScan@1
  inputs:
    serviceConnectionEndpoint: 'snykToken'
    testType: 'code'
    codeSeverityThreshold: 'medium'
    failOnIssues: true
```
