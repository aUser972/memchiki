from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union
import json
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from typing import List

class Item(BaseModel):
  name: str

class Request(BaseModel):
  AdministrativeDistricts: List[str]
  Area: List[str]
  objectType: List[str]
  calculationModel: str
  minConsumers: str
  maxConsumers: str


class ClientProcessing:
  app = FastAPI()
  origins = ["*"]
  app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
  )
  @app.post("/")
  async def get_data(req: Request):
    #Waits for the request and converts into JSON
    # print(req)
    # result = item.json()
    response = { "Postamats": [] }
    with open("TmpData_new.json") as f:
      json_data = json.load(f)
    f.close()
    for area in req.Area:
      for district in json_data["Districts"]:
        for are in district["area"]:
          if area == are['name']:
            for i in are['postamats']:
              print(i)
              response['Postamats'].append(i)
    print(response)
    # Prints result in cmd – verification purpose
    return response

  @app.get("/")
  async def get_data():
    print("Get data")
    return { "name": "Andrey"}

  def start(self):
    with open("config.json") as f:
      config_data = json.load(f)
    f.close()
    uvicorn.run(self.app, host=config_data["ip_addr"], port=config_data["port"])


# with open("TmpData_new.json") as f:
#   json_data = json.load(f)
# f.close()

# for district in json_data["Districts"]:
#   for are in district["area"]:
#     print(are['postamats'])