import openpyxl
from geopy import Yandex

# Класс для работы с перечнем зданий
class BuildingData:
  def getData():
    geolocator = Yandex(api_key="1b2779ee-0b47-46e1-a95f-1f45d41033b5")
    workbook = openpyxl.load_workbook("house_old.xlsx")
    worksheet = workbook.active
    for row in worksheet.iter_rows(2, 2):
      location = geolocator.geocode(row[2].value)
      print(row[2].value, end="\t\t") # адрес
      print(row[7].value, end="\t\t") # количество квартир
      print((location.latitude, location.longitude))
    
# BuildingData.getData()