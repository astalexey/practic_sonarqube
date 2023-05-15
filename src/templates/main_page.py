from dash import html
import dash_bootstrap_components as dbc


first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Анализ статистическими моделями", className="card-title"),
            html.P("Классификация, кластеризация, расчет риска смертности"),
            dbc.Button("Анализ", color="success", href="/static-page", id="nav_button"),
        ],
        className="text-center"
    )
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Анализ нейронной сетью", className="card-title"),
            html.P(
                "Предсказание развития пандемии"
            ),
            dbc.Button("Анализ", color="success", href="/neuron-page", id="nav_button"),
        ],
        className="text-center"

    )
)

overhead = html.Div([
    dbc.Row(dbc.Col(
        html.H1("Анализ данных о COVID-19 с использованием нейронной сети и статистических моделей", className="text-light"),
        className="p-3 bg-dark text-center")),

    dbc.Row(dbc.Col(
        [
            dbc.Col(first_card, width=5, className="m-5 d-inline-block"),
            dbc.Col(second_card, width=5, className="m-5 d-inline-block"),
        ],
        width={"size": 10, "offset": 1},
        className="d-flex justify-content-center justify-content-around"),
    )
])


def MainPage():
    layout = overhead
    return layout