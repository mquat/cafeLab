from sqlalchemy import between, and_
from sqlalchemy.orm import Session

from database.models import Cafe

from utils.location import calculate_bound

def get_total_cafe_name_list(db = Session) -> Cafe:
    cafe_list = db.query(Cafe).with_entities(Cafe.name).all()

    return cafe_list

def update_new_cafe(
    new_cafe: dict,
    db = Session
)-> None:
    cafe = Cafe(
        id = Cafe.id,
        name = new_cafe['place_name'],
        address = new_cafe['road_address_name'],
        phone = new_cafe['phone'],
        lat = new_cafe['x'],
        lng = new_cafe['y'],
        parking = new_cafe['facility_info']['parking'],
        wifi = new_cafe['facility_info']['wifi'],
        animal = new_cafe['facility_info']['animal'],
        wheelchair = new_cafe['facility_info']['wheelchair']
    )

    db.add(cafe)
    db.commit()
    db.refresh(cafe)

    return

def get_cafe_list_by_location(
    lat: float,
    lng: float,
    db: Session
):
    bounds = calculate_bound(lat, lng)

    cafe_list = db.query(Cafe).where(
                    and_(
                        between(Cafe.lat, bounds['min_lat'], bounds['max_lat']),
                        between(Cafe.lng, bounds['min_lng'], bounds['max_lng'])
                    )
                ).all()

    return cafe_list

