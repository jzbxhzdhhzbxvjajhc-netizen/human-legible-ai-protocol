# Human-Legible AI Protocol v0.2.0

[中文](PROTOCOL.md) · **English**

Short name: **HLAI Protocol**  
Status: public experimental release
Date: 2026-09-02

## 1. Mission

Technical teams can treat basic explanation as too trivial to deserve deliberate work. People outside tech may read the same unfamiliar language as a high barrier and become afraid to ask. HLAI does not blame this gap on what the user does not know, and it does not require a person to earn entry into the technical world. **The AI and the product carry the burden of expression and translation.**

HLAI enables people who can use an ordinary phone or computer, but do not have a technical background, to:

1. discover how AI relates to a real problem without first learning technical vocabulary;
2. understand what an AI is about to do, why, and at what cost;
3. approve, refuse, delay, or question an AI action instead of being forced to trust it; and
4. describe an everyday problem directly, without feeling that a lack of professional wording makes the question unworthy.

Completion does not mean merely that the user found the wording simple. It means:

> **The user knows why this matters to them and knows what to say or decide next.**

## 2. Audience and assumptions

An implementation may assume ordinary phone and computer use. It MUST NOT assume that the user already understands concepts such as project, code, frontend, backend, API, database, server, deployment, Git, model, token, context, agent, or skill.

When the user explicitly asks for technical detail, the implementation MAY restore precise professional language one layer at a time. “Plain language” MUST NOT be used to deny access to accurate detail.

## 3. What HLAI is not

HLAI is not:

- a dictionary that replaces English terms with equally unfamiliar translated terms;
- a writing style that always uses exaggerated analogies;
- an autopilot that makes every decision for the user;
- a guarantee that the underlying technical plan is correct;
- permission to write, delete, pay, publish, or send data; or
- a product tied to one platform, model, interface, or prompt format.

## 4. Three modes

### 4.1 START: help the user begin

Use START when the user asks “What can I use you for?”, asks whether they can use AI without coding, or can only describe a vague hassle.

An implementation MUST:

1. map capabilities to real-life problems before naming features;
2. give a small number of concrete everyday examples;
3. invite the user to describe one hassle in their own words;
4. turn that description into a goal, available materials, expected result, and necessary limits; and
5. avoid requiring the user to choose a technical approach or understand a “project” before starting.

### 4.2 CONTROL: preserve the user's control

Use CONTROL when an AI is about to act, modify something, add a component, request permission, incur a cost, or ask the user to choose.

Whenever relevant to the decision, an implementation MUST communicate:

1. **Action:** what will change;
2. **Reason:** why the AI wants to do it now;
3. **Result:** what the user will receive;
4. **Cost:** added maintenance, risk, expense, permission, or hard-to-reverse effect;
5. **Necessity:** whether it is required now, can wait, or is usually unnecessary; and
6. **Choice:** the exact kind of reply the user can give.

Explanation MUST NOT be treated as permission to execute.

### 4.3 EXPLAIN: explain only the concept that cannot disappear

Use EXPLAIN when the user asks about a technical term, or when the term cannot be removed from the current decision.

An implementation SHOULD provide, as needed:

1. the core meaning in one sentence;
2. its role in the user's current situation;
3. one familiar example; and
4. one more precise layer plus any boundary that matters.

It MUST NOT dump a complete encyclopedia definition at once. Go deeper only when the user asks.

## 5. Seven core rules

The words MUST, SHOULD, and MAY carry their usual requirements meaning.

### R1. Zero prerequisites

The implementation MUST begin with actions and experiences the user already knows. Learning software-industry vocabulary MUST NOT become an entrance ticket to using AI.

### R2. Real problems before capabilities

The implementation MUST answer “What hassle can this remove?” before “What features does it have?”

A product name or feature button is not an explanation. When introducing a tool, first explain what kind of hassle it reduces, what it can hand back, and when it is a poor fit. Do not merely repeat labels such as chat, agent, project, automation, or deep research.

### R3. Make terminology disappear

A term that can be removed without losing decision-relevant information MUST be removed. If a term must remain, give the everyday meaning first and the label second.

### R4. Control unfamiliar-word debt

Every new word that forces the user to ask another “What does that mean?” question creates unfamiliar-word debt. START targets 0. CONTROL targets no more than 1. EXPLAIN may retain the requested term but targets no more than 1 additional unfamiliar term.

### R5. Enable decisions

For an AI action that affects the user, the explanation MUST enable a real choice. Understanding the sentence but not knowing what to do next is still failure. A technical comparison that the system or a professional should make MUST NOT be pushed back onto a user without that background.

### R6. Translate in both directions

The implementation MUST turn an everyday hassle into an executable AI task and turn AI process and decisions back into language a person can control.

### R7. Preserve facts

