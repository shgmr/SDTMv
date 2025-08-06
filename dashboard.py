import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Read the CSV file into a DataFrame
df = pd.read_csv("Survival.csv")

# Compute Kaplan-Meier survival probabilities
times = []
survival_probs = []
n_subjects = len(df)
n_at_risk = n_subjects
survival_prob = 1.0

unique_times = np.unique(df['time'])

for t in unique_times:
    d = np.sum((df['time'] == t) & (df['event'] == 1))  # number of events at time t
    c = np.sum((df['time'] == t) & (df['event'] == 0))  # number censored at time t
    if n_at_risk > 0:
        survival_prob *= (1 - d / n_at_risk)
        times.append(t)
        survival_probs.append(survival_prob)
        n_at_risk -= (d + c)

# Plot Kaplan-Meier curve using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=times,
    y=survival_probs,
    mode='lines+markers',
    name='Kaplan-Meier Estimate',
    line=dict(color='blue'),
    marker=dict(size=6)
))

fig.update_layout(
    title='Time to First AE (Kaplan-Meier Survival Curve)',
    xaxis_title='Time (days)',
    yaxis_title='Survival Probability',
    yaxis=dict(range=[0, 1]),
    template='plotly_white'
)

#------------------------------------------------------------------------------------------
# Read the CSV file into a DataFrame
ae = pd.read_csv("ae.csv")

import plotly.express as px

# Create a bar chart showing AE frequency by study day, stratified by severity
fig_ae = px.bar(ae, x='StudyDay', y='AE_Count', color='Severity',
             title='Adverse Events Over Time by Severity',
             labels={'AE_Count': 'Number of Adverse Events', 'StudyDay': 'Study Day'})


#-------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV file into a DataFrame
lb = pd.read_csv("lb.csv")

# Create the plot
fig_lb = px.line(lb, x='StudyDay', y='LabValue', color='Subject', facet_col='LabTest',
              title='Lab Value Trends Over Time by Subject')


# Add shaded normal range for ALT (7–56) and AST (5–40)

lab_tests = ['ALT', 'AST']

for i, test in enumerate(lab_tests):
    if test == 'ALT':
        lower, upper = 7, 56
    elif test == 'AST':
        lower, upper = 5, 40

    fig_lb.add_shape(
        type="rect",
        xref="x domain",
        yref="y",
        x0=0, x1=1,
        y0=lower, y1=upper,
        fillcolor="lightgreen",
        opacity=0.3,
        layer="below",
        line_width=0,
        row=1, col=i+1
    )

# Update layout
fig_lb.update_layout(height=500, showlegend=True)
#fig_lb.show()


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H6("SDTM Metrics Interactive Dashboard created by Jun Shigemura", className="text-center my-3"), width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    #html.H5("Kaplan-Meier Survival", className="card-title"),
                    dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": "300px"})
                ])
            ], className="mb-3")
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    #html.H5("Another KPI", className="card-title"),
                    dcc.Graph(figure=fig_ae, config={"displayModeBar": False}, style={"height": "300px"})
                ])
            ], className="mb-3")
        ], width=6),
    ]),

     dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    #html.H5("Kaplan-Meier Survival", className="card-title"),
                    dcc.Graph(figure=fig_lb, config={"displayModeBar": False}, style={"height": "300px"})
                ])
            ], className="mb-3")
        ], width=12),
    ])
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)

