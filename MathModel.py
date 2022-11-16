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


def sorting_by_coef_poly(data, k):
    postamats = data['Polygon']
    swapped = False
    for i in range(len(postamats)-1, 0, -1):
        for j in range(i):
            if postamats[j]['coefficient'] < postamats[j+1]['coefficient']:
                postamats[j]['id'], postamats[j + 1]['id'] = postamats[j + 1]['id'], postamats[j]['id']
                postamats[j], postamats[j+1] = postamats[j+1], postamats[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    postamats = postamats[0:k]
    return {'Polygon': postamats}

def sorting_by_coef_post(data, k):
    postamats = data['Postamats']
    swapped = False
    for i in range(len(postamats)-1, 0, -1):
        for j in range(i):
            if postamats[j]['coefficient'] < postamats[j+1]['coefficient']:
                postamats[j]['id'], postamats[j + 1]['id'] = postamats[j + 1]['id'], postamats[j]['id']
                postamats[j], postamats[j+1] = postamats[j+1], postamats[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    postamats = postamats[0:k]
    return {'Postamats': postamats}