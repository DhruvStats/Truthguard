def test_prediction_has_label(client):
    response = client.post("/predict", json={"text": "Breaking news today"})
    assert "prediction" in response.json()