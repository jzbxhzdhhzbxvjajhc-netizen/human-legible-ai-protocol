# Public-release checklist / 公开发布检查

The release stops if any required item fails.

## Identity and privacy

- [ ] The public GitHub profile shows no private email, phone number, home/work location, or unwanted real photo.
- [ ] Git commits use the GitHub-provided `noreply` address or another intentionally public address.
- [ ] GitHub email privacy and push-protection settings have been reviewed.

## Ownership and maintenance

- [ ] `LICENSE`, `ATTRIBUTION.md`, `GOVERNANCE.md`, `TRADEMARKS.md`, `COMMERCIAL.md`, and `MAINTAINERS.md` match the chosen release strategy.
- [ ] The canonical repository URL in `CITATION.cff` and templates is correct.
- [ ] GitHub Issues are enabled.
- [ ] GitHub Discussions are enabled.
- [ ] Private vulnerability reporting is enabled.
- [ ] Branch protection or a ruleset requires steward review for protected boundary files when the account/repository plan supports it.

## Skill and protocol

- [ ] All evaluation, bilingual, link, and Skill-structure checks pass.
- [ ] The official Skill validator passes in an environment with its required YAML dependency; otherwise the fallback limitation is disclosed.
- [ ] At least one fresh install of the packaged Skill has been tested outside the source folder.
- [ ] Known gaps in real-user and multi-model testing remain visible in the release review.

## Secret hard stop

- [ ] Current files pass the secret scan.
- [ ] Complete local Git history passes the secret scan.
- [ ] Final ZIP archives pass the secret scan.
- [ ] Any discovered credential was revoked or rotated before history cleanup; deletion alone is not treated as a fix.

## Release integrity

- [ ] Working tree is clean.
- [ ] The public commit author is intentional.
- [ ] Public history begins at the reviewed release commit; no pre-publication MIT commit or release-candidate tag is pushed.
- [ ] The release tag points to the reviewed commit.
- [ ] ZIP archives were rebuilt from that commit.
- [ ] SHA-256 checksums match the final archives.
