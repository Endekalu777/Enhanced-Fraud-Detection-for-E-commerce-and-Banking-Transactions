from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialize Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# API endpoint
API_BASE_URL = 'http://localhost:5000/api'

# Layout
app.layout = html.Div([
    html.H1("Fraud Detection Dashboard", className="text-center mb-4"),
    
    # Summary Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Transactions", className="card-title"),
                    html.H2(id="total-transactions", className="card-text")
                ])
            ], color="info", outline=True)
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Fraud Cases", className="card-title"),
                    html.H2(id="total-fraud-cases", className="card-text")
                ])
            ], color="danger", outline=True)
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud Percentage", className="card-title"),
                    html.H2(id="fraud-percentage", className="card-text")
                ])
            ], color="success", outline=True)
        ]),
    ], className="mb-4"),

    # Graphs
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud Cases Over Time"),
                    dcc.Graph(id='time-series-graph')
                ])
            ])
        ], width=12, className="mb-4"),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud by Device"),
                    dcc.Graph(id='device-graph')
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud by Browser"),
                    dcc.Graph(id='browser-graph')
                ])
            ])
        ], width=6),
    ]),
    
    # Interval component for periodic updates
    dcc.Interval(
        id='interval-component',
        interval=30*1000,  # updates every 30 seconds
        n_intervals=0
    )
])