from dash import dcc, html
import dash_bootstrap_components as dbc
import src.business_logic.classification_decision as CD
import src.templates.statistic_page as SP


importances, score = CD.solve_classification()


def ClassificationPage():
    layout = html.Div(SP.overhead), html.Div([dbc.Container(
        [
            html.H1("Iris k-means clustering"),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col([
                        dcc.Graph(figure={'data': [{'x': CD.corr, 'y': importances, 'type': 'bar'}, ],
                                          'layout': {
                                              'title': 'Влиятние признаков на смертность'
                                          }
                                          }
                                  ),
                        html.H3("Оценка качества: ", className="text-light"),
                        html.H3(score, className="text-light")
                    ], md=12),
                ],
                align="center",
            ),
        ],
        fluid=True,
    )])
    return layout
