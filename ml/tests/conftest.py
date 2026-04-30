import pytest
from fastapi.testclient import TestClient
from infer import app


@pytest.fixture(scope="module")
def client():
    """
    Provides a FastAPI TestClient for the ML inference service.
    """
    return TestClient(app)