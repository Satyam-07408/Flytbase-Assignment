import matplotlib.pyplot as plt

def plot_paths(primary, simulated, conflicts=[]):
    plt.figure()
    px, py = zip(*[wp[:2] for wp in primary["waypoints"]])
    plt.plot(px, py, label="Primary", color='blue')

    for sim in simulated:
        sx, sy = zip(*[wp[:2] for wp in sim["waypoints"]])
        plt.plot(sx, sy, '--', label=f'Sim {sim["id"]}', alpha=0.7)

    for c in conflicts:
        plt.scatter(*c["conflict_at"], color='red', label="Conflict")

    plt.legend()
    plt.title("UAV Path Deconfliction")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.savefig("output.png")
    plt.show()
