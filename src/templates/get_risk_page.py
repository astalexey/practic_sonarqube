from dash import dcc, html
import dash_bootstrap_components as dbc
import src.templates.statistic_page as SP


dropdown = html.Div(
    [
        dbc.Label("Пол", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="inputSex",
            className="card-title m3",
            options=[
                {"label": "Женский", "value": 1},
                {"label": "Мужской", "value": 2},
            ],
        ),
        dbc.Label("Возраст", html_for="slider", className="text-light"),
        dcc.Dropdown(
            id="inputAge",
            className="card-title m3",
            options=[
                {"label": "от 0 до 25", "value": 1},
                {"label": "от 25 до 40", "value": 2},
                {"label": "от 40 до 80", "value": 3},
                {"label": "от 80 и более", "value": 4},
            ],
        ),
        dbc.Label("Пневмония", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownPnevmo",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Беременность", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownPregant",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Диабет", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownDiabet",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Хроническая обструктивная болезнь лёгких", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownCopd",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Астма", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownAstma",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Иммуносупрессия", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownInmsupr",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Артериальная гипертензия", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownCardiovascular",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Cердечно-сосудистые заболевания", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownHypertension",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Хроническая почечная недостаточность", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownRenalChronic",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Другие заболевания", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownOtherDisease",
            options=[
                {"label": "Есть", "value": 1},
                {"label": "Нет", "value": 2},
            ],
        ),
        dbc.Label("Ожирение", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownObesity",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Статус курения", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownTobacco",
            options=[
                {"label": "Курящий", "value": 2},
                {"label": "Не курящий", "value": 1},
            ],
        ),
        dbc.Label("Были ли вы интубированы?", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownIntubed",
            options=[
                {"label": "Да", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Были ли вы в интенсивной терапии?", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownIcu",
            options=[
                {"label": "Да", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
    ],
    className="m-3",
)


def GetRiskPage():
    layout = html.Div(SP.overhead), html.Div(children=[
        html.H1(children='Hello Dash'),  # Create a title with H1 tag

        dbc.Row(
            dbc.Col(
                dbc.Form([dropdown]),
                width={"size": 6, "offset": 3},
            )
        ),

        dbc.Row(dbc.Col(
            html.H1(id='container-button-basic', children='Выберите значения!', className="text-light"),
            className="p-3 bg-dark text-center")),

        dbc.Row(dbc.Col([
            dbc.Button("Вывести риск смертности", color="success", id="submit-risk", className="d-grid gap-2 col-6 m-3"),
            dbc.Button("Вывести влияющие признаки", color="success", id="submit-val", className="d-grid gap-2 col-6 m-3"),
            ],
            width={"size": 10, "offset": 1},
            className="d-flex justify-content-center justify-content-around "),
        ),
        html.Div(id="tab-content", className="p-4"),
    ])
    return layout