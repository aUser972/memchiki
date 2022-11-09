import json
import random
from geopy import Nominatim
from pymongo import MongoClient
import openpyxl
from geopy import Yandex

class OpenMapData:
  def getPostamatData():
    geolocator_yandex = Yandex(api_key="1b2779ee-0b47-46e1-a95f-1f45d41033b5")
    geolocator_nomenatim = Nominatim(user_agent="memchiki")
    workbook = openpyxl.load_workbook("HouseInfo.xlsx")
    worksheet = workbook.active
    json_data = {}
    with open("another_safe.json", "r") as f:
      json_data = json.load(f)  
    f.close()
    i=1
    for row in worksheet.iter_rows(2, 300):
      try:
        location = geolocator_yandex.geocode(row[2].value)
        coef = round(random.uniform(0, 1), 4)
        addr = geolocator_nomenatim.reverse((location.latitude,location.longitude))
        for district in json_data["Districts"]:
          for are in district["area"]:
            if addr.address.find(are['name']) > 0:
              postamat = {"id": i, "lattitude": location.latitude, "longtitude": location.longitude, "address": addr.address, "coefficient": coef}
              are['postamats'].append(postamat)
              i+=1
      except:
        print("Exception occured while reverse geocodein")

    with open("TmpData_new.json", "w") as f:
      json.dump(json_data, f, ensure_ascii=False)
    f.close()

    # client = MongoClient('localhost', 27017)
    # db = client['postamats_db']
    # db.create_collection("postamats")
    # postamats_collections = db["postamats"]
    # postamats_collections.insert_one(json_data)
    # client.close()

  def test():
    print("Try test")

    client = MongoClient('localhost', 27017)
    db = client['postamats_db']
    coll = db['postamats']
    data = coll.find_one({"Districts.name": "Северо-Западный"})
    print(data)

OpenMapData.getPostamatData()
# OpenMapData.test()