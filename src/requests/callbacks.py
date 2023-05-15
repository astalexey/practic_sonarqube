from dash import Input, Output, State
from src.business_logic.clusterization_decision import get_risk_age
import src.requests.callbacks_function as callback_func


def get_callbacks(app):

    #Определение открываемой страницы
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        return callback_func.display_page_func(pathname)


    @app.callback(Output('updatemode-cont', 'children'),
                  Input('inputAgeN', 'value'))
    def display_value(value):
        return 'Возраст: '+str(value)


    #Расчет риска смертности статистическая модель
    @app.callback(
        Output("container-button-basic", "children"),
        Input('submit-risk', 'n_clicks'),
        State('inputSex', 'value'),
        State('inputAge', 'value'),
        State('dropdownPnevmo', 'value'),
        State('dropdownPregant', 'value'),
        State('dropdownDiabet', 'value'),
        State('dropdownCopd', 'value'),
        State('dropdownAstma', 'value'),
        State('dropdownInmsupr', 'value'),
        State('dropdownCardiovascular', 'value'),
        State('dropdownHypertension', 'value'),
        State('dropdownRenalChronic', 'value'),
        State('dropdownOtherDisease', 'value'),
        State('dropdownObesity', 'value'),
        State('dropdownTobacco', 'value'),
        State('dropdownIntubed', 'value'),
    )
    def calcutate_risk_static(n_clicks, sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed):
        if n_clicks:
            result = callback_func.calcutate_risk_static_func(sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed)
            return result


    #Расчет риска смертности Нейронная сеть
    @app.callback(
        Output("container-button-neuron", "children"),
        Input('sub-neuron', 'n_clicks'),
        State('inputSexN', 'value'),
        State('inputAgeN', 'value'),
        State('dropdownPnevmoN', 'value'),
        State('dropdownPregantN', 'value'),
        State('dropdownDiabetN', 'value'),
        State('dropdownCopdN', 'value'),
        State('dropdownAstmaN', 'value'),
        State('dropdownInmsuprN', 'value'),
        State('dropdownCardiovascularN', 'value'),
        State('dropdownHypertensionN', 'value'),
        State('dropdownRenalChronicN', 'value'),
        State('dropdownOtherDiseaseN', 'value'),
        State('dropdownObesityN', 'value'),
        State('dropdownTobaccoN', 'value'),
        State('dropdownIntubedN', 'value'),
    )
    def calcutate_risk_neuron(n_clicks, sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed):
        if n_clicks:
            return callback_func.calcutate_risk_neuron_func(sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed)


    #Вывод влияющих факторов
    @app.callback(
        Output("tab-content", "children"),
        Input('submit-val', 'n_clicks'),
        State('inputSex', 'value'),
        State('inputAge', 'value'),
    )
    def output_factors(n_clicks, sex, age):
        if n_clicks:
            return callback_func.output_factors(sex, age)


    @app.callback(
        Output("graph", "figure"),
        Input('dropdown', "value"))
    def train_and_display(name):
        fig = get_risk_age(name)
        return fig