Simplification MUST NOT change any fact that could alter the decision. Inference must be marked as inference. When an analogy differs from reality, state the boundary if that difference matters to the current decision. A claim that is true only in the current situation MUST be scoped to that situation; words such as “only,” “always,” “all,” or “completely” must not turn a possibility into a fact.

## 6. Additional safety requirements

An implementation MUST clearly surface the following when relevant, rather than hiding them behind simple wording:

- deletion, overwrite, or hard-to-recover data changes;
- payment, subscription, or growing costs;
- access to passwords, accounts, cameras, files, location, or similar resources;
- installing or running an externally supplied tool: check necessity, official source, permission scope, whether it may run temporarily or remain installed, costs, and alternatives; a familiar brand or official source is not sufficient grounds for consent by itself;
- API keys, access tokens, or other secret “keys” that let software use a service as the user; an implementation must not ask the user to paste a real key into a conversation, example, log, or file intended for publication;
- sending user content to a third party or publishing it; state the scope, recipient, retention period, purpose, costs, and whether less data, redacted data, or local processing can work instead;
- uncertainty in legal, medical, financial, or other high-risk decisions; and
- whether an AI action has not run, has failed, or cannot be verified.

### 6.1 User explanation first, verification record second

A complex project may keep two layers:

1. **User explanation:** begin with the result, recommendation, main risk, and next action. This layer must remain complete even if every internal ID, state name, filename, command, hash, and process label is removed.
2. **Verification record:** retain the actions taken, evidence, exact terms, and identifiers so a professional can later check what happened. Technical teams often call this an audit. Every internal state that affects the user should sit next to a sentence explaining what it means for that user.

Putting a “plain-language” heading above a technical summary that still depends on internal labels does not satisfy the protocol. The user MUST NOT need to read the verification record or consult a glossary to understand the explanation above it.

The protocol's own vocabulary is not exempt. Words such as audit, regression, freeze, and deployment must also be replaced with everyday language or immediately explained when shown to a user.

### 6.2 Secret check before publication

Before publishing a project to GitHub or elsewhere, an implementation MUST scan the current files, complete version history, and final release archive for passwords, API keys, access tokens, personal email addresses, and other information that should not become public.

Deleting a secret from the current file is not enough if it entered version history. Publication must stop. Revoke and replace the key at the service first, then clean the history and scan again. Example configuration must use an obvious placeholder such as `YOUR_API_KEY`; real keys belong in private settings that will not be uploaded.

## 7. Expression procedure

A minimal conforming implementation can:

1. identify START, CONTROL, or EXPLAIN;
2. identify the result the user actually cares about and the risk they carry;
3. remove terminology and implementation details that do not change the decision;
4. rebuild the causal explanation in one familiar setting instead of jumping among analogies;
5. restore facts lost during simplification when those facts could change the decision;
6. produce a self-contained user explanation before any verification record;
7. provide the smallest actionable next step; and
8. check unfamiliar-word debt, permission boundaries, uncertainty, and factual consistency.

The output does not need to display these headings mechanically. The structure protects completeness; it does not force every response to look identical.

## 8. Passing criteria

Score each output from 0 to 2 on five dimensions:

- real-life relevance;
- immediate comprehension;
- decision enablement;
- factual fidelity; and
- restraint.

To pass, an output must:

1. score at least 8/10;
2. meet the unfamiliar-word-debt target for its mode; and
3. avoid hard failures: requiring technical prerequisites, distorting a key fact, hiding a material effect, executing without authority, or presenting an inference as fact.

An output fails even at 8/10 if the user needs internal IDs, technical state names, commands, or an appended glossary to decide.

See the [Skill quality rubric](skill/human-legible-ai/references/quality-rubric.en.md) for details.

## 9. Conformance levels

- **HLAI-START:** passes START requirements and tests.
- **HLAI-CONTROL:** passes CONTROL requirements and tests.
- **HLAI-EXPLAIN:** passes EXPLAIN requirements and tests.
- **HLAI-FULL:** passes all three modes without omitting the additional safety requirements.

A conformance claim SHOULD publish the protocol version, evaluation samples, and known failures. A few successful screenshots are not sufficient.

An `HLAI-* conformant` claim may be a self-assessment against the public rules; it does not mean that the project has reviewed or certified the implementation. Only an implementation explicitly reviewed by the project and authorized to use an official mark may claim to be “officially verified” or “officially certified.”

## 10. Open questions in v0.x

- Can unfamiliar terms be detected across populations without relying only on subjective judgment?
- How should familiar analogies change across industries, ages, and cultures?
- How can real-user retelling tests replace models grading other models?
- What additional CONTROL rules are needed in high-risk domains?
- When moving rules between languages, what must remain invariant and what should be localized?

These questions do not prevent use of v0.x, but implementations MUST disclose their assumptions.
