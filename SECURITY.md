# Security policy / 安全报告

## Never publish a secret

Do not put API keys, access tokens, passwords, private keys, session cookies, personal contact details, private repository URLs, or real customer data in an Issue, Discussion, pull request, screenshot, example, or test case.

If a secret was committed, deleting the visible line is not enough because it may remain in Git history. Revoke or rotate the secret first, then clean the history and verify it before publishing again.

## Reporting a vulnerability

After the public repository is created, use GitHub's **private vulnerability reporting** entry when available. Do not open a public Issue for an unpatched vulnerability or exposed credential.

Until private reporting is enabled, do not send secret material to the project. Open a public Issue containing only a non-sensitive request for a private reporting channel, without vulnerability details.

The project does not publish a personal email address for security contact. This protects the steward's private identity and prevents the README from becoming a spam target.

## Response targets

- acknowledge a private report within 7 days when maintainers are available;
- assess severity and exposure before discussing details publicly;
- rotate exposed credentials immediately;
- publish a plain-language advisory after a fix, without exposing victims or reusable secrets.

These are project targets, not a warranty or guaranteed service level.

