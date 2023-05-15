from dash import dcc, html
import src.templates.statistic_page as SP


def ClusterizationPage():
    layout = html.Div(SP.overhead), html.Div(children=[
        html.H4("Предсказание риска смертности по возрасту"),

        html.P("Выберите статистическую модель:"),
        dcc.Dropdown(
            id='dropdown',
            options=["Регрессия", "Дерево решений", "Метод К-средних"],
            value='Дерево решений',
            clearable=False
        ),
        dcc.Graph(id="graph"),
    ])
    return layout