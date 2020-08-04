import json
with open("config.json","r") as f:
    config =json.load(f) 
class ConfigDB:
    def __init__(self):
        self.host=config.get("host") #'database-2.cdqj5q1oiaw9.eu-west-3.rds.amazonaws.com'
        self.user = config.get("user") #'admin'
        self.password = config.get("password") #'Clarusway_1'
        self.db=config.get("db") # 'phone_book'
        self.port =config.get("port") # 3306
        