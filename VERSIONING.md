# Protocol versioning / 协议版本规则

HLAI uses Semantic Versioning notation, but a communication protocol needs a stricter definition of what is compatible. The release is one reviewed bundle: protocol text, conformance rules, evaluations, reference Skill, and release evidence. The part with the highest compatibility impact determines the bundle version.

HLAI 使用语义化版本号的写法，但“协议兼容”不能只按代码接口理解。一次发布是经过同一轮审查的整体：协议正文、符合性规则、评测、参考 Skill 和发布证据。只要其中一部分需要更高等级的版本变化，整个发布就按最高等级升级。

## Normative surface / 规范性范围

The following can change what `HLAI-* conformant` means and are therefore normative:

- MUST, SHOULD, MAY, mode, safety, permission, and conformance requirements in `PROTOCOL.md` and `PROTOCOL.en.md`;
- required passing thresholds, hard failures, and evaluation cases used to establish conformance;
- a translation whose wording changes a user's choice, consequence, risk, permission, or required next action.

以下内容会改变“符合 HLAI”的含义，因此属于规范性内容：

- 协议正文中的必须、应、可以、模式、安全、授权和符合性规则；
- 用于判定符合性的必过门槛、硬失败条件和评测案例；
- 会改变用户选择、后果、风险、授权或必要下一步的翻译。

Examples, guides, wording cleanup, release evidence, and the reference Skill are non-normative only when they preserve protocol meaning. A file is not automatically non-normative merely because it lives outside `PROTOCOL.md`.

案例、指南、文字整理、发布证据和参考 Skill，只有在不改变协议含义时才属于非规范性内容。不能因为一个文件不在 `PROTOCOL.md` 里，就自动把它当成“只改文案”。

## Breaking-change test / 破坏性变更判断

A change is breaking when any of the following is true:

1. an implementation that conformed before the change becomes nonconforming without changing its behavior;
2. the same facts can now require a different approve, refuse, delay, permission, disclosure, or safety decision;
3. a mode, mandatory rule, hard failure, required output, or conformance claim changes meaning;
4. an existing public field, marker, or behavior that implementations reasonably depend on is removed or redefined.

只要符合下列任一项，就属于破坏性变更：

1. 一个原本合格的实现，在自身行为没变的情况下，因为新规则变成不合格；
2. 同一组事实现在可能要求不同的同意、拒绝、推迟、授权、披露或安全决定；
3. 模式、强制规则、硬失败、必需输出或符合性声明的含义发生变化；
4. 实现者已经合理依赖的公开字段、标记或行为被删除或重新定义。

Adding a new MUST or hard failure is not considered a harmless additive change. Tightening a safety boundary may be necessary, but it still receives the version required by its compatibility impact.

新增一个“必须”或硬失败条件，不算无害的功能追加。安全规则即使必须收紧，也不能用“只是补丁”掩盖它对兼容性的影响。

## Version rules before 1.0 / 1.0 前的规则

- `0.MINOR.0`: any normative semantic, conformance, permission, or safety change. Compatibility is not promised across different `0.MINOR` releases.
- `0.MINOR.PATCH`: editorial clarification, link or packaging repair, test-data correction, or reference-implementation bug fix that preserves protocol meaning and expected user decisions.

- `0.MINOR.0`：任何规范性语义、符合性、授权或安全变化。不同 `0.MINOR` 版本之间不承诺兼容。
- `0.MINOR.PATCH`：不改变协议含义和用户预期决定的文字澄清、链接或打包修复、测试数据纠错、参考实现缺陷修复。

Examples:

- adding a mandatory check before sending user data: `0.MINOR.0`;
- changing a hard-failure definition: `0.MINOR.0`;
- fixing a typo, dead link, archive layout, or Skill bug without changing required behavior: `0.MINOR.PATCH`.

## Version rules from 1.0 / 1.0 起的规则

- `MAJOR`: an incompatible normative change under the breaking-change test above;
- `MINOR`: a backward-compatible optional extension that does not invalidate a previously conforming implementation;
- `PATCH`: a meaning-preserving editorial, packaging, evidence, or implementation correction.

- `MAJOR`：符合上面破坏性判断的、不兼容的规范性变化；
- `MINOR`：不让旧合格实现失效的、向后兼容的可选扩展；
- `PATCH`：不改变含义的文字、打包、证据或实现修正。

## Security, deprecation, and migration / 安全、弃用与迁移

- A protocol-level security rule follows the same compatibility rules: before 1.0 it normally bumps `0.MINOR.0`; after 1.0 a breaking requirement bumps `MAJOR`.
- A reference-implementation security fix may use `PATCH` only when the normative protocol and expected decisions are unchanged.
- A planned removal should first be marked deprecated with a replacement and migration note. Removal waits for the next allowed breaking version unless immediate harm requires an emergency change.
- An emergency change must still be versioned and recorded; urgency is not permission to silently redefine an existing version.

安全变化也按兼容性定级：1.0 前的协议级安全规则通常升 `0.MINOR.0`；1.0 后若会破坏兼容则升 `MAJOR`。只有不改变协议含义和用户决定的参考实现安全修复，才可以使用 `PATCH`。计划移除的内容应先标记弃用、给出替代办法和迁移说明；紧急情况也必须留下新版本和公开记录，不能悄悄重定义旧版本。

## Release record / 发布记录

Every release must:

1. update `VERSION`, `CITATION.cff`, protocol headings, and current-version documentation consistently;
2. add a `CHANGELOG.md` entry that labels the change normative or non-normative;
3. state migration impact and the evaluations required for normative changes;
4. preserve already published tags and content; an existing version is never silently redefined.

The canonical version is the signed or annotated tag and release published by the canonical repository. Forks may use their own versions but must not present them as an official HLAI release.

官方版本以规范仓库发布的签名或附注标签及 Release 为准。分支项目可以使用自己的版本号，但不得把它说成 HLAI 官方版本。
