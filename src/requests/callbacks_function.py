from src.templates.main_page import MainPage
from src.templates.statistic_page import StatisticPage
import src.templates.classific_page as CP
from src.templates.clusterization_page import ClusterizationPage
from src.templates.get_risk_page import GetRiskPage
from src.templates.neuron_net_page import NeuronPage
from src.business_logic.data import get_data_for_risk
import src.business_logic.classification_decision as class_decision
import numpy as np
from src.business_logic.neuron_net_decision import data_preprocessing
import dash_bootstrap_components as dbc
from dash import dcc


def display_page_func(path):
    if path == '/static-page':
        return StatisticPage()
    elif path == '/static-page/classification':
        return CP.ClassificationPage()
    elif path == '/static-page/clasterization':
        return ClusterizationPage()
    elif path == '/static-page/get-risk':
        return GetRiskPage()
    elif path == '/neuron-page':
        return NeuronPage()
    else:
        return MainPage()


def calcutate_risk_static_func(sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed):
    if (sex != None and  age != None and pnevmo != None and diabet != None and cord != None and astma != None and inmsupr != None and cardio != None and hypertension != None):
        param = [sex, age]

        data = get_data_for_risk(param)
        importances, score = class_decision.calculate_risk(data)

        specifications = np.array([1, intubed-1, pnevmo-1, 1, pregant-1, diabet-1, cord-1, astma-1, inmsupr-1, hypertension-1, disease-1, cardio-1, obesity-1, renal-1, tobaco-1])

        result = round(sum(importances * specifications)*100, 2)

        return 'Ваш риск смертности при болезни: {}%'.format(result)
    else:
        return 'Введите данные!'


def calcutate_risk_neuron_func(sex, age, pnevmo, pregant, diabet, cord, astma, inmsupr, cardio, hypertension, renal, disease, obesity, tobaco, intubed):
    if (sex != None and  age != None and pnevmo != None and diabet != None and cord != None and astma != None and inmsupr != None and cardio != None and hypertension != None):

        specifications = np.array([[sex-1, intubed-1, pnevmo-1, age, pregant-1, diabet-1, cord-1, astma-1, inmsupr-1, hypertension-1, disease-1, cardio-1, obesity-1, renal-1, tobaco-1]])

        predict_risk, score = data_preprocessing(specifications)

        return "Риск смертности: " + str(round(predict_risk[0][0] * 100, 2))+"%, Достоверность предсказания: "+str(round(score * 100, 2))+"%"

    else:
        return 'Введите данные!'


def output_factors(sex, age):
    if (sex != None and  age != None):
        param = [sex, age]

        data = get_data_for_risk(param)
        importances, score = class_decision.calculate_risk(data)

        if(sex == 1):
            result = class_decision.corr_risk_female
        else:
            result = class_decision.corr_risk_male

        return dbc.Row(
            [
                dbc.Col(dcc.Graph(figure={'data': [{'x': result, 'y': importances, 'type': 'bar'}, ],
                                          'layout': {'title': 'Влияние признаков на смертность'}}),)
            ]
        )