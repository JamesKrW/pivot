# 05 - Scenario Implementation and Release Readiness

## Purpose

Complete Milestone 08 end to end and close release readiness with deterministic validation tests, UI review coverage, non-blocking manual-trade verification, and explicit handoff notes for later autonomous-gating milestones.

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
- `03 - generation-persistence-and-risk-framing.md`
- `04 - advisory-and-review-scenario-surfaces.md`

## Likely Files Touched

- backend/ai/*
- backend/portfolios/*
- backend/tests/*
- frontend/src/*
- frontend/tests/*
- docs/reference/*

## Entry Conditions

- prior Milestone 08 task files completed or explicitly narrowed

## Background

Milestone 08 should ship as a coherent user-facing extension of strategy validation. This task is responsible for final integration, milestone-wide verification, and explicit notes about any intentionally deferred regeneration or review tooling.

## Detailed Requirements

- implement scenario generation and persistence end to end
- ensure deterministic validation rejects unsupported generated frames
- expose frames in manual advisory and recommendation review surfaces
- preserve manual trade execution regardless of scenario output
- document any intentionally deferred regeneration, operator review, or autonomous-gating work

## Validation Scenarios

- strategy validation creates a recommendation with linked base, bull, and bear frames
- invalid generated frame output is rejected before persistence
- recommendation review shows stored scenario frames
- manual trade submit remains independent of scenario output
- risk framing references approved guardrail and candidate sources only

## Task Steps

1. Review the requirement and expected behavior.
2. Implement the smallest complete Milestone 08 slice.
3. Add or update regression coverage.
4. Run lint, typecheck, and affected tests.
5. Document actual outcome, gaps, and next-step recommendation.

## Tests to Add or Update

- backend scenario-frame persistence tests
- backend deterministic validation tests
- backend integration tests for recommendation plus scenario frames
- frontend advisory and review rendering tests
- regression tests for non-blocking manual trade execution

## Commands to Run

- `cd backend && ruff check .`
- `cd backend && pytest`
- `cd frontend && npm run typecheck`
- run affected frontend tests
- run milestone integration tests covering scenario generation, persistence, review display, and non-blocking execution

## Exit Conditions

- milestone behavior works end to end
- deterministic validation coverage passes
- manual-trade execution remains non-blocking
- release notes and follow-ups are explicit
- milestone remains user-releaseable

## Implementation Notes / What Was Done

Not started.

## Open Follow-Ups

- none
