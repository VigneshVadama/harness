# Communication Law

Pick the layer by audience. Code, commands, paths, IDs, secret refs, commit-type keywords, error strings: EXACT at every layer. Compression never touches them.

## Layer 1 — agent to agent

Mission files, results, handoffs, status lines.

- Drop articles, filler (just/really/basically), pleasantries, hedging. Fragments fine. Short synonyms: big not extensive, fix not "implement a solution for".
- Standard acronyms fine (DB/API/HTTP). MUST NOT invent abbreviations (cfg/impl/req) — tokenizers split them like the full word: zero saved, clarity lost. No causal arrows (→): own token, saves nothing.
- No tool-call narration, decorative tables, emoji. Quote the shortest decisive error line, never the full log. State each fact once.
- Pattern: `[thing] [action] [reason]. [next step].`

## Layer 2 — human-facing

Chat, reports, summaries. Adapted from `i-have-adhd` by Ayoub Ghriss (MIT).

- Lead with the next action or outcome. Number multi-step work. End with one action doable in two minutes.
- Finish the current issue before naming another. Restate state each turn: "step 3 of 5 done".
- Concrete time estimates. Wins visible. Errors matter-of-fact: cause, then fix. Lists cap at 5.
- No preamble, no recap, no closing pleasantries.

## Layer 3 — durable artifacts

Docs, READMEs, ADRs, PR and issue bodies, commit bodies, skill and agent files. ASD-STE100-derived:

- One instruction per sentence. Procedural sentences stay at or under 20 words. Active voice, present tense, verb-first steps.
- One term = one meaning. No noun clusters over 3 words. Warnings before the instructions they guard.
- Normative statements use capitalized RFC 2119 keywords.

## Auto-clarity override

Write plain full sentences for: security warnings, irreversible-action confirmations, sequences where fragment order risks misreading, any ambiguity created by compression. Resume the layer style after. Clarity beats compression.
