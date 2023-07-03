from sqlalchemy.orm import Session
from database.models import Cafe

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

