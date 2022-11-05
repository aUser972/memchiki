import json
import random
from geopy import Nominatim

class OpenMapData:
  def getPostamatData():
    print("Generate data")
    json_data = { "Postamats": [] }
    geolocator = Nominatim(user_agent="memchiki")

    lat_from = 55.564566
    lat_to = 55.915321
    lon_from = 37.315118
    lon_to = 37.943093
    for i in range(20):
      lat = round(random.uniform(lat_from, lat_to), 6)
      lon = round(random.uniform(lon_from, lon_to), 6)
      coef = round(random.uniform(0, 1), 4)
      try:
        addr = geolocator.reverse((lat,lon))
        postamat = {"id": i, "lattitude": lat, "longtitude": lon, "address": addr.address, "coefficient": coef}
        json_data["Postamats"].append(postamat)
      except:
        print("Exception occured while reverse geocodein, id: ", i)

    with open("TmpData.json", "w") as f:
      json.dump(json_data, f, ensure_ascii=False)
    f.close()

  def getDistrictAndArea():
    print("Get district and area")

  def getTradeShop():
    print("Get trade shop")

  def getMFC():
    print("Get MFC")
  
  def getLibrary():
    print("Get library")

  def getCultureHouse():
    print("Get clubs and culture house")

  def getSportsObjects():
    print("Get sports objects") 



OpenMapData.getPostamatData()