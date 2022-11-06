from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from typing import List

class AdministrativeDistrict(BaseModel):
  district: str

class Area(BaseModel):
  id: int
  name: str

class Hui(BaseModel):
  List[Area]

class ObjectType(BaseModel):
  objectType: str

class CalculationModel(BaseModel):
  calculationModel: str

AdministrativeDistricts = List[AdministrativeDistrict]
Areas = List[Area]
ObjectTypes = List[ObjectType]
class Request(BaseModel):
  AdministrativeDistricts
  Areas
  ObjectTypes
  CalculationModel


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
  async def get_data(item: List[Area]):    
    #Waits for the request and converts into JSON
    print(item)
    result = item.json()
    response = { "postamats": [] }
    # with open("TmpData_new.json") as f:
    #   json_data = json.load(f)
    # f.close()
    # print(result)
    # for area in result:
    #   for district in json_data["Districts"]:
    #     for are in district["area"]:
    #       if area == are:
    #         response['postamats'].append(are)

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


        