def test_pytest_available():
    import pytest
    assert pytest.__version__

def test_requests_available():
    import requests
    assert requests.__version__