from __future__ import annotations
from datetime import datetime

def coverage_summary(points: list[dict], expected_interval_s: float|None=None) -> dict:
    numeric=[]
    for p in points:
        try: numeric.append((datetime.fromisoformat(p["ts"]),float(p["value"])))
        except (KeyError,TypeError,ValueError): pass
    numeric.sort()
    gaps=[]
    for (ta,_),(tb,_) in zip(numeric,numeric[1:]): gaps.append((tb-ta).total_seconds())
    out={"point_count":len(points),"numeric_count":len(numeric),"largest_gap_s":max(gaps) if gaps else None}
    if numeric: out.update(first_ts=numeric[0][0].isoformat(),last_ts=numeric[-1][0].isoformat())
    if expected_interval_s and gaps: out["large_gap_count"]=sum(g>2*expected_interval_s for g in gaps)
    return out
