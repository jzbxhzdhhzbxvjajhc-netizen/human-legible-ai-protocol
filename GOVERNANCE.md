# Governance / 治理规则

This document answers a simple question: people around the world may help, but who decides what becomes the official protocol?

## Canonical project

The canonical project is the repository published at:

https://github.com/jzbxhzdhhzbxvjajhc-netizen/human-legible-ai-protocol

The founding steward is **@jzbxhzdhhzbxvjajhc-netizen**.

## Open participation

Anyone may:

- report language that ordinary people cannot understand;
- propose examples, translations, evaluation cases, or implementation fixes;
- review a proposal in public;
- create a compatible implementation or a clearly named fork under the applicable licenses.

Issues are for specific problems and proposals. Discussions are for questions, field reports, and broader design conversations. Pull requests are for reviewable changes.

## Decision roles

- **Contributors** submit or review work. Contribution does not automatically grant maintainer status or ownership of the project identity.
- **Maintainers** may triage issues, review tests, and merge changes within their documented responsibility.
- **Founding steward** appoints and removes maintainers and is the final decision maker for reserved matters during the `0.x` protocol stage.

Reserved matters are:

- changing the meaning or mandatory rules of the protocol;
- publishing an official version or conformance level;
- changing licenses, attribution, governance, or contribution terms;
- granting official status, official badges, or project-name exceptions;
- moving or declaring a new canonical repository.

These decisions require a public record and explicit approval from the founding steward. Routine typo fixes, broken links, and test corrections may be handled by maintainers.

Authority over licensing applies only to future versions and only where the project holds the necessary rights. Rights already granted under CC BY-SA 4.0 or MPL 2.0 are not withdrawn, and the founding steward cannot unilaterally relicense copyright owned by outside contributors.

## Change process

1. Open an issue describing the ordinary-person problem, not only the proposed technical fix.
2. Show a before/after example and identify any decision or risk that could be lost.
3. Add or update an evaluation case when behavior changes.
4. Allow public review. Security reports follow `SECURITY.md` instead.
5. Record the decision in the pull request or issue before merging.

No silent change may redefine an already published protocol version. Corrections that change meaning require a new version.

Every proposed change must be classified under `VERSIONING.md`. A normative change requires a migration note, updated evaluation evidence, and a `CHANGELOG.md` entry. The founding steward approves the final classification during the `0.x` stage. Published tags are immutable; a correction is a new version, never a replacement with the same number.

## Maintainer window

The project is ready to receive global reports and proposed changes through GitHub Issues, Discussions, and pull requests once those features are enabled. The public maintainer list begins with the founding steward. New maintainers must be named in `MAINTAINERS.md`, with their scope and appointment recorded publicly.

## Succession and forks

The founding steward may appoint a successor in a signed or publicly verifiable repository record. No contributor group may silently replace the canonical steward or claim an unofficial fork is the official project. If the canonical project becomes inactive, the licenses still allow community forks, but forks must identify themselves clearly and must not imply official status.

## 中文一句话

全球开发者可以提问题、交案例、做翻译和改实现；但在协议 `0.x` 阶段，改变规则、发正式版本、授予“官方”身份，以及改许可和治理，最终由发起人 **@jzbxhzdhhzbxvjajhc-netizen** 决定，并且必须留下公开记录。
