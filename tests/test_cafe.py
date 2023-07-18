import requests

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def mock_get_google_ip():
    return f"https://www.googleapis.com/geolocation/v1/geolocate?key=test_key"

def test_search_cafe_by_location():
    ip_url = mock_get_google_ip()
    config = {'considerIp': True}
    location_data = requests.post(ip_url, config)
    response = client.request(
        "GET",
        "/cafe/location",
        json = location_data.json()
    )

    assert response.status_code == 200

