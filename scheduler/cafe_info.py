import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from fastapi import HTTPException

from utils.config import settings
from crud.cafe import get_total_cafe_name_list, update_new_cafe
from database.session import get_db

GOOGLE_KEY = settings.google_api_key
KAKAO_KEY  = settings.kakao_api_key

def get_facility_info(facility_url: str) -> dict:
    driver = webdriver.Safari()
    facility_url = facility_url

    driver.get(facility_url)
    time.sleep(0.5)

    wifi        = True if driver.find_elements(By.CLASS_NAME, 'ico_wifi') else False
    parking     = True if driver.find_elements(By.CLASS_NAME, 'ico_parking') else False
    wheelchair  = True if driver.find_elements(By.CLASS_NAME, 'ico_handicapped') else False
    animal      = True if driver.find_elements(By.CLASS_NAME, 'ico_animal') else False

    return {'wifi':wifi, 'parking':parking, 'wheelchair':wheelchair, 'animal':animal}

def update_kakao_local_cafe():
    db = next(get_db())

    db_cafe_list = get_total_cafe_name_list(db)

    url = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code=CE7"
    header = {'Authorization': 'KakaoAK ' + KAKAO_KEY}

    result = requests.get(url, headers=header)
    if not result.status_code == 200:
        raise HTTPException(status_code=400, detail='잘못된 요청입니다')
    else:
        result = result.json()

    kakao_cafe_list = result['documents']

    new_cafe_list = []
    if db_cafe_list:
        for new_cafe in kakao_cafe_list:
            for cafe in db_cafe_list:
                if new_cafe['place_name'] == cafe[0]:
                    break
                else:
                    url = new_cafe['place_url']
                    facility_info = get_facility_info(url)
                    new_cafe['facility_info'] = facility_info
                    new_cafe_list.append(new_cafe)

        for new_cafe in new_cafe_list:
            update_new_cafe(new_cafe, db)

        db.close()
    else:
        for new_cafe in kakao_cafe_list:
            url = new_cafe['place_url']
            facility_info = get_facility_info(url)
            new_cafe['facility_info'] = facility_info
            update_new_cafe(new_cafe, db)

        db.close()

