import math
import json

# Площадь пересечения двух кругов с одинаковым радиусом
# Возвращает 0, если окружности не пересекаются и площадь круга, если центры совпали
def get_shape(R, dist):
    if not dist:
        return math.pi * R * R
    if 2 * R > dist:
         return 0
    F = 2 * math.acos(dist / (2 * R))
    S = R*R*(F - math.sin(F))
    return S

#Вычисление расстояния между 2-мя точками
def haversine(lat1, lon1, lat2, lon2): # широта и долгота точек
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2))
    rad = 6371302
    c = 2 * math.asin(math.sqrt(a))
    print('dist = ', rad * c)
    return rad * c

with open("DataBase_pickpoint.json") as f:
    data_pick = json.load(f)
f.close()

with open("DataBase.json") as f:
    data_house = json.load(f)
f.close()
i = 0
for pick_postamat in data_pick["postamats"]:
    for object in req.objectType:
        for area in req.Area:
            for house in data_house["Data"][0]["Жилой дом"]:
                if i == 10:
                    break
                haversine(pick_postamat['lattitude'], pick_postamat['longtitude'], house['lattitude'], house['longtitude'])
            if i == 10:
                break
