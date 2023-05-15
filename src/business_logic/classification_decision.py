import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from src.business_logic.data import get_data

corr = ["Пол","Был ли интубирован?","Пневмония","Возраст","Беременность","Диабет","Хроническая болезнь легких","Астма",
        "Подавленный иммунитет","Гипертония","Другие заболевания","Заболевания сердца","Ожирение","Заболевание почек","Статус курения","Был ли пациент в интенсивной терапии"]

corr_risk_female = ["Пол","Был ли интубирован?","Пневмония","Возраст","Беременность","Диабет","Хроническая болезнь легких","Астма",
                  "Подавленный иммунитет","Гипертония","Другие заболевания","Заболевания сердца","Ожирение","Заболевание почек","Статус курения"]

corr_risk_male = ["Пол","Был ли интубирован?","Пневмония","Возраст","Диабет","Хроническая болезнь легких","Астма",
             "Подавленный иммунитет","Гипертония","Другие заболевания","Заболевания сердца","Ожирение","Заболевание почек","Статус курения"]


#Расчет влияющих факторов
def solve_classification():
    vectorizer = TfidfVectorizer()

    data = get_data()

    train_test_feature_matrix = vectorizer.fit_transform(data['DATE_DIED']).toarray()
    a = pd.DataFrame(train_test_feature_matrix)
    data['DATE_DIED'] = a[a.columns[1:]].apply(lambda x: sum(x.dropna().astype(float)), axis=1)

    corr = data[["SEX","INTUBED","PNEUMONIA","AGE","PREGNANT","DIABETES","COPD","ASTHMA",
                 "INMSUPR","HIPERTENSION","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","RENAL_CHRONIC","TOBACCO","ICU"]]

    y = data['DIED']

    x_train, x_test, y_train, y_test = train_test_split(corr, y, test_size=0.01, random_state=42)

    clf = DecisionTreeClassifier(random_state=241)
    clf.fit(x_train, y_train)
    score = clf.score(x_test, y_test)
    importances = clf.feature_importances_

    return importances, score


#Расчет риска смертности
def calculate_risk(data):
    vectorizer = TfidfVectorizer()

    train_test_feature_matrix = vectorizer.fit_transform(data['DATE_DIED']).toarray()
    a = pd.DataFrame(train_test_feature_matrix)
    data['DATE_DIED'] = a[a.columns[1:]].apply(lambda x: sum(x.dropna().astype(float)), axis=1)

    corr = data[["SEX","INTUBED","PNEUMONIA","AGE","PREGNANT","DIABETES","COPD","ASTHMA",
                 "INMSUPR","HIPERTENSION","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","RENAL_CHRONIC","TOBACCO"]]

    y = data['DIED']

    x_train, x_test, y_train, y_test = train_test_split(corr, y, test_size=0.01, random_state=42)

    clf = DecisionTreeClassifier(random_state=241)
    clf.fit(x_train, y_train)
    score = clf.score(x_test, y_test)
    importances = clf.feature_importances_

    return importances, score