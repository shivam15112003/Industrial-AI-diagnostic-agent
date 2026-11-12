from __future__ import annotations

# Simple liquid-water approximations for demonstration. Replace with validated
# property correlations for production engineering work.
def water_density_kg_per_l(temp_c: float) -> float:
    return max(0.95, 0.99984 - 0.00030 * max(0.0, temp_c - 4.0))

def water_enthalpy_kwh(volume_l: float, temp_c: float, reference_c: float=0.0, cp_kj_kgk: float=4.186) -> float:
    mass_kg=water_density_kg_per_l(temp_c)*volume_l
    return mass_kg*cp_kj_kgk*(temp_c-reference_c)/3600.0

def inventory_enthalpy(tanks: dict[str, tuple[float,float]]) -> dict:
    parts={name:water_enthalpy_kwh(v,t) for name,(v,t) in tanks.items()}
    return {"tanks_kwh":parts,"total_kwh":sum(parts.values())}

def net_decrease(h_t0_kwh: float, h_end_kwh: float) -> float:
    return h_t0_kwh-h_end_kwh

def heater_adjusted_decrease(h_t0_kwh: float, h_end_kwh: float, heater_input_kwh: float) -> float:
    return h_t0_kwh-h_end_kwh+heater_input_kwh
