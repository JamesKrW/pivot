# 02 - Scenario Frame Contract and Validation

## Purpose

Define the canonical Milestone 08 scenario-frame contract so AI-generated frames remain structured, bounded, validated, and subordinate to the stored recommendation evidence.

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

## Likely Files Touched

- backend/ai/*
- backend/tests/*
- docs/reference/*

## Entry Conditions

- recommendation evidence and risk source scan complete

## Background

Milestone 08 intentionally lets AI do analytical work by generating structured scenario frames. The deterministic boundary must reject unsupported or malformed frames before persistence so the output remains auditable and cannot drift into new trade generation or hidden safety decisions.

## Detailed Requirements

- define the linked scenario frame record contract:
  - `recommendation`
  - `scenario_case`
  - `direction`
  - `catalysts`
  - `invalidating_conditions`
  - `confidence_band`
  - `risk_notes`
  - `position_size_guidance`
  - `generated_at`
- keep scenario cases limited to:
  - `base`
  - `bull`
  - `bear`
- keep confidence bands limited to:
  - `low`
  - `medium`
  - `high`
- cap frames at three per recommendation
- require catalysts and invalidating conditions to reference stored evidence or explicit candidate facts
- reject frames that:
  - use unsupported catalysts
  - use invalid labels
  - omit required risk fields
  - exceed the scenario cap
  - create new trade ideas
  - override safety rules

## Proposed Approach

1. Normalize AI output into a compact internal frame payload.
2. Validate enum values and required fields.
3. Validate frame count and per-case uniqueness.
4. Validate evidence references against the stored recommendation payload.
5. Persist only validated frames.

## Validation Scenarios

- valid base, bull, and bear frame set persists
- invalid scenario case is rejected
- invalid confidence band is rejected
- more than three frames is rejected
- frame with unsupported catalyst is rejected
- frame missing risk notes or position-size guidance is rejected
- frame that creates a new trade idea is rejected

## Task Steps

1. Review the requirement and expected behavior.
2. Define or confirm the canonical scenario frame payload.
3. Implement the smallest validation boundary.
4. Add fixture-driven regression tests.
5. Run verification commands.

## Tests to Add or Update

- scenario frame validation tests
- persistence contract tests
- regression tests for invalid labels, missing fields, unsupported catalysts, and cap violations

## Commands to Run

- `cd backend && ruff check .`
- `cd backend && pytest`

## Exit Conditions

- scenario frame contract is canonical
- deterministic validation rejects malformed or unsupported frames
- structured fields remain the source of truth
- tests cover accepted and rejected frame payloads

## Implementation Notes / What Was Done

- Added linked `StrategyScenarioFrame` records with base/bull/bear cases, coarse confidence bands, catalyst and invalidation lists, risk notes, position-size guidance, and generated timestamp.
- Added deterministic `validate_scenario_frame_payloads` boundary for case labels, confidence labels, case cap, required risk fields, supported evidence sources, and new-trade-idea rejection.
- Added regression tests for valid payloads, invalid labels, missing risk fields, unsupported catalysts, cap violations, and new trade idea attempts.

## Open Follow-Ups

- none
