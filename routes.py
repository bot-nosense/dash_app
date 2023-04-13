
from dash.dependencies import Input, Output 
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output 
from main import dash_app

from layout1 import layout_1
from layout2 import layout_2


@dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/page-1':
        return layout_1
    elif pathname == '/page-2':
        return layout_2
    elif pathname == '/':
        return layout_1
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
















