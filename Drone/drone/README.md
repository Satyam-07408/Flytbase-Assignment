# UAV Strategic Deconfliction System 🚁

This project implements a **strategic deconfliction service** for UAVs operating in shared airspace. It checks whether a primary drone's mission plan (defined as a series of spatiotemporal waypoints) conflicts with simulated drone flights, ensuring flight safety before takeoff.

---

## 📂 Project Structure

uav_deconfliction/
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── data_loader.py
│ ├── conflict_checker.py
│ ├── interface.py
│ └── visualizer.py
├── data/
│ ├── primary_mission.json
│ └── simulated_drones.json
├── README.md
├── reflection.md

## 🚀 How to Run

Make sure you're in the root directory (`Drone/`), then run:
python3 -m src.main

**Inputs**
Primary mission: data/primary_mission.json
 Example:    {
              "waypoints": [[0, 0], [10, 10], [20, 20]],
              "timestamps": [[0, 10], [11, 20], [21, 30]]
             }
Simulated flights: data/simulated_drones.json
 Example:   [
                {
                    "id": "drone_1",
                    "waypoints": [[5, 5], [15, 15]],
                    "timestamps": [[5, 15], [16, 25]]
                }
            ]

**Output**
Console: "Status: clear" or "conflict detected", with full conflict explanations

Visualization: output.png — showing all flight paths and conflict points

**🎬 Spatiotemporal Animation (Plotly)**

This project includes an interactive time-based animation using Plotly. The animation:

   1.  Visually shows the movement of the primary and simulated drones over time

   2.  Animates each drone's path based on their assigned timestamp intervals

   3.  Displays each time step with a slider and “Play” button in the browser

    4. Can be exported and shared as an HTML file

To generate and open the animation:
run : python3 -m src.main
This will create a file:
uav_animation.html
   
                                                                  **THANK YOU**