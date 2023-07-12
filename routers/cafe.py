import requests
from fastapi import APIRouter, Depends

from database.session import get_db

from utils.config import settings

from crud.cafe import get_cafe_list_by_location

router = APIRouter()

db = Depends(get_db)

GOOGLE_KEY = settings.google_api_key

@router.get("/location", status_code=200)
def search_total_cafe_by_location(db = db) -> dict:
    ip_url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_KEY}"
    config = {'considerIp': True}

    data = requests.post(ip_url, config)
    current_location = data.json()

    cafe_list = get_cafe_list_by_location(current_location['location']['lat'], current_location['location']['lng'], db)

    return cafe_list

