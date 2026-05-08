# 04 - Advisory and Review Scenario Surfaces

## Purpose

Show scenario frames in the manual advisory flow and recommendation review surfaces while keeping manual trade execution fully non-blocking.

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
- `01 - recommendation-evidence-and-risk-source-scan.md`
- `02 - scenario-frame-contract-and-validation.md`
- `03 - generation-persistence-and-risk-framing.md`

## Likely Files Touched

- frontend/src/api/*
- frontend/src/types/*
- frontend/src/views/*
- frontend/src/components/*
- frontend/src/views/__tests__/*
- frontend/src/components/__tests__/*
- backend/tests/*

## Entry Conditions

- recommendation responses expose validated scenario frames

## Background

Scenario frames are part of the recommendation record. They should be visible immediately after the opt-in advisory result and remain reviewable later. They must not become a hidden gate around the manual trade submit flow.

## Detailed Requirements

- show scenario frames after the opt-in strategy validation result
- show scenario frames in recommendation history or review surfaces
- keep manual trade submit separate from scenario frame loading, generation, and display state
- do not block manual execution on missing, rejected, or unavailable scenario frames
- present base, bull, and bear cases compactly
- keep risk framing visible without creating sizing instructions beyond stored `position_size_guidance`

## Proposed Approach

1. Extend frontend recommendation types to include scenario frames.
2. Reuse the existing manual trade advisory surface.
3. Add a compact scenario frame renderer.
4. Reuse the renderer in the recommendation review list.
5. Add tests for advisory and review rendering plus non-blocking execution.

## Validation Scenarios

- user requests validation and sees scenario frames with the recommendation
- user reviews older recommendations and sees stored scenario frames
- user executes a trade without requesting validation
- user executes a trade after a rejected or missing scenario frame
- scenario frame loading failure does not disable trade submit

## Task Steps

1. Review the requirement and expected behavior.
2. Scan the current advisory and review UI.
3. Implement the smallest reusable scenario display.
4. Add or update regression coverage.
5. Run verification commands.

## Tests to Add or Update

- frontend tests for scenario frame rendering after validation
- frontend tests for scenario frame rendering in recommendation review
- regression tests proving trade submit remains available independent of scenario output

## Commands to Run

- `cd frontend && npm run typecheck`
- run affected frontend tests

## Exit Conditions

- scenario frames appear in manual advisory output
- scenario frames appear in recommendation review output
- missing scenario frames are handled gracefully
- manual execution remains available regardless of scenario state

## Implementation Notes / What Was Done

- Extended frontend recommendation types with scenario frames.
- Rendered compact scenario frames after the opt-in manual trade advisory result.
- Added scenario-case summaries to the previous recommendation review table without coupling manual trade submission to scenario state.
- Updated `TradeNewView` coverage to assert scenario display while preserving separate manual submit behavior.

## Open Follow-Ups

- none
