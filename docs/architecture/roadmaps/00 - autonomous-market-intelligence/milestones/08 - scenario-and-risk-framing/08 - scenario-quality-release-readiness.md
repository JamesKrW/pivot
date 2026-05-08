# 08 - Scenario Quality Release Readiness

## Purpose

Repeat Milestone 08 release readiness after the scenario-quality remediation and keep the milestone blocked until backend tests and live scenario inspection prove BUY and SELL frames meet the reopened acceptance bar.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

blocked

## Owner

Codex / orchestration

## Date Started

2026-05-08

## Date Completed

Blocked 2026-05-08 after live/current scenario inspection failed the scenario-quality bar.

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- `00 - milestone coordination.md`
- `06 - scenario-quality-gap-and-acceptance-reset.md`
- `07 - news-causal-scenario-generation-and-sell-parity.md`

## Likely Files Touched

- docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/08 - scenario-and-risk-framing/*
- backend/ai/*
- frontend/src/views/*
- frontend/src/views/__tests__/*

## Entry Conditions

- scenario-quality acceptance reset exists
- backend generation and frontend display remediation have been implemented
- focused backend tests can run
- live or current scenario data can be inspected

## Background

The corrective round improved scenario wording, SELL parity, AI-output validation, and frontend action-relative labels. Release readiness still cannot be restored because current scenario output still falls back to canned deterministic text instead of producing user-facing LLM-generated, news-causal scenario analysis.

## Detailed Requirements

- run focused backend scenario validation tests
- run affected frontend verification
- inspect current API or persisted scenario output for at least one accepted BUY example and one accepted SELL example
- confirm user-facing scenario language says `trade`, not `paper trade`
- keep Milestone 08 blocked if backend tests or live/current inspection cannot run

## Validation Scenarios

- BUY example shows news event or condition, asset implication, and effect on the submitted trade
- SELL example shows news event or condition, asset implication, and effect on the submitted trade
- SELL with asset-positive evidence is clearly adverse to the submitted SELL trade
- no-news fallback is honest and non-repetitive
- manual trade execution remains non-blocking

## Task Steps

1. Review task 06 acceptance examples and task 07 implementation notes.
2. Run focused backend tests for scenario validation.
3. Run frontend typecheck and affected frontend tests.
4. Inspect current persisted or API scenario output for BUY and SELL examples.
5. Update Milestone 08 coordination and task 05 only after all release-readiness checks pass.

## Tests to Add or Update

- no new tests unless release-readiness inspection finds a missed acceptance gap

## Commands to Run

- `cd backend && pytest ai/test_strategy_validation.py -q`
- `cd backend && ruff check ai/strategy_validation.py ai/test_strategy_validation.py`
- `cd frontend && npm run typecheck`
- `cd frontend && npm run test -- --run src/views/__tests__/TradeNewView.spec.ts`

## Exit Conditions

- focused backend tests pass
- affected frontend verification passes
- current BUY and SELL scenario examples satisfy the reopened action-relative/news-causal acceptance bar
- task 05 can be returned to done
- Milestone 08 can be marked user-releaseable again

## Implementation Notes / What Was Done

- Frontend typecheck passed.
- Affected frontend test passed: `npm run test -- --run src/views/__tests__/TradeNewView.spec.ts` with 6/6 tests passing.
- Python compilation passed for `backend/ai/strategy_validation.py` and `backend/ai/test_strategy_validation.py`.
- Diff whitespace check passed for the touched backend and frontend files.
- Rebuilt the backend image after discovering the running backend container had stale source code and no bind mount.
- Focused backend tests passed in a rebuilt one-off container: `docker compose run --rm backend pytest ai/test_strategy_validation.py -q` with 19/19 tests passing.
- Focused backend ruff passed in a rebuilt one-off container: `docker compose run --rm backend ruff check ai/strategy_validation.py ai/test_strategy_validation.py`.
- Recreated the backend service from the rebuilt image and inspected a fresh PETR4 SELL validation.
- Fresh validation confirmed SELL direction labeling now works, but scenario text is still fallback/canned: only the rationale is LLM-generated and news-aware; scenario frames remain generic and do not explain news event -> asset implication -> effect on the submitted trade.

## Open Follow-Ups

- Diagnose why AI scenario generation calls fail validation or parsing and silently fall back.
- Add observability for AI scenario-generation failures so invalid JSON, validation rejection, and provider failures are visible during UAT.
- Replace fallback-dominant scenario behavior with user-facing LLM-generated, news-causal scenario frames.
- Inspect current persisted or API scenario output for accepted BUY and SELL examples after that fix.
- Only after those checks pass, return task 05 and Milestone 08 to done.
