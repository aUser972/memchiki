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
  maxConsumers: str
  minConsumers: str


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
    response = {}

    with open("DataBase.json") as f:
      jsonData = json.load(f)
    f.close()
    dataBase = jsonData["Data"][0]
    i=1
    if req.calculationModel == "Model1":
      response = { "Postamats": [] }
      for object in req.objectType:
        for area in req.Area:
          for postamat in dataBase[area][object]:
            if float(req.minConsumers) < postamat['coefficient'] < float(req.maxConsumers):
              postamat["id"] = i
              response['Postamats'].append(postamat)
              i+=1
    else:
      response = { "Polygon": [] }
      for object in req.objectType:
        for area in req.Area:
          for postamat in dataBase[area][object]:
            if float(req.minConsumers) < postamat['coefficient'] < float(req.maxConsumers):
              postamat["id"] = i
              response['Polygon'].append(postamat)
              i+=1
            
    return response

  def start(self):
    with open("config.json") as f:
      config_data = json.load(f)
    f.close()
    uvicorn.run(self.app, host=config_data["ip_addr"], port=config_data["port"])