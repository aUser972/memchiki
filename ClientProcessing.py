from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import uvicorn

class Request(BaseModel):
  name: str

class ClientProcessing:
    app = FastAPI()
    @app.post("/")
    async def get_data(item: Request):    
        #Waits for the request and converts into JSON
        result = await item.json()
        with open("TmpData.json") as f:
            json_data = json.load(f)
        f.close()
        #Prints result in cmd – verification purpose
        print(json_data)
        return json_data

    def start(self):
        with open("config.json") as f:
            config_data = json.load(f)
        f.close()
        uvicorn.run(self.app, host=config_data["ip_addr"], port=config_data["port"])


        