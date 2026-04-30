"""
Model quality and responsible AI tests for TruthGuard.
These tests check correctness, robustness, and fairness properties.
"""

def test_prediction_not_empty(client):
    """Prediction must be either REAL or FAKE."""
    r = client.post("/predict", json={"text": "Breaking news reported today"})
    assert r.json()["prediction"] in ("REAL", "FAKE")


def test_confidence_range(client):
    """Confidence must be between 0 and 100."""
    r = client.post("/predict", json={"text": "Breaking news reported today"})
    conf = r.json()["confidence"]
    assert 0 <= conf <= 100


def test_explanation_present(client):
    """Explanation must be non-empty."""
    r = client.post("/predict", json={"text": "Breaking news reported today"})
    assert isinstance(r.json()["explanation"], str)
    assert len(r.json()["explanation"]) > 0


def test_black_box_known_real(client):
    """Clearly factual news should be REAL."""
    text = "The Prime Minister addressed parliament during the budget session."
    r = client.post("/predict", json={"text": text})
    assert r.json()["prediction"] == "REAL"


def test_black_box_known_fake(client):
    """Clearly conspiratorial text should be FAKE."""
    text = "Aliens secretly control governments using 5G towers."
    r = client.post("/predict", json={"text": text})
    assert r.json()["prediction"] == "FAKE"


def test_adversarial_typos(client):
    """Small typos should not flip prediction."""
    clean = "The government announced new healthcare reforms."
    noisy = "The g0vernment ann0unced new healthcare ref0rms."
    r1 = client.post("/predict", json={"text": clean})
    r2 = client.post("/predict", json={"text": noisy})
    assert r1.json()["prediction"] == r2.json()["prediction"]


def test_fairness_no_demographic_bias(client):
    """
    Changing demographic mentions should not change prediction.
    """
    text1 = "A teacher reported the incident to authorities."
    text2 = "A teacher from a minority community reported the incident to authorities."
    r1 = client.post("/predict", json={"text": text1})
    r2 = client.post("/predict", json={"text": text2})
    assert r1.json()["prediction"] == r2.json()["prediction"]