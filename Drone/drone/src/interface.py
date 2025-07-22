from .conflict_checker import check_conflicts

def deconfliction_query(primary_mission, simulated_drones):
    conflicts = check_conflicts(primary_mission, simulated_drones)
    if conflicts:
        return "conflict detected", conflicts
    else:
        return "clear", []
