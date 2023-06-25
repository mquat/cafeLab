import requests

from fastapi import HTTPException

from utils.config import settings
from crud.cafe import get_total_cafe_name_list, update_new_cafe
from database.session import get_db

GOOGLE_KEY = settings.google_api_key
KAKAO_KEY  = settings.kakao_api_key

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
                new_cafe_list.append(new_cafe)

        for new_cafe in new_cafe_list:
            update_new_cafe(new_cafe, db)

        db.close()
    else:
        for new_cafe in kakao_cafe_list:
            update_new_cafe(new_cafe, db)

        db.close()

