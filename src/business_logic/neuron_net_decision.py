from sklearn.model_selection import train_test_split
from src.business_logic.data import get_data
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from sklearn.metrics import accuracy_score


def data_preprocessing(character):
    data = get_data()
    X = data[["SEX", "INTUBED", "PNEUMONIA", "AGE", "PREGNANT", "DIABETES", "COPD", "ASTHMA", "INMSUPR", "HIPERTENSION",
              "OTHER_DISEASE", "CARDIOVASCULAR", "OBESITY", "RENAL_CHRONIC", "TOBACCO"]]
    y = data.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.2, random_state=0)

    sc = StandardScaler()

    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    neuron_net = tf.keras.models.Sequential()

    neuron_net.add(tf.keras.layers.Dense(units=6, activation='sigmoid'))
    neuron_net.add(tf.keras.layers.Dense(units=6, activation='sigmoid'))
    neuron_net.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    neuron_net.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    neuron_net.fit(X_train, y_train, batch_size=32, epochs=100)

    y_pred = neuron_net.predict(X_test)
    y_pred = (y_pred > 0.5)

    obj = sc.transform(character)

    predict_risk = neuron_net.predict(obj)

    score = accuracy_score(y_test, y_pred)

    return predict_risk, score