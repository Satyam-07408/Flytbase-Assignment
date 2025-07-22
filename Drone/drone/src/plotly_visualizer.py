# src/plotly_visualizer.py
import plotly.graph_objects as go

def plotly_animate(primary, simulated):
    frames = []
    all_x, all_y = [], []

    for t in range(0, 35):
        primary_x, primary_y = [], []
        traces = []

        for wp, ts in zip(primary["waypoints"], primary["timestamps"]):
            if ts[0] <= t <= ts[1]:
                primary_x.append(wp[0])
                primary_y.append(wp[1])
                all_x.append(wp[0])
                all_y.append(wp[1])

        traces.append(go.Scatter(
            x=primary_x,
            y=primary_y,
            mode="lines+markers",
            name="Primary",
            marker=dict(color="blue", size=10)
        ))

        for sim in simulated:
            sim_x, sim_y = [], []
            for wp, ts in zip(sim["waypoints"], sim["timestamps"]):
                if ts[0] <= t <= ts[1]:
                    sim_x.append(wp[0])
                    sim_y.append(wp[1])
                    all_x.append(wp[0])
                    all_y.append(wp[1])
            traces.append(go.Scatter(
                x=sim_x,
                y=sim_y,
                mode="lines+markers",
                name=sim["id"],
                line=dict(dash="dash")
            ))

        frames.append(go.Frame(data=traces, name=str(t)))

    fig = go.Figure(
        data=frames[0].data,
        layout=go.Layout(
            title="UAV Spatiotemporal Animation (Plotly)",
            xaxis=dict(title="X", range=[min(all_x)-5, max(all_x)+5]),
            yaxis=dict(title="Y", range=[min(all_y)-5, max(all_y)+5]),
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play", method="animate", args=[None])]
            )]
        ),
        frames=frames
    )

    fig.write_html("uav_animation.html", auto_open=True)
