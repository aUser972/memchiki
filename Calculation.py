import threading
import time
import json

class Calculation(threading.Thread):
    def getData(self):
        print("Try to get data")
    
    def calc(self):
        print('Do calc')
        

    def run(self,*args,**kwargs):
        with open("config.json") as f:
            config_data = json.load(f)
        f.close()
        while True:
            self.calc()
            time.sleep(config_data["recalc_timer_sec"])


