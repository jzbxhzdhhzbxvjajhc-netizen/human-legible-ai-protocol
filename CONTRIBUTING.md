# Contributing / 参与维护

Thank you for helping AI speak to people who should not need a technical vocabulary first.

## Useful contributions

- a sentence that made an ordinary person stop or feel afraid to ask;
- a before/after rewrite grounded in a real-life problem;
- a missing START, CONTROL, or EXPLAIN evaluation case;
- a translation that preserves the same choice, consequence, and risk;
- a Skill or validation fix;
- evidence from a real user test, with private details removed.

## Before opening a pull request

1. Open or find an issue unless the change is a small typo.
2. Explain who got stuck, where, and what decision they needed to make.
3. Avoid adding a new unexplained technical term to explain the old one.
4. Add or update an evaluation case for behavior changes.
5. Run the checks listed in `evals/release-review-v0.1.1.md`.
6. Remove names, emails, phone numbers, API keys, tokens, private URLs, and real customer data.

## Language

English and Chinese contributions are both welcome. Other languages are welcome when a reviewer can check meaning. A translation is accepted only when it preserves the user's choice, consequence, risk, and next action—not merely similar wording.

## Contribution terms

By submitting a contribution, you confirm that you have the right to submit it and agree that it is licensed under the license already applying to that part of the repository:

- protocol, documentation, examples, and evaluation data: CC BY-SA 4.0;
- reference Skill and scripts: MPL 2.0.

You keep copyright in your contribution. Contribution does not grant maintainer status, ownership of project names, or authority to issue an official release or certification. See `GOVERNANCE.md` and `TRADEMARKS.md`.

During the initial `0.x` stage, Issues, Discussions, reviews, and proposed patches are welcome. The project will not merge a non-trivial or copyrightable outside contribution into normative protocol text or the reference implementation until its contribution-rights process has received appropriate legal review. Small factual corrections and material already clearly licensed for inclusion may be handled case by case with a public record. This pause avoids promising that community-owned work can later be relicensed by the founding steward alone.

## 中文入口

不需要先成为开发者。你只要能指出“这句话普通人会在哪个词停住”“看完之后还是不知道点不点同意”，就是有效贡献。先开 Issue 讲清真实场景；不要上传真人隐私、公司秘密或任何 API Key。协议 `0.x` 初期欢迎提案和补丁，但在贡献权利流程经过法律复核前，项目暂不合并具有实质版权内容的外部改动。
