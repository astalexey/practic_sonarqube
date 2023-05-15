from dash import html, dash, dcc
import dash_bootstrap_components as dbc
from src.requests.callbacks import get_callbacks

app = dash.Dash(
    external_stylesheets=[dbc.themes.COSMO],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
app.config.suppress_callback_exceptions = False

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className="bg-dark")
])

get_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)
