# 01 - Recommendation Evidence and Risk Source Scan

## Purpose

Identify the smallest correct insertion points for scenario framing so Milestone 08 can reuse stored recommendation evidence, existing guardrails, and current manual-review surfaces without creating a parallel forecasting stack.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

done

## Owner

Codex / implementation

## Date Started

2026-05-07

## Date Completed

2026-05-07

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- `00 - milestone coordination.md`

## Likely Files Touched

- backend/ai/*
- backend/portfolios/*
- backend/tests/*
- frontend/src/api/*
- frontend/src/types/*
- frontend/src/views/*
- frontend/src/components/*

## Entry Conditions

- SPEC-008 approved
- ADR-009 accepted
- milestone coordination reviewed
- Milestone 07 recommendation record contract reviewed

## Background

Scenario framing is only bounded if it consumes the recommendation evidence snapshot from Milestone 07. This task confirms where the stored candidate, technical inputs, context inputs, sentiment trajectory inputs, divergence inputs, and guardrail data already live before any new model or service is introduced.

## Detailed Requirements

- identify the current sources of:
  - `StrategyRecommendation`
  - candidate snapshot
  - technical inputs
  - context inputs
  - sentiment trajectory inputs
  - divergence inputs
  - available cash
  - current position exposure
  - `PortfolioGuardrails`
- identify where scenario generation should attach during validation
- identify existing API serializers and frontend types that should carry scenario frames
- identify existing manual advisory and recommendation review surfaces
- document any missing source that blocks honest risk framing

## Task Steps

1. Review the requirement and expected behavior.
2. Scan Milestone 07 backend validation, models, serializers, and tests.
3. Scan portfolio guardrail and position exposure sources.
4. Scan manual trade advisory and recommendation review frontend surfaces.
5. Map each SPEC-008 input to an existing source or explicit gap.
6. Add or update tests only if code changes are required for the scan outcome.
7. Run verification commands.

## Tests to Add or Update

- none expected unless scan findings require code changes

## Commands to Run

- `cd backend && pytest -q`
- `cd frontend && npm run typecheck`

## Exit Conditions

- scenario generation insertion point is explicit
- evidence reuse points are documented
- guardrail and candidate-fact risk sources are documented
- any blocker is concrete and named

## Implementation Notes / What Was Done

- Confirmed `StrategyRecommendation` in `backend/ai/models.py` stores candidate, technical, context, sentiment trajectory, divergence, verdict, and rationale.
- Confirmed scenario generation belongs immediately after recommendation persistence in `StrategyValidationService.validate`.
- Confirmed risk framing sources: `Portfolio.current_cash`, portfolio market/currency, candidate quantity, quote price, `trading.Position`, and `PortfolioGuardrails`.
- Confirmed existing surfaces: `StrategyRecommendationSerializer`, frontend `StrategyRecommendation` type, `TradeNewView` opt-in advisory result, and previous recommendation table.

## Open Follow-Ups

- none
