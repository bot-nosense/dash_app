from dash import html, dcc
import dash_bootstrap_components as dbc


content = html.Div(id="page-content")

layout = html.Div([
    html.Div(
        className= "app-div",
        children= [
            dbc.Row([
                dbc.Col([html.H3("Learning Dash"), ]),
                dbc.Col([
                    dbc.Button("Home", outline=True, color="primary", className="me-1", style={ "margin-left": "1%", "margin-right": "1%",}, href='/page-1'),
                    dbc.Button("Page 1", outline=True, color="primary", className="me-1", style={ "margin-left": "1%", "margin-right": "1%",}, href='/page-1'),
                    dbc.Button("Page 2", outline=True, color="primary", className="me-1", style={ "margin-left": "1%", "margin-right": "1%",}, href='/page-2'),
                ]),
            ],
            style={
                "margin-left": "1%",
                "margin-top": "1%",
            }, ),
            html.Hr(),
        ]),
    dcc.Location(id="url"), content
]) 