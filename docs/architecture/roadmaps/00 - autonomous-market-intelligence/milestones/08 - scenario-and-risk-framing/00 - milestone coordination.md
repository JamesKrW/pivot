# 00 - Milestone Coordination

## Purpose

Coordinate Milestone 08 execution so strategy recommendations can include bounded scenario and risk framing without granting trade execution or sizing authority.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

in_progress

## Owner

Codex / implementation

## Date Started

2026-05-07

## Date Completed

Reopened 2026-05-07 after UAT/live-example scenario quality failure.

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- SPEC-008 approved
- ADR-009 accepted
- required references:
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/roadmap.md`
  - `docs/architecture/execution/milestone-delivery-execution-model.md`
  - `docs/specs/SPEC-001-open-news-context-expansion.md`
  - `docs/specs/SPEC-002-narrative-continuity-for-asset-context.md`
  - `docs/specs/SPEC-003-context-scope-expansion-asset-portfolio-watchlist.md`
  - `docs/specs/SPEC-004-sentiment-trajectory-and-narrative-state.md`
  - `docs/specs/SPEC-005-divergence-reasoning-for-market-analysis.md`
  - `docs/specs/SPEC-006-opportunity-discovery-pipeline.md`
  - `docs/specs/SPEC-007-strategy-validation-with-technical-and-context-inputs.md`
  - `docs/specs/SPEC-008-scenario-framing-for-strategy-decisions.md`
  - `docs/adrs/ADR-009-bounded-scenario-framing.md`
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/07 - strategy-validation-layer/00 - milestone coordination.md`
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/07 - strategy-validation-layer/01 - candidate-intake-and-analysis-reuse-scan.md`
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/07 - strategy-validation-layer/02 - deterministic-verdict-rules-and-recommendation-record-contract.md`
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/07 - strategy-validation-layer/03 - advisory-manual-trade-ui-and-paper-review-surface.md`
  - `docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/07 - strategy-validation-layer/04 - validation-implementation-and-release-readiness.md`

## Likely Files Touched

- docs/architecture/roadmaps/00 - autonomous-market-intelligence/milestones/08 - scenario-and-risk-framing/*
- backend/ai/*
- backend/portfolios/*
- backend/tests/*
- frontend/src/api/*
- frontend/src/types/*
- frontend/src/views/*
- frontend/src/components/*
- frontend/src/views/__tests__/*
- frontend/src/components/__tests__/*

## Entry Conditions

- roadmap reviewed
- milestone delivery execution model reviewed
- SPEC-008 reviewed
- ADR-009 reviewed
- Milestone 07 task files reviewed and adopted as working constraints
- no open SPEC-008 decisions remain

## Task Steps

1. Read the roadmap, execution model, SPEC-008, ADR-009, and Milestone 07 required references before implementation.
2. Execute Milestone 08 task files in order.
3. Keep scenario framing attached to explicit strategy recommendations.
4. Generate initial scenario frames during strategy validation so they share the recommendation evidence snapshot.
5. Persist scenario frames as separate records linked to `StrategyRecommendation`.
6. Keep scenario cases capped to `base`, `bull`, and `bear`.
7. Keep confidence bands capped to `low`, `medium`, and `high`.
8. Allow AI to generate structured scenario frames only from stored recommendation evidence.
9. Validate AI-generated frames deterministically before persistence.
10. Use existing guardrails and candidate facts for risk framing.
11. Keep scenario output advisory, paper-only, and non-blocking.
12. Surface scenario frames in manual advisory and recommendation review flows.
13. Execute task 06 to reset acceptance around scenario quality gaps and action-relative examples.
14. Execute task 07 to remediate generation and validation until frames are action-relative and news-causal.
15. Execute task 08 to repeat release readiness with live BUY and SELL examples.
16. Make final handoff explicit about:
    - whether scenario frames persist end to end
    - whether deterministic validation rejects unsupported frames
    - whether manual trade execution remains non-blocking
    - whether future regeneration history was implemented or intentionally deferred

## Tests to Add or Update

- backend model and serializer tests for scenario frame records
- backend tests for scenario generation during validation
- deterministic validation tests for invalid labels, missing fields, unsupported catalysts, and scenario cap
- regression tests proving trade execution remains non-blocking
- frontend tests for scenario display in manual advisory and recommendation review surfaces

## Commands to Run

- `cd backend && ruff check .`
- `cd backend && pytest`
- `cd frontend && npm run typecheck`
- run affected frontend tests
- run milestone integration tests covering validation, scenario persistence, review display, and non-blocking execution

## Exit Conditions

- scenario frames are generated from recommendation evidence during validation
- scenario frames are persisted as linked records
- deterministic validation enforces labels, caps, evidence boundaries, and required risk fields
- manual advisory and recommendation review surfaces show scenario frames
- manual trade execution remains non-blocking
- milestone remains user-releaseable

## Reopened Gap

UAT/live examples showed the implementation met the deterministic structure but not the acceptance quality bar. Scenario frames were too generic and similar across cases, biased toward BUY-shaped framing, weak for SELL candidates, weak at explaining news causality, and too often dominated by fallback/template language.

## Release Criteria Addendum

- At least one accepted BUY example must show an explicit news event or condition, its market or asset implication, and its effect on the submitted trade.
- At least one accepted SELL example must show an explicit news event or condition, its market or asset implication, and its effect on the submitted trade.
- Scenario frames must be action-relative: favorable and adverse cases must be interpreted relative to the submitted BUY or SELL action, not as generic asset forecasts.
- Scenario frames must be news-causal when news context exists: event or condition -> market/asset implication -> effect on submitted BUY/SELL trade.

## Implementation Notes / What Was Done

- Executed Milestone 08 task files in order.
- Scenario frames now persist end to end as linked `StrategyScenarioFrame` records on recommendations.
- Deterministic validation rejects invalid labels, unsupported evidence sources, missing risk fields, scenario cap violations, and new trade idea payloads before persistence.
- Manual trade execution remains non-blocking; scenario generation/display is advisory only.
- Future regeneration history was intentionally deferred.
- Reopened Milestone 08 for docs-only acceptance reset after UAT/live examples exposed scenario quality gaps.

## Open Follow-Ups

- Full backend lint, full frontend lint, and full frontend unit tests have unrelated existing baseline failures documented in task 05.
- Compose watch ignores backend migrations, so the new migration was copied into the running backend container for verification.
- Tasks 06, 07, and 08 must close the scenario quality gap before release readiness can be restored.
