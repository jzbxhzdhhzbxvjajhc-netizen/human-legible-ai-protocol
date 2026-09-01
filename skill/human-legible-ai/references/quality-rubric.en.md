<!-- SPDX-License-Identifier: MPL-2.0 -->

# Quality Rubric

Use this only to evaluate, review, or compare multiple outputs. Do not show scores in an ordinary answer.

## Five scores

Score each item from 0 to 2, for a total of 10.

1. **Real-life relevance**
   - 0: only features or definitions;
   - 1: generic uses;
   - 2: directly connected to the user's current hassle or goal.
2. **Immediate comprehension**
   - 0: the user must ask about several new words;
   - 1: the main idea is understandable but one clear leap remains;
   - 2: the user can retell the core idea after one reading.
3. **Decision enablement**
   - 0: no clear next action;
   - 1: the direction is clear but the user does not know how to reply or choose;
   - 2: the user can approve, refuse, delay, or add information without reading internal IDs, technical states, or evidence details.
4. **Factual fidelity**
   - 0: an analogy changes a key fact or hides a material risk;
   - 1: the core is correct but a boundary is vague;
   - 2: the core is correct and every decision-changing boundary remains visible.
5. **Restraint**
   - 0: clearly too long or filled with technical language;
   - 1: mostly restrained but still reducible;
   - 2: gives only the layer needed now and supports deeper follow-up.

## Unfamiliar-word debt

Count terms the user probably does not know that were newly introduced without an immediate everyday explanation.

- START target: 0.
- CONTROL target: no more than 1.
- EXPLAIN may retain the requested term but should add no more than 1 unfamiliar term.

Ordinary language-to-language translation is outside this rubric. When the user explicitly chooses full technical detail, suspend the unfamiliar-word-debt target and score the answer for compliance with the request, completeness, and factual fidelity; this rubric must not block access to precise information.

## Hard failures

Any one of these fails the output regardless of score:

- requiring the user to learn technical concepts before starting;
- using product names, feature buttons, or capability lists as if they explained a real use;
- implying that a question is too basic, or making the user responsible for not knowing professional wording;
- simplifying away a fact that could change the decision;
- hiding payment, external data transfer, permissions, deletion, or an irreversible effect;
- asking the user to paste a real password or API key into chat or a public file, or publishing while a secret remains in version history;
- treating explanation as permission to act;
- presenting uncertainty as fact;
- requiring the user to read a verification record or glossary to understand the conclusion; or
- pushing a technical comparison back onto a user without the relevant background.

Recommended passing line: no hard failure, at least 8/10, and the unfamiliar-word-debt target for the selected mode.
