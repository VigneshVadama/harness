# Communication Law

Three layers. Pick the layer by audience, not by mood. Code, commands, paths, IDs, secret references, commit-type keywords, and error strings stay EXACT at every layer. Compression never touches them.

## Layer 1 — agent to agent

Applies to: mission files, worker results, validator results, handoffs, status lines between agents.

Write compressed. All technical substance stays. Only fluff dies.

- Drop articles (a/an/the), filler (just/really/basically/actually/simply), pleasantries, and hedging.
- Fragments are fine. Short synonyms win: big not extensive, fix not "implement a solution for".
- Standard acronyms are fine (DB/API/HTTP). MUST NOT invent abbreviations (cfg/impl/req/res/fn) — tokenizers split them the same as the full word: zero tokens saved, clarity lost.
- MUST NOT use causal arrows (→) in prose. Own token, saves nothing.
- No tool-call narration. No decorative tables or emoji. Quote the shortest decisive line of an error, never the full log.
- State each fact once.
- Pattern: `[thing] [action] [reason]. [next step].`

## Layer 2 — human-facing

Applies to: chat replies, progress reports, final summaries a person reads.

Shape output so the reader can act on it, not just read it. Adapted from `i-have-adhd` by Ayoub Ghriss (MIT).

- Lead with the next action or the outcome. Not context, not a plan.
- Number multi-step work. One bounded action per step.
- End with one concrete next action doable in under two minutes.
- Finish the current issue before naming a second one. Offer tangents separately.
- Restate state every turn: "Step 3 of 5 done. Next: X."
- Give concrete time estimates. "About 15 minutes", never "some work".
- Make wins visible: state what now works and how to try it.
- Errors are matter-of-fact: cause, then fix. No "Uh oh".
- Cap lists at 5 items. Split "do now" from "later" past that.
- No preamble, no recap, no closing pleasantries.

## Layer 3 — durable artifacts

Applies to: docs, READMEs, ADRs, PR bodies, issue bodies, commit bodies, skill and agent files.

Write ASD-STE100-derived controlled technical English:

- One instruction per sentence.
- Procedural sentences MUST stay at or under 20 words.
- Active voice. Present tense. Verb-first numbered steps.
- One term = one meaning across the whole document set.
- No noun clusters over 3 words.
- Warnings come before the instructions they guard.
- Normative statements use RFC 2119 keywords, capitalized: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY.

## Auto-clarity override

Drop compression and write plain full sentences for:

- Security warnings.
- Irreversible-action confirmations.
- Multi-step sequences where fragment order or omitted conjunctions risk misreading.
- Any case where compression itself creates ambiguity.

Resume the layer style after the clear part is done. Clarity beats compression. Every time.
