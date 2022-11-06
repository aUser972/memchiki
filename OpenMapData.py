import json
import random
from geopy import Nominatim
from pymongo import MongoClient

class OpenMapData:
  def getPostamatData():
    print("Generate data")
    json_data = {}
    with open("another.json", "r") as f:
      json_data = json.load(f)  
    f.close()    
    geolocator = Nominatim(user_agent="memchiki")

    lat_from = 55.564566
    lat_to = 55.915321
    lon_from = 37.315118
    lon_to = 37.943093
    for i in range(200):
      lat = round(random.uniform(lat_from, lat_to), 6)
      lon = round(random.uniform(lon_from, lon_to), 6)
      coef = round(random.uniform(0, 1), 4)
      try:
        addr = geolocator.reverse((lat,lon))
        for district in json_data["Districts"]:
          for are in district["area"]:
            if addr.address.find(are['name']) > 0:
              postamat = {"id": i, "lattitude": lat, "longtitude": lon, "address": addr.address, "coefficient": coef}
              are['postamats'].append(postamat)
      except:
        print("Exception occured while reverse geocodein, id: ", i)

    with open("TmpData_new.json", "w") as f:
      json.dump(json_data, f, ensure_ascii=False)
    f.close()

    client = MongoClient('localhost', 27017)
    db = client['postamats_db']
    db.create_collection("postamats")
    postamats_collections = db["postamats"]
    postamats_collections.insert_one(json_data)
    client.close()

  def test():
    print("Try test")

    client = MongoClient('localhost', 27017)
    db = client['postamats_db']
    coll = db['postamats']
    data = coll.find_one({"Districts.name": "Северо-Западный"})
    print(data)

# OpenMapData.getPostamatData()
OpenMapData.test()




  # def getDistrictAndArea():
  #   print("Get district and area")

  # def getTradeShop():
  #   print("Get trade shop")

  # def getMFC():
  #   print("Get MFC")
  
  # def getLibrary():
  #   print("Get library")

  # def getCultureHouse():
  #   print("Get clubs and culture house")

  # def getSportsObjects():
  #   print("Get sports objects") 