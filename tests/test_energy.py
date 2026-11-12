from datetime import datetime,timedelta
from analysis.energy import Sample,counter_energy,integrate_power

def test_counter_delta():
    t=datetime(2026,1,1); r=counter_energy([Sample(t,10),Sample(t+timedelta(hours=1),12.5)])
    assert r['energy_kwh']==2.5 and r['reset_count']==0

def test_power_integration():
    t=datetime(2026,1,1); r=integrate_power([Sample(t,1000),Sample(t+timedelta(hours=1),1000)],'W')
    assert abs(r['energy_kwh']-1.0)<1e-9
