
import flask
import dash
from dash_bootstrap_components.themes import BOOTSTRAP
from layouts import layout
from flask_caching import Cache

server = flask.Flask(__name__)

dash_app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True, 
    external_stylesheets=[BOOTSTRAP],
)


dash_app.title = "Dashboard for Python"

dash_app.layout = layout

cache = Cache(dash_app.server, config={
    'CACHE_TYPE': 'redis',
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache_directory',

    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})

server = dash_app.server 

