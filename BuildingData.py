import openpyxl
from geopy import Yandex
from geopy import Nominatim
import json
import time

# Класс для работы с перечнем зданий
class BuildingData:
  def getData():
    geolocator_yandex = Yandex(api_key="1b2779ee-0b47-46e1-a95f-1f45d41033b5")
    geolocator_nomenatim = Nominatim(user_agent="memchiki")
    workbook = openpyxl.load_workbook("house_old.xlsx")
    worksheet = workbook.active
    buildingData = { "buildings": [] }
    id=1
    for row in worksheet.iter_rows(2, 950):
      try:
        location = geolocator_yandex.geocode(row[2].value)
        addr = geolocator_nomenatim.reverse((location.latitude, location.longitude))
        buildingData["buildings"].append({"id": id, 
                                    "address": addr.address,
                                    "lattitude": location.latitude,
                                    "longtitude": location.longitude,
                                    "appartments": row[7].value})
        id+=1
        time.sleep(1)
      except:
        print("Error occured while geocode")     
    
    with open("DataBase_Building.json", "w") as f:
      json.dump(buildingData, f, ensure_ascii=False)
    f.close()

BuildingData.getData()