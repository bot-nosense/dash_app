from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from main import dash_app
from dash.exceptions import PreventUpdate
import json
import requests
import uuid
from main import cache

@cache.memoize()

@dash_app.callback(
    Output('layout1_textarea', 'placeholder'),
    Input('layout1_input', 'value'), # input text
    State('session-id', 'data'),
)
def update_areatext(api_url, data_store):
    if api_url:
        try:
            response = requests.get(api_url)
            data = response.json()
            data_store = json.dumps(data)
            return data_store
        except requests.exceptions.RequestException as e:
            print('error: ', e)
            return None

session_id = str(uuid.uuid4())


@dash_app.callback(Output('layout2_div', 'chidren'),
              Input('session-id', 'data'))
def on_data_set_table(data):
    if data is None:
        print('data is None')
        raise PreventUpdate
    return data

container = dbc.Card(
    dbc.CardBody(
        dbc.Container([
            dcc.Store(data=session_id, id='session-id'),
            dbc.Row([
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H5("Seed API", className="card-title"),
                            dbc.Input(placeholder="API ...", size="sm", valid=True, id= 'layout1_input'),
                        ]
                    ),
                    width={'size': 3}),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H5("https://dummyjson.com/products/1", className="card-title"),
                            dbc.Textarea(
                                valid=True,
                                className="mb-3",
                                placeholder="",
                                style={'height': '200px'},
                                id= 'layout1_textarea'
                            ),
                        ]
                    ),
                    className="align-self-center",
                    style={'height': '10rem'},
                    width={'size':9,'offset':0}
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H5("Push Data in Page 2", className="card-title"),
                            dbc.Button(
                                "Success", 
                                color="primary", 
                                className="me-1", 
                                style={"width": "100%"}, 
                                outline=True, 
                                href='/page-2',
                                id= 'layout1_button'
                            ),
                            html.Div([], id='div_none')
                        ]
                    ),
                    width={'size': 3},
                ),
            ]),
        ], fluid=True)
    ),
    style={
        "width": "98%",
        "height": "98%",
        "margin-left": "1%",
        "margin-right": "1%",
        "margin-top": "1%",
        "margin-bot": "1%",
    },
)

layout_1 = html.Div(
    [
        container,
    ]
)





