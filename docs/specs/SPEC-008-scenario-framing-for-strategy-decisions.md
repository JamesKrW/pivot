---
name: Scenario Framing for Strategy Decisions
description: Spec for bounded scenario and risk framing attached to paper-only strategy recommendations
type: reference
---

# SPEC

## SPEC-008 Scenario Framing for Strategy Decisions

Status: Approved
Governing ADR: [ADR-009-bounded-scenario-framing](../adrs/ADR-009-bounded-scenario-framing.md)

## Roadmap Position

This SPEC corresponds to Milestone 8 of the Autonomous Market Intelligence roadmap:

- [Autonomous Market Intelligence Roadmap](../roadmaps/00%20-%20autonomous-market-intelligence/roadmap.md)

Its role is narrow: attach bounded near-term scenarios, catalysts, uncertainty, and risk framing to existing paper-only strategy recommendations.

It is not intended to execute trades, create an unconstrained prediction engine, or grant portfolio-management authority to AI.

## Context

SPEC-001 broadens asset context. SPEC-002 adds bounded continuity. SPEC-003 generalizes analysis to monitored sets. SPEC-004 adds short-window sentiment trajectory. SPEC-005 explains expected-vs-actual divergence. SPEC-006 surfaces watch candidates. SPEC-007 validates explicit trade candidates and persists paper-only recommendation records.

That still leaves a gap: a recommendation can approve, reject, or defer a trade idea, but it does not yet show the bounded forward-looking frame a user needs before deciding how much confidence to place in that recommendation.

Users eventually need answers such as:

- what concrete catalyst would make this recommendation work
- what condition would invalidate it
- what downside or uncertainty should affect paper position size
- whether the scenario is clean, conditional, or too conflicted to act on

Without scenario framing, recommendations are auditable but not yet transparent enough about uncertainty and risk.

## Decision

Milestone 8 should add a bounded scenario-framing layer to the strategy-validation output.

That layer should:

1. consume an existing explicit strategy candidate and its stored recommendation evidence
2. produce a small set of near-term scenarios tied to concrete catalysts or invalidating conditions
3. attach confidence or probability bands without pretending precision
4. frame risk in terms of existing paper position-sizing constraints
5. persist scenario framing alongside, or directly linked to, the paper-only recommendation record

Scenario framing should remain advisory. It should not authorize execution, block manual execution, alter a portfolio, or generate new trade ideas by itself.

The first consumer should be:

1. paper-strategy review and manual trade advisory surfaces

Future milestones may reuse the same framing contract later for:

1. fact-conflict and correction checks
2. autonomous execution gating
3. post-trade review and learning workflows

## Intended Shape

The future implementation should treat scenario framing as a bounded extension of strategy validation, not as a separate analyst or forecasting stack.

Expected flow:

1. receive an explicit strategy candidate
2. run or load the corresponding strategy-validation recommendation
3. read the recommendation's stored technical, context, sentiment trajectory, and divergence inputs
4. derive a capped scenario frame from those stored inputs
5. emit structured scenario fields
6. persist the scenario frame with the recommendation
7. render concise scenario and risk framing wherever the recommendation is reviewed

The scenario output should stay compact and reviewable. It should not require storing a free-form reasoning transcript as the system of record.

Recommended minimum structured fields:

- `recommendation_id`
- `scenario_case`
- `direction`
- `catalysts`
- `invalidating_conditions`
- `confidence_band`
- `risk_notes`
- `position_size_guidance`
- `generated_at`

Allowed `scenario_case` values should stay small. A first implementation may use:

- `base`
- `bull`
- `bear`

Allowed `confidence_band` values should be coarse. A first implementation may use:

- `low`
- `medium`
- `high`

## Resolved Decisions

### Scenario Framing Requires a Governing ADR

Milestone 8 introduces a reusable contract between strategy validation, later fact-conflict checks, and autonomous gating. The decision boundary should be captured in an ADR because scenario frames must stay advisory, structured, bounded, and non-executing.

### Scenario Frames Should Be Separate Linked Records

Scenario frames should be persisted as separate records linked to `StrategyRecommendation`, not as loose fields directly on the recommendation.

Recommended model shape:

- `StrategyScenarioFrame`
- `recommendation`
- `scenario_case`
- `direction`
- `catalysts`
- `invalidating_conditions`
- `confidence_band`
- `risk_notes`
- `position_size_guidance`
- `generated_at`

Reason:

- `StrategyRecommendation` remains the canonical verdict and evidence record from Milestone 7
- scenario framing can evolve independently
- regeneration and review history remain easier to audit
- future fact-conflict and autonomous-gating workflows can reference frames without mutating the original recommendation

