from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from math import isfinite

@dataclass
class Sample:
    ts: datetime
    value: float


def counter_energy(samples: list[Sample]) -> dict:
    """Return endpoint delta and reset evidence for a cumulative energy counter."""
    clean=[s for s in samples if isfinite(float(s.value))]
    if len(clean)<2: return {"status":"blocked","reason":"fewer than two numeric samples"}
    resets=sum(1 for a,b in zip(clean,clean[1:]) if b.value<a.value)
    return {"status":"ok" if resets==0 else "review","start":clean[0].value,"end":clean[-1].value,
            "energy_kwh":clean[-1].value-clean[0].value,"reset_count":resets,
            "start_ts":clean[0].ts.isoformat(),"end_ts":clean[-1].ts.isoformat()}


def integrate_power(samples: list[Sample], unit: str="W") -> dict:
    """Trapezoidal integration using actual elapsed seconds."""
    clean=sorted([s for s in samples if isfinite(float(s.value))], key=lambda s:s.ts)
    if len(clean)<2: return {"status":"blocked","reason":"fewer than two numeric samples"}
    scale=0.001 if unit.upper()=="W" else 1.0 if unit.lower()=="kw" else None
    if scale is None: return {"status":"blocked","reason":"power unit must be W or kW"}
    kwh=0.0
    for a,b in zip(clean,clean[1:]):
        dt=(b.ts-a.ts).total_seconds()
        if dt<=0: continue
        kwh += ((a.value+b.value)/2.0)*scale*dt/3600.0
    return {"status":"ok","energy_kwh":kwh,"sample_count":len(clean),
            "start_ts":clean[0].ts.isoformat(),"end_ts":clean[-1].ts.isoformat()}
