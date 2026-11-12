from __future__ import annotations
import csv
from pathlib import Path
from datetime import datetime

class SampleTelemetryProvider:
    """Read-only provider backed by a local CSV. No network/control access."""
    def __init__(self, path: str|Path): self.path=Path(path)
    def tags(self):
        with self.path.open(newline='',encoding='utf-8') as f: return sorted({r['tag'] for r in csv.DictReader(f)})
    def query(self,tags:list[str],start:datetime,end:datetime):
        wanted=set(tags); out={t:[] for t in tags}
        with self.path.open(newline='',encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if r['tag'] not in wanted: continue
                ts=datetime.fromisoformat(r['timestamp'])
                if start<=ts<=end:
                    try:v=float(r['value'])
                    except ValueError:v=r['value']
                    out[r['tag']].append({'ts':ts.isoformat(),'value':v,'quality':r.get('quality') or None})
        return out
