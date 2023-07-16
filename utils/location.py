import math

def calculate_bound(
    lat:float, 
    lng:float
)-> dict:
    lat_change = 1 / 111.2
    lng_change = abs(math.cos(lat * (math.pi / 180)))

    bounds = {
        'min_lat': lat - lat_change,
        'min_lng': lng - lng_change,
        'max_lat': lat + lat_change,
        'max_lng': lng - lng_change
    }

    return bounds

