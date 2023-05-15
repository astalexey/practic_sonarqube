import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split
from src.business_logic.data import get_data
from sklearn import linear_model, tree, neighbors
import numpy as np

models = {'Регрессия': linear_model.LinearRegression,
          'Дерево решений': tree.DecisionTreeRegressor,
          'Метод К-средних': neighbors.KNeighborsRegressor}


def get_risk_age(name):
    df = get_data()
    data = df[["DIED", "AGE"]]
    X = data.AGE.values[:, None]

    X_train, X_test, y_train, y_test = train_test_split(
        X, data.DIED, random_state=42)

    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    score = round(mse(y_test, model.predict(X_test)), 2)

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train, name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test, name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range,  name='prediction')
    ])

    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      title="Оценка качества: " + str(score),
                      xaxis_title="Возраст",
                      yaxis_title="1 - человек умер, 0 - человек жив",
                      margin=dict(l=0, r=0, t=30, b=0))

    return fig