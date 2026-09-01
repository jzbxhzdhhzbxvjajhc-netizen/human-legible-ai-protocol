# My Mom Can Understand AI Now

[中文](README.md) · **English**

**Human-Legible AI Protocol (HLAI Protocol) v0.1.1**

> This does not teach ordinary people to speak AI. It makes AI speak in words ordinary people can use.

Technical teams often treat basic explanations as trivial. People outside tech can see the same unfamiliar words as proof that they are not qualified to ask. HLAI removes that false mystery: **people may describe the problem in their own words; the burden of translation belongs to the AI, not the user.**

HLAI is a platform-independent communication protocol. It translates AI capabilities into real-life problems, and translates AI actions and technical choices into language people can understand, question, approve, delay, or refuse.

It prevents two moments of failure:

1. **Never starting:** “What can I actually use AI for?”
2. **Losing control after starting:** “What is it about to do, and should I agree?”

## A 20-second example

Typical AI answer:

> I can create projects, develop applications, process data, and automate workflows.

HLAI answer:

> Think of something you repeatedly do on a computer that is annoying or easy to get wrong: combining spreadsheets, tracking income, renaming many files, or sorting photos. Tell me one specific hassle. I will first say whether I can make it easier and what I would need from you. You do not need to know what “code” or a “project” means.

## What v0.1.1 contains

- [Protocol](PROTOCOL.en.md): purpose, modes, mandatory rules, safety requirements, and conformance;
- [Founding statement](ORIGIN.md): the original problem definition, ten claims, steward, and public timeline;
- [Chinese source protocol](PROTOCOL.md): the original language version;
- [Assessment](ASSESSMENT.md): category definition, adjacent products, risks, and strategy;
- [First-tool guide](guides/first-ai-tools.en.md): an English plain-language guide to ChatGPT, Codex, WorkBuddy, and Doubao mobile, with a [Chinese version](guides/first-ai-tools.zh-CN.md);
- [Evaluation cases](evals/cases.jsonl): 25 Chinese cases plus 9 bilingual decision-parity cases;
- [English Before / After examples](examples/before-after.en.md): 12 common points where people drop out;
- [ChatGPT desktop / Codex reference Skill](skill/human-legible-ai/SKILL.md): one Skill that answers in the user's language;
- [Pre-release Skill review](evals/release-review-v0.1.1.md): structure, safety, bilingual coverage, scenarios, and known validation limits;
- [72-hour response plan](ROADMAP.md): immediate real-user validation and fast correction after the first release.

## One Skill, not one Skill per language

The reference Skill detects and follows the user's language. It does not translate technical labels word for word. It preserves three things across languages:

1. the real-life effect the user needs to understand;
2. the risk or tradeoff that could change the decision;
3. the next action the user is able to take.

For example, Chinese should explain `审计` first as `把做过的事和依据检查一遍`. English should first say `check what was done and why`. Only then, if useful, should either version add the technical label `audit`.

## Use it now—no installation required

Send this to any AI you already use:

> Assume I can use an ordinary phone and computer but do not know AI or software-industry terms. The thing bothering me is: ____. First tell me in everyday language whether you can help and what you need from me. Point out anything that would send, delete, publish, cost money, or be hard to undo. Do not begin with a feature list. When I need to decide, tell me the kind of reply I can give.

If you use ChatGPT desktop or Codex and already work with Skills, install [skill/human-legible-ai](skill/human-legible-ai) to apply these rules throughout a conversation. On ChatGPT web or mobile, copy the prompt above; this first release is not distributed as a plugin. Developers can implement [the protocol](PROTOCOL.en.md) directly. The Skill is only a reference implementation; the protocol is the core.

## Strategic boundary

HLAI does not monitor other apps, collect content the user did not provide, guarantee that the underlying technical plan is correct, or treat explanation as permission to write, delete, pay, publish, or send data.

Implementations may claim `HLAI-START`, `HLAI-CONTROL`, `HLAI-EXPLAIN`, or `HLAI-FULL` conformance. See the protocol for the test requirements.

## Global maintenance

After publication, anyone may report an ordinary-person drop-off through Issues, discuss field experience in Discussions, or submit translations, examples, evaluations, and implementation fixes through pull requests. See [Contributing](CONTRIBUTING.md), [Governance](GOVERNANCE.md), and [Security](SECURITY.md).

During the `0.x` stage, changes to protocol meaning, official releases, licensing, governance, and official certification require a public record and final approval from founding steward [@jzbxhzdhhzbxvjajhc-netizen](https://github.com/jzbxhzdhhzbxvjajhc-netizen). Global participation does not silently transfer the canonical project identity.

The public history begins with the reviewed `v0.1.1` content as a clean root commit. Private pre-publication candidate history is not included in the public repository.

## Open adoption and commercial boundary

- Protocol text, documentation, examples, and evaluations use **CC BY-SA 4.0**: reuse and commercial use are allowed, while shared copies and adaptations require attribution, change indication, and share-alike terms.
- The reference Skill and validation scripts use **MPL 2.0**: commercial use is allowed, while distributed modifications to covered files remain available in source form.
- Project names, official releases, and official certification are not licensed as product branding. Others may truthfully claim compatibility; they may not claim unofficial work is official.

Read [LICENSE](LICENSE), [Attribution](ATTRIBUTION.md), [Project-name policy](TRADEMARKS.md), and [Commercial boundary](COMMERCIAL.md). These protections preserve attribution for copied material, the canonical release, and official service opportunities. They do not create ownership of the abstract idea that AI should speak plainly.

## License

Protocol material: CC BY-SA 4.0. Reference Skill and scripts: MPL 2.0. See [LICENSE](LICENSE) for the file-by-file scope.
