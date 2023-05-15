from dash import html
import dash_bootstrap_components as dbc


first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Классификация", className="card-title"),
            dbc.Button("Анализ", color="success", href="/static-page/classification", id="nav_button"),
        ],
        className="text-center"
    )
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Кластеризация", className="card-title"),
            dbc.Button("Анализ", color="success", href="/static-page/clasterization", id="nav_button"),
        ],
        className="text-center"

    )
)


third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Рассчитать риск", className="card-title"),
            dbc.Button("Анализ", color="success", href="/static-page/get-risk", id="nav_button"),
        ],
        className="text-center"

    )
)


overhead = html.Div([
    dbc.Row(dbc.Col(
        html.H1("Анализ данных о COVID-19 с использованием нейронной сети и статистических моделей", className="text-light"),
        className="bg-dark text-center")),

    dbc.Row(dbc.Col(
        [
            dbc.Col(first_card, width=4, className="m-3 d-inline-block"),
            dbc.Col(second_card, width=4, className="m-3 d-inline-block"),
            dbc.Col(third_card, width=4, className="m-3 d-inline-block"),
        ],
        width={"size": 10, "offset": 1},
        className="d-flex justify-content-center justify-content-around "),
    ),

    dbc.Row(dbc.Col(
        [
            dbc.Button("Главная страница", color="success", href="/", id="nav_button", className="d-grid gap-2 col-6 m-3"),
        ],
        width={"size": 6, "offset": 3},
        className="d-flex justify-content-center"),
    )
])


def StatisticPage():
    layout = overhead
    return layout