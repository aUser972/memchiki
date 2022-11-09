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

    with open("TmpData_new.json") as f:
      json_data = json.load(f)
    f.close()

    if req.calculationModel == "Model1":
      response = { "Postamats": [] }
      for area in req.Area:
        for district in json_data["Districts"]:
          for are in district["area"]:
            if area == are['name']:
              for i in are['postamats']:
                if float(req.minConsumers) < i['coefficient'] < float(req.maxConsumers):
                  response['Postamats'].append(i)
    else:
      response = { "Polygon": [] }
      for area in req.Area:
        for district in json_data["Districts"]:
          for are in district["area"]:
            if area == are['name']:
              for i in are['postamats']:
                if float(req.minConsumers) < i['coefficient'] < float(req.maxConsumers):
                  response['Polygon'].append(i)
    return response

  def start(self):
    with open("config.json") as f:
      config_data = json.load(f)
    f.close()
    uvicorn.run(self.app, host=config_data["ip_addr"], port=config_data["port"])