# Project Overview for Reviewers

## Problem

Industrial telemetry investigations combine noisy sensors, sparse events, counters, process states, and incomplete metadata. A language model can help organize the investigation, but engineering calculations and safety boundaries should not depend on unconstrained natural-language reasoning.

## Approach

This project separates responsibilities:

- **Agent layer:** chooses read-only evidence tools and synthesizes findings.
- **Tool layer:** exposes bounded observations and compact summaries.
- **Analysis layer:** performs deterministic numerical calculations.
- **Adapter layer:** isolates the data source from the reasoning system.
- **Safety layer:** omits control/write operations from the public tool surface.

## Engineering decisions

### Deterministic math outside the LLM

Energy integration and water-energy calculations are Python functions that can be unit-tested. This avoids asking the language model to perform long numerical integrations from raw telemetry.

### Compact evidence

Large time-series windows are summarized before being returned to the reasoning layer. This reduces context pressure and makes evidence easier to audit.

### Missing is not zero

Unavailable or non-numeric measurements remain unavailable. They are not silently converted into physical zeros.

### Independent measurement comparison

Where a cumulative counter and sampled power both exist, the system calculates both and reports disagreement rather than averaging them.

### Safety is structural

The public tool facade contains no actuator/write methods. The AI therefore cannot gain control capability simply by being prompted differently.

## Skills demonstrated

- Python software architecture
- agent/tool orchestration
- MCP-style interfaces
- time-series processing
- numerical integration
- data-quality reasoning
- engineering-energy calculations
- safety-conscious AI design
- unit testing and CI
