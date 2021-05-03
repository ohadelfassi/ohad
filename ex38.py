# originally from http://stackoverflow.com/a/15737218/57952 :
from math import radians, cos, sin, asin, sqrt

ISRAEL_LAT, ISRAEL_LON = 31.5, 34.75

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
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

from csv import DictReader

with open("cow.csv", encoding="utf8") as f, open("index.html", "w", encoding="utf8") as w:
    reader = DictReader(f)
    for d in reader:
        #print(degel->kovetz)
        print(f'<img src="http://static.10x.org.il/flags/{d["short_name"].lower()}.png">', file=w)
        print(f'<li>{d["name"]}: {haversine(ISRAEL_LON, ISRAEL_LAT, float(d["lon"]), float(d["lat"]))}</li>', file=w)
