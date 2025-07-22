from .data_loader import load_primary_mission, load_simulated_drones
from .interface import deconfliction_query
from .visualizer import plot_paths

primary = load_primary_mission("data/primary_mission.json")
simulated = load_simulated_drones("data/simulated_drones.json")

status, conflicts = deconfliction_query(primary, simulated)
print(f"Status: {status}")
if conflicts:
    for i, c in enumerate(conflicts, 1):
        print(f"[{i}] Conflict with {c['simulated_drone']} at {c['conflict_at']} during {c['time']}")


plot_paths(primary, simulated, conflicts)
from .plotly_visualizer import plotly_animate
plotly_animate(primary, simulated)
