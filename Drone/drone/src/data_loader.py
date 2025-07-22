import json

def load_primary_mission(path):
    with open(path) as f:
        return json.load(f)

def load_simulated_drones(path):
    with open(path) as f:
        return json.load(f)
