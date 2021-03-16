import time
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

import requests

url = "https://www.vaccinespotter.org/api/v0/states/IL.json"
minutes = 1
center = {'lat': 0.0, 'lon': 0.0}
max_distance = 50
found = []


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956
    return c * r


def get_distance(data):
    return data['distance']


def sound(data):
    print("FOUND! {}".format(data))
    # GPIO.output(23, GPIO.HIGH)
    # time.sleep(10)
    # GPIO.output(23, GPIO.LOW)


def run():
    print("{} - Running".format(datetime.now()))
    # GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(23, GPIO.OUT)
    # GPIO.output(23, GPIO.LOW)
    resp = requests.get(url)
    data = resp.json()
    for feature in data['features']:
        coordinates = feature['geometry']['coordinates']
        if coordinates[0] is None or coordinates[1] is None:
            continue
        pharmacy_loc = {'lat': coordinates[1], 'lon': coordinates[0]}
        props = feature['properties']
        distance = haversine(center['lon'], center['lat'], pharmacy_loc['lon'], pharmacy_loc['lat'])
        if props['appointments_available'] and distance <= max_distance:
            found.append({
                "name": props['name'],
                "url": props['url'],
                "address": props['address'],
                "city": props['city'],
                "state": props['state'],
                "zip": props['postal_code'],
                "distance": distance
            })
    found.sort(key=get_distance)
    if len(found):
        sound(found)
    # GPIO.cleanup()


def main():
    while True:
        run()
        print("{} - Sleeping for {} minutes".format(datetime.now(), minutes))
        time.sleep(minutes * 60)


if __name__ == '__main__':
    main()
