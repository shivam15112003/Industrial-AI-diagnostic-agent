# Architecture

The public implementation separates probabilistic reasoning from deterministic calculations.

1. The agent interprets the operator's question and selects read-only tools.
2. The telemetry adapter returns observations; the demo adapter reads only local synthetic CSV data.
3. Deterministic Python modules perform integration, counter deltas, coverage checks, and thermodynamic calculations.
4. The agent correlates compact results and labels observations, inferences, unknowns, and blocked calculations.
5. Report/plot layers can persist derived artifacts without changing the source telemetry.

Production connectors are intentionally not included in this public repository.
