from ClientProcessing import ClientProcessing
from Calculation import Calculation

if __name__ == '__main__':
  # geolocator = Yandex(api_key="1b2779ee-0b47-46e1-a95f-1f45d41033b5")
  # geolocator = Nominatim(user_agent="memchiki")
  # location = geolocator.geocode("Пункты выдачи")
  # print((location.latitude, location.longitude))
  # calculationInstance = Calculation()
  clientProcessingInstance = ClientProcessing()
  # calculationInstance.start()
  clientProcessingInstance.start()
