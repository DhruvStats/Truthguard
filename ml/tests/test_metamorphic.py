"""
Metamorphic testing checks whether fundamental properties
of the model remain consistent under benign transformations.
"""


def test_same_input_same_output(client):
    """
    The same input should always produce the same prediction.
    """
    text = "The government announced a new economic policy today."

    r1 = client.post("/predict", json={"text": text})
    r2 = client.post("/predict", json={"text": text})

    assert r1.json()["prediction"] == r2.json()["prediction"]


def test_irrelevant_words_do_not_flip_prediction(client):
    """
    Adding irrelevant filler words should not flip the prediction.
    """
    base_text = "Scientists confirmed the discovery after peer review."
    noisy_text = base_text + " blah blah lorem ipsum random text"

    r1 = client.post("/predict", json={"text": base_text})
    r2 = client.post("/predict", json={"text": noisy_text})

    assert r1.json()["prediction"] == r2.json()["prediction"]


def test_case_insensitivity(client):
    """
    Uppercase and lowercase versions of the same text
    should yield the same prediction.
    """
    text_lower = "inflation rates remain stable according to reports"
    text_upper = text_lower.upper()

    r1 = client.post("/predict", json={"text": text_lower})
    r2 = client.post("/predict", json={"text": text_upper})

    assert r1.json()["prediction"] == r2.json()["prediction"]