# 06 - Scenario Quality Gap and Acceptance Reset

## Purpose

Reset Milestone 08 acceptance after UAT/live examples showed that structurally valid scenario frames were not good enough for release.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

done

## Owner

Codex / Sub-agent 1

## Date Started

2026-05-07

## Date Completed

2026-05-07

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- `00 - milestone coordination.md`
- `05 - scenario-implementation-and-release-readiness.md`
- `docs/specs/SPEC-008-scenario-framing-for-strategy-decisions.md`
- `docs/adrs/ADR-009-bounded-scenario-framing.md`

## Background

Milestone 08 implementation proved scenario persistence, deterministic validation, and display, but UAT/live examples exposed a quality gap. Release readiness now requires scenario frames that are action-relative and news-causal, not merely valid records.

## Observed Bad Examples

- Generic sameness: base, bull, and bear frames repeated the same high-level language with only labels changed.
- BUY-shaped framing: frames tended to describe asset upside even when the submitted candidate was SELL.
- Weak SELL behavior: SELL scenarios did not clearly explain why negative evidence supports selling or why positive evidence invalidates selling.
- Weak news causality: news appeared as a named catalyst without connecting event or condition to market/asset implication to trade effect.
- Fallback/template dominance: output often read like fallback copy instead of evidence-specific scenario analysis.

## Acceptance Reset

Accepted scenario frames must satisfy this causal chain when news or event context exists:

`news event or condition -> market/asset implication -> effect on submitted BUY/SELL trade`

Accepted scenario frames must also be action-relative:

- For a BUY candidate, favorable cases explain why evidence supports buying; adverse cases explain what would make buying unattractive.
- For a SELL candidate, favorable cases explain why evidence supports selling; adverse cases explain what would make selling unattractive.
- Bull and bear labels describe asset direction, but usefulness must be interpreted against the submitted action.

## Accepted BUY Example

Candidate: BUY PETR4.

Base:

- News event or condition: oil prices remain firm after geopolitical tension disrupts expected supply.
- Market/asset implication: higher crude prices support Petrobras revenue expectations and improve near-term sentiment for PETR4.
- Effect on submitted BUY trade: the BUY trade has a clearer catalyst, but position sizing should stay moderate if volatility is elevated.

Bull:

- News event or condition: geopolitical risk persists while crude inventories tighten.
- Market/asset implication: oil-linked equities gain support as investors price stronger cash flow.
- Effect on submitted BUY trade: the BUY trade becomes more attractive if price confirms strength without breaching guardrails.

Bear:

- News event or condition: diplomatic de-escalation lowers oil prices or local policy news pressures Petrobras margins.
- Market/asset implication: PETR4 loses the catalyst that supported the trade.
- Effect on submitted BUY trade: the BUY trade should be treated as weaker or deferred because the evidence no longer supports upside.

## Accepted SELL Example

Candidate: SELL PETR4.

Base:

- News event or condition: oil prices soften after geopolitical risk eases.
- Market/asset implication: weaker crude prices reduce near-term support for Petrobras sentiment and expected cash flow.
- Effect on submitted SELL trade: the SELL trade has a direct catalyst, assuming the submitted quantity stays within guardrails.

Bull:

- News event or condition: oil rebounds because supply disruption risk returns.
- Market/asset implication: PETR4 may strengthen despite the submitted SELL candidate.
- Effect on submitted SELL trade: the SELL trade becomes less attractive or should be deferred because asset-favorable evidence works against selling.

Bear:

- News event or condition: oil continues falling and domestic policy headlines add pressure.
- Market/asset implication: Petrobras faces weaker sentiment from both commodity and local-risk channels.
- Effect on submitted SELL trade: the SELL trade is more strongly supported, with risk notes focused on rebound risk and position exposure.

## Release Criteria For Tasks 07 and 08

- Task 07 must adjust generation and validation so fallback/template language cannot dominate accepted examples.
- Task 07 must verify SELL candidates are not framed as inverted BUY candidates.
- Task 07 must preserve advisory/non-executing boundaries.
- Task 08 must include at least one accepted BUY example and one accepted SELL example using the causal chain above.
- Task 08 must not mark release readiness done until live examples satisfy action-relative and news-causal acceptance.

## Implementation Notes / What Was Done

- Reopened Milestone 08 acceptance around scenario quality instead of deterministic structure alone.
- Documented the observed UAT/live-example failures.
- Added accepted BUY and SELL examples, including PETR4 oil/geopolitical causal scenarios.
- Pointed follow-up remediation and release readiness to tasks 07 and 08.
