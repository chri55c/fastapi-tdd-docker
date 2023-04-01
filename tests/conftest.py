import os

import pytest
from fastapi.testclient import TestClient

from app.main import create_application
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=True, database_url=os.environ.get("TEST_DATABASE_URL"))

@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    # Override get_settings in app/config.py
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