### Scenario Frames Are Generated During Strategy Validation

Scenario frames should be generated during strategy validation so they belong to the same evidence snapshot as the recommendation verdict.

Allowed later:

- explicit regeneration may create a new scenario frame linked to the same recommendation
- regeneration must not overwrite the original frame

Reason:

- generating later could use drifted context that no longer matches the stored verdict evidence
- keeping the first frame tied to validation preserves auditability

### Scenario Taxonomy Starts With Base, Bull, and Bear

Milestone 8 should use exactly these scenario cases:

- `base`
- `bull`
- `bear`

Meaning:

- `base`: most likely near-term path from the stored evidence
- `bull`: asset-favorable upside path
- `bear`: asset-negative downside path

These are trade-scenario frames, not pure asset forecasts. A `bull` case supports a `BUY` candidate but is adverse to a `SELL` candidate. A `bear` case supports a `SELL` candidate but is adverse to a `BUY` candidate.

Future refinements may add more scenario types if review evidence shows a real need.

### Confidence Bands Stay Coarse

Milestone 8 should use exactly these confidence bands:

- `low`
- `medium`
- `high`

Numeric probabilities are not approved in this milestone.

Reason:

- numeric odds imply precision the system does not have
- coarse bands are easier to audit from bounded evidence
- calibrated probability bands should wait until review data exists

### Risk Framing Uses Existing Guardrails and Candidate Facts

Risk framing should use existing portfolio guardrails and candidate facts only.

Approved inputs:

- available cash
- portfolio market
- candidate quantity
- quote price
- existing position exposure when available
- existing `PortfolioGuardrails` constraints

Not approved:

- new scenario-specific sizing rules
- AI-generated sizing authority
- hidden allocation logic

Reason:

- scenario framing can describe whether a candidate looks oversized, constrained, or cleaner under current paper limits
- it must not decide portfolio allocation or create autonomous sizing logic

### Scenario Count Is Capped at Three

Each recommendation may have at most three scenario frames:

- one `base`
- one `bull`
- one `bear`

Frames may be omitted when evidence is insufficient, but additional cases are not approved in this milestone.

### AI Generates Structured Frames Under Deterministic Validation

AI may generate structured scenario frames, not just prose, but only from stored recommendation evidence.

Deterministic validation must reject frames that:

- use unsupported catalysts
- use invalid labels
- omit required risk fields
- exceed the scenario cap
- create new trade ideas
- override safety rules

Reason:

- AI should perform useful analytical work from bounded evidence
- deterministic validation preserves the audit boundary
- safety and execution authority remain outside the AI-generated frame

### Scenario Frames Appear in Manual Advisory and Review Surfaces

Milestone 8 should expose scenario frames in both:

- the manual trade advisory flow after the opt-in validation result
- recommendation history or review surfaces for the portfolio

Reason:

- scenarios are part of the recommendation record
- transient-only display would lose audit and review value

### Acceptance Clarification: Scenario Quality Is Action-Relative and News-Causal

Passing deterministic structure is not enough for acceptance. A releaseable scenario frame must explain the causal chain from available evidence to the submitted action:

`news event or condition -> market/asset implication -> effect on submitted BUY/SELL trade`

Accepted examples must show how the same evidence can be favorable or adverse relative to the submitted action. A scenario for a SELL candidate must not read like a BUY recommendation with labels inverted, and a scenario for a BUY candidate must not ignore news that weakens the trade.

## Constraints

- Scenario framing must consume explicit candidate and recommendation evidence; it must not invent trades.
- Scenario framing must remain paper-only and advisory.
- Scenario framing must reuse stored strategy-validation inputs where possible.
- AI-generated scenario output must be deterministically validated before persistence.
- Scenario count must be capped at three frames per recommendation.
- Confidence or probability framing must be coarse and auditable from inputs.
- Risk framing must reference existing paper position-sizing constraints instead of creating autonomous sizing authority.
- Manual trade execution must remain non-blocking regardless of scenario output.

## Non-Goals

- Live autonomous trade execution
- Automatic order placement
- Free-form market prediction
- AI-managed portfolio allocation
- Hidden or non-auditable confidence scores
- New strategy generation from scenario prose
- Long-horizon macro forecasting

## Notes

This SPEC should remain independently mergeable and user-releaseable when implemented.

Expected user-facing value:

- users can review trade recommendations with explicit catalysts, scenario boundaries, uncertainty, and risk framing before deciding whether to act.
