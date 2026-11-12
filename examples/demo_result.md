# Demo Investigation — Synthetic Energy Disagreement

## Scenario

A completed synthetic process cycle contains a cumulative electrical-energy counter and sampled real power for the same equipment. The objective is to determine whether the two independent measurements support the same cycle-energy estimate.

## Agent workflow

1. Select the cycle time range.
2. Query the required telemetry through the read-only adapter.
3. Check point coverage and numeric usability.
4. Calculate cumulative-counter energy from endpoint difference.
5. Integrate sampled power using actual timestamps.
6. Compare the two results.
7. Report the measurement basis and any limitations.

## Example output

```text
OBSERVED
- Counter advanced monotonically during the cycle.
- No counter reset was detected.
- Timestamped power samples were available across the analysis window.

CALCULATED
- Counter energy: 12.48 kWh
- Integrated power: 12.41 kWh
- Difference: -0.56%

INFERRED
- The two independent measurement bases are consistent for this
  synthetic example.

UNKNOWN / BLOCKED
- Equipment efficiency cannot be calculated without an independently
  measured useful-output boundary.
```

## Why this matters

The agent does not choose whichever energy estimate looks preferable and does not invent efficiency from electrical consumption alone. Deterministic tools calculate the quantities; the reasoning layer interprets the evidence and limitations.
