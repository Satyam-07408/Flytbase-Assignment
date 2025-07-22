import math

SAFETY_RADIUS = 10  # meters
TIME_TOLERANCE = 5  # seconds

def distance(p1, p2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def spatial_conflict(wp1, wp2, radius=SAFETY_RADIUS):
    return distance(wp1[:2], wp2[:2]) < radius

def temporal_overlap(t1, t2):
    return not (t1[1] < t2[0] or t1[0] > t2[1])

def check_conflicts(primary, simulated):
    conflicts = []
    for sim in simulated:
        for i, wp1 in enumerate(primary["waypoints"]):
            t1 = primary["timestamps"][i]
            for j, wp2 in enumerate(sim["waypoints"]):
                t2 = sim["timestamps"][j]
                if spatial_conflict(wp1, wp2) and temporal_overlap(t1, t2):
                    conflicts.append({
                        "conflict_at": wp1[:2],
                        "time": t1,
                        "simulated_drone": sim["id"]
                    })
    return conflicts
