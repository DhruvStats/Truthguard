"""
Robustness testing ensures the system behaves safely
under unusual or extreme inputs.
"""


def test_empty_input_response(client):
    """
    Empty input should be rejected with a clear error response.
    """
    response = client.post("/predict", json={"text": ""})

    assert response.status_code in (400, 422)


def test_very_long_input_does_not_crash(client):
    """
    Extremely long input should not crash the server.
    """
    long_text = "news " * 10000
    response = client.post("/predict", json={"text": long_text})

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_special_characters_input(client):
    """
    Input containing only numbers or symbols should not crash the system.
    """
    text = "1234567890 !!! ??? ### $$$"
    response = client.post("/predict", json={"text": text})

    assert response.status_code == 200
    assert "prediction" in response.json()
