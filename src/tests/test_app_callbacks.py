import requests

ENDPOINT = 'http://127.0.0.1:8050/'

def test_api_main_page():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_api_static_page():
    response = requests.get(ENDPOINT+'/static-page')
    assert response.status_code == 200

def test_api_classification_page():
    response = requests.get(ENDPOINT+'/static-page/classification')
    assert response.status_code == 200

def test_api_clasterization_page():
    response = requests.get(ENDPOINT+'/static-page/clasterization')
    assert response.status_code == 200

def test_api_risk_page():
    response = requests.get(ENDPOINT+'/static-page/get-risk')
    assert response.status_code == 200

def test_api_neuron_page_page():
    response = requests.get(ENDPOINT+'/neuron-page')
    assert response.status_code == 200
