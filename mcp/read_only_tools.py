from __future__ import annotations
from datetime import datetime
from pathlib import Path
from mcp.server.mcpserver import MCPServer
from adapters.sample_provider import SampleTelemetryProvider
from analysis.energy import Sample,counter_energy,integrate_power
from analysis.quality import coverage_summary

server=MCPServer(name='industrial-ai-demo',title='Industrial AI Demo',description='Read-only tools over synthetic telemetry.')
DATA=Path(__file__).resolve().parents[1]/'examples'/'sample_telemetry.csv'
provider=SampleTelemetryProvider(DATA)

@server.tool()
def list_tags()->dict:
    return {'mode':'read_only','tags':provider.tags()}

@server.tool()
def summarize_range(tags:list[str],start:str,end:str)->dict:
    s,e=datetime.fromisoformat(start),datetime.fromisoformat(end)
    raw=provider.query(tags,s,e)
    return {'mode':'read_only','summary':{t:coverage_summary(v) for t,v in raw.items()}}

@server.tool()
def analyze_electrical_energy(counter_tag:str,power_tag:str,start:str,end:str,power_unit:str='W')->dict:
    s,e=datetime.fromisoformat(start),datetime.fromisoformat(end)
    raw=provider.query([counter_tag,power_tag],s,e)
    def smp(tag): return [Sample(datetime.fromisoformat(p['ts']),float(p['value'])) for p in raw[tag] if isinstance(p['value'],(int,float))]
    return {'mode':'read_only','counter':counter_energy(smp(counter_tag)),'integrated_power':integrate_power(smp(power_tag),power_unit)}

if __name__=='__main__': server.run(transport='stdio')
