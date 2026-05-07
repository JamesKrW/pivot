---
name: Bounded Scenario Framing
description: AI-generated structured scenario frames linked to paper-only recommendations under deterministic validation
type: reference
---

# ADR-009: Bounded Scenario Framing With Closed Execution Boundary

Status: Accepted
Date: 2026-05-07
SPEC: [SPEC-008-scenario-framing-for-strategy-decisions](../specs/SPEC-008-scenario-framing-for-strategy-decisions.md)

## Context

Strategy validation can approve, reject, or defer explicit paper-trade candidates, but it does not yet explain near-term catalysts, invalidating conditions, or risk framing. Without a bounded contract, scenario work could drift into unauditable forecasting or hidden portfolio management.

## Decision

Add AI-generated structured scenario frames linked to paper-only recommendation records. Frames must be generated from stored recommendation evidence, capped to `base`, `bull`, and `bear` cases, validated deterministically before persistence, and kept separate from execution authority.

## Consequences

- Scenario framing becomes auditable and reviewable alongside the recommendation
- AI contributes real analytical structure while deterministic validation enforces labels, caps, evidence boundaries, and required risk fields
- Separate scenario records preserve the Milestone 7 recommendation snapshot and allow future regeneration history
- Autonomous execution and position sizing remain governed by explicit safety rules, not scenario prose
