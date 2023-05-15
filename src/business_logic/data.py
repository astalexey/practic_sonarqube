import pandas as pd


#Добавление колонки типа смерти человека
def died_stats(value):
    if value == "9999-99-99":
        return 0
    else:
        return 1


#Определение возрастного диапозона
def get_age(age):
    result = ""
    if(age == 1):
        result = 'AGE > 0 & AGE < 26'
    elif(age == 2):
        result = 'AGE > 25 & AGE < 41'
    elif(age == 3):
        result = 'AGE > 40 & AGE < 81'
    elif(age == 4):
        result = 'AGE > 81'

    return result


#Получение данных
def get_data():
    data = pd.read_csv('../Covid Data.csv', sep=',')
    data['DIED'] = data['DATE_DIED'].map(died_stats)
    data = data.dropna()
    data = data.head(10000)
    return data


#Получение данных для расчета риска
def get_data_for_risk(param=[], *args):

    paramQuery = 'SEX == {}'.format(
        param[0]
    )

    data = pd.read_csv('../Covid Data.csv', sep=',').query(paramQuery)

    data = data.query(get_age(param[1]))

    data['DIED'] = data['DATE_DIED'].map(died_stats)
    data = data.dropna()
    data = data.head(10000)
    return data