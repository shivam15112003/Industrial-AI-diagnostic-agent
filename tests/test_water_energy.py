from analysis.water_energy import water_enthalpy_kwh,heater_adjusted_decrease

def test_enthalpy_positive(): assert water_enthalpy_kwh(100,50)>0
def test_adjusted(): assert heater_adjusted_decrease(10,7,5)==8
