import pytest

@pytest.fixture
def sample_data():
    """
    Fixture que proporciona datos de ejemplo para los tests
    """
    return {
        "name": 5,
        "value": 5
    }

@pytest.fixture
def mock_external_api():
    """
    Fixture que simula una API externa
    """
    class MockAPI:
        def get_data(self):
            return {"status": "success"}
    
    return MockAPI() 