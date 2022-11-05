#!/bin/bash

curl -i -X PUT https://api.delivery.yandex.ru/pickup-points \
-H 'Content-Type: application/json' \
-H 'Authorization: OAuth y0_AgAAAAALEtDMAAiNnAAAAADTBKPHEiCBkRrWTau5oHcJbtY0RC9SWxY' \
-d \
'{
  "pickupPointIds": 
  [
    45987,
    12345,
    456897
  ],
  "latitude": 
  {
    "from": 37.315118,
    "to": 37.943093
  },
  "longitude": 
  {
    "from": 55.564566,
    "to": 55.915321  
  },
  "locationId": 1346,
  "type": "POST_OFFICE"
}'


55.755864, 37.617698
curl 'http://geocode-maps.yandex.ru/1.x/?geocode=Москва, магазин Травы и приправы'
https://geocode-maps.yandex.ru/1.x/?apikey=1b2779ee-0b47-46e1-a95f-1f45d41033b5&geocode=Пункты Выдачи&ll=
37.617698,55.755864&spn=0.352069,0.350552