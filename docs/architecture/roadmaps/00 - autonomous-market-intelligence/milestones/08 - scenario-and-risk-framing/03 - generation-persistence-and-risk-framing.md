# 03 - Generation, Persistence, and Risk Framing

## Purpose

Implement scenario generation during strategy validation, persist linked scenario frames, and derive risk framing from existing guardrails and candidate facts only.

## Roadmap Milestone

Milestone 08 - Scenario and Risk Framing

## Governing SPEC

SPEC-008 Scenario Framing for Strategy Decisions

## Status

planned

## Owner

unassigned

## Date Started

YYYY-MM-DD

## Date Completed

YYYY-MM-DD

## Branch

feat/autonomous/08-scenario-risk

## Dependencies

- `00 - milestone coordination.md`
- `01 - recommendation-evidence-and-risk-source-scan.md`
- `02 - scenario-frame-contract-and-validation.md`

## Likely Files Touched

- backend/ai/*
- backend/portfolios/*
- backend/tests/*

## Entry Conditions

- scenario frame contract and validation boundary defined

## Background

Scenario frames should belong to the same evidence snapshot as the recommendation verdict. They should be generated during validation, stored separately, and risk-framed from current paper constraints without introducing new sizing authority.

## Detailed Requirements

- create linked scenario frame persistence for recommendations
- generate initial scenario frames during strategy validation
- keep original frames immutable after creation
- allow future explicit regeneration only as a new frame set if implemented
- derive risk framing only from:
  - available cash
  - portfolio market
  - candidate quantity
  - quote price
  - existing position exposure when available
  - existing `PortfolioGuardrails` constraints
- do not add new autonomous allocation or sizing rules
- keep validation fallback behavior explicit when AI credentials or budget are unavailable

## Proposed Approach

1. Add the linked scenario frame storage model and serializer shape.
2. Extend strategy validation to request structured scenario frames from stored evidence.
3. Validate generated frames before persistence.
4. Persist validated frames linked to the created recommendation.
5. Return frames with recommendation responses.
6. Preserve recommendation creation if scenario generation is unavailable, using an explicit empty or fallback frame behavior defined during implementation.

## Validation Scenarios

- recommendation validation creates linked scenario frames
- no more than one base, one bull, and one bear frame persists for a recommendation
- risk framing reflects existing guardrails and candidate facts
- malformed AI frame output is rejected without granting execution authority
- validation remains paper-only and does not place trades
- recommendation creation behavior is explicit when scenario generation is unavailable

## Task Steps

1. Review the requirement and expected behavior.
2. Implement linked scenario frame persistence.
3. Integrate scenario generation into strategy validation.
4. Add deterministic validation before persistence.
5. Add or update backend tests.
6. Run verification commands.

## Tests to Add or Update

- backend model and migration tests where applicable
- scenario generation and persistence tests
- risk-framing source tests
- malformed AI-output rejection tests
- regression tests proving no trade execution side effect

## Commands to Run

- `cd backend && ruff check .`
- `cd backend && pytest`

## Exit Conditions

- scenario frames persist as linked recommendation records
- scenario generation runs during validation
- risk framing uses approved sources only
- malformed generated output cannot persist
- execution boundary remains closed

## Implementation Notes / What Was Done

Not started.

## Open Follow-Ups

- none
