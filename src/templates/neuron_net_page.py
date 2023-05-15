from dash import dcc, html
import dash_bootstrap_components as dbc
import src.templates.main_page as sp


dropdown = html.Div(
    [
        dbc.Label("Пол", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="inputSexN",
            className="card-title m3",
            options=[
                {"label": "Женский", "value": 1},
                {"label": "Мужской", "value": 2},
            ],
        ),

        dbc.Label("Возраст", html_for="slider", className="text-light"),
        dcc.Slider(1, 100, 1,
                   id='inputAgeN',
                   marks={1: {'label': '1'},
                          25: {'label': '25'},
                          50: {'label': '50'},
                          75: {'label': '75'},
                          100: {'label': '100'}},
                   value=1,
                   updatemode='drag'
                   ),
        html.H4(id='updatemode-cont', style={'margin-top': 20}, className="text-light"),
        dbc.Label("Пневмония", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownPnevmoN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Беременность", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownPregantN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Диабет", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownDiabetN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Хроническая обструктивная болезнь лёгких", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownCopdN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Астма", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownAstmaN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Иммуносупрессия", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownInmsuprN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Артериальная гипертензия", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownCardiovascularN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Cердечно-сосудистые заболевания", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownHypertensionN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Хроническая почечная недостаточность", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownRenalChronicN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Другие заболевания", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownOtherDiseaseN",
            options=[
                {"label": "Есть", "value": 1},
                {"label": "Нет", "value": 2},
            ],
        ),
        dbc.Label("Ожирение", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownObesityN",
            options=[
                {"label": "Есть", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Статус курения", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownTobaccoN",
            options=[
                {"label": "Курящий", "value": 2},
                {"label": "Не курящий", "value": 1},
            ],
        ),
        dbc.Label("Были ли вы интубированы?", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownIntubedN",
            options=[
                {"label": "Да", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
        dbc.Label("Были ли вы в интенсивной терапии?", html_for="dropdown", className="text-light"),
        dcc.Dropdown(
            id="dropdownIcuN",
            options=[
                {"label": "Да", "value": 2},
                {"label": "Нет", "value": 1},
            ],
        ),
    ],
    className="m-3",
)


def NeuronPage():
    layout = html.Div(sp.overhead), html.Div(children=[
        html.H1(children='Вывод риска с помощью нейронной сети'),  # Create a title with H1 tag

        dbc.Row(
            dbc.Col(
                dbc.Form([dropdown]),
                width={"size": 6, "offset": 3},
            )
        ),

        dbc.Row(dbc.Col(
            html.H1(id='container-button-neuron', children='Выберите значения!', className="text-light"),
            className="p-3 bg-dark text-center")),

        dbc.Row(dbc.Col([
            dbc.Button("Вывести риск смертности", color="success", id="sub-neuron", className="d-grid gap-2 col-6 m-3"),
        ],
            width={"size": 10, "offset": 1},
            className="d-flex justify-content-center justify-content-around "),
        ),
        html.Div(id="tab-content_neuron", className="p-4"),
    ])
    return layout