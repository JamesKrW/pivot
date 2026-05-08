# 07 - News-Causal Scenario Generation and Sell Parity

## Purpose

Remediate scenario quality so generated and fallback frames use concrete stored news context when available, and render SELL scenarios with action-relative support and adverse evidence.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

blocked

## Owner

Codex / Sub-agent 2

## Date Started

2026-05-07

## Date Completed

Blocked 2026-05-08 pending focused backend pytest.

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- `00 - milestone coordination.md`
- `02 - scenario-frame-contract-and-validation.md`
- `03 - generation-persistence-and-risk-framing.md`
- `05 - scenario-implementation-and-release-readiness.md`

## Likely Files Touched

- backend/ai/strategy_validation.py
- backend/ai/test_strategy_validation.py

## Entry Conditions

- strategy validation persists base, bull, and bear scenario frames
- scenario frame API and database shape remain unchanged

## Background

Milestone 08 scenario frames need to read like causal, user-facing trade guidance. Generic fallback prose and BUY-oriented bull/bear wording can mislead users, especially when validating SELL candidates.

## Detailed Requirements

- replace generic fallback scenario prose with action-relative, news-causal scenario text
- require AI scenario risk notes to use concrete stored news text when context exists
- ensure asset-negative or bear evidence supports SELL candidates
- ensure asset-positive or bull evidence is adverse to SELL candidates
- use `trade` in user-facing language, not `paper trade`
- preserve advisory-only behavior with no schema or API contract changes

## Validation Scenarios

- BUY with positive concrete news produces causal BUY-supportive scenario text
- SELL with negative concrete news produces causal SELL-supportive scenario text
- SELL with asset-bullish news renders the bull case as adverse to SELL
- no-news fallback stays honest without repeating the same missing-news sentence
- malformed or generic AI output is rejected before persistence and falls back predictably

## Task Steps

1. Review existing scenario generation and validation.
2. Keep remediation inside the current backend service and tests.
3. Add deterministic validation for stored-news grounding.
4. Add focused BUY/SELL/no-news regression coverage.
5. Run focused backend verification where available.

## Tests to Add or Update

- backend strategy-validation tests for BUY/news causal support
- backend strategy-validation tests for SELL/news causal support
- backend strategy-validation tests for SELL adverse bull evidence
- backend fallback tests for no-news scenario wording
- deterministic scenario validation tests for generic or malformed AI output

## Commands to Run

- `cd backend && pytest ai/test_strategy_validation.py -q`
- `python3 -m py_compile backend/ai/strategy_validation.py backend/ai/test_strategy_validation.py`

## Exit Conditions

- scenario text is action-relative for BUY and SELL
- scenario risk notes are grounded in stored headlines when available
- generic AI scenario output is rejected before persistence
- no database, serializer, or API shape changes are introduced

## Implementation Notes / What Was Done

- Added deterministic risk-note validation that rejects generic AI scenario prose and requires stored headline overlap when context news exists.
- Reworked fallback scenario wording so bull and bear frames describe whether evidence supports or works against the submitted BUY or SELL candidate.
- Updated prompts and fallback language to say `trade` instead of `paper trade`.
- Added focused regression tests for BUY-positive news, SELL-negative news, SELL-bullish adverse evidence, no-news fallback wording, and generic/malformed AI output rejection.
- Local focused pytest could not run because `pytest` is not installed on PATH and Docker is unavailable; Python compilation and diff whitespace checks passed.

## Open Follow-Ups

- Run focused backend pytest once a backend test runner or Docker daemon is available.
