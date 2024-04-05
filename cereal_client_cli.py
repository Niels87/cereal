import requests
import requests.api
from prompt_toolkit import formatted_text, print_formatted_text, HTML, prompt
from html_parser import MyHTMLParser
from bs4 import BeautifulSoup
from utils.formatting import print_dict
import string
from utils.formatted_printing import CerealPrinter

class CerealCLI():
    
    def __init__(self) -> None:
        self.main_loop()
    
    
    def main_loop(self):
        
        db_config: dict = self.send_get_request("db_config")[0]
        #print_dict(db_config)
        
        while True:
            
            req_type = prompt("\ninput request type\n -> ")
            
                        
            match req_type:
                case "get":
                    params = prompt("\ninput optional search parameters as: field=value\n -> ")
                    key = params.split("=", maxsplit=1)[0].strip()
                    val = params.split("=", maxsplit=1)[1].strip()
                    if db_config.keys().__contains__(key):
                        self.send_get_request("results", {"field": key, "value": val})
                case "post":
                    data = {}
                    for key in db_config.keys():
                        data[key] = None
                    missing = True    
                    while missing:
                        print_dict(data)
                        params:str = prompt("\ninput new cereal data as: field=value \n all fields except ID must be supplied\n -> ")
                        
                        match params:
                            case "exit" | "quit":
                                break
                        
                        key = params.split("=", maxsplit=1)[0].strip()
                        val = params.split("=", maxsplit=1)[1].strip()
                        print(key)
                        print(val)
                                                
                        missing = False
                        for value in data.values():
                            if value == None:
                                missing = True
                        
                        if missing == False:
                            self.send_post_request(data)
                        
                            
                        
                        # missing = False
                        # for key in db_config.keys():
                        #     if data.__contains__(key) == False:
                        #         missing = True
                            
                case "exit":
                    break
                case "quit":
                    break
                
    
    
    def send_get_request(self, path: str, params: dict = None):
        
        try:        
            response = requests.get(f"http://localhost:8080/{path}", params=params)
        except Exception as e:
            print(e)
            return
        
        print(response.status_code)
        if response.status_code != 200:
            print(response.reason)
            return
        
        print_dict(response.headers)
        print("")
                    
        try:
            match response.headers["Content-type"]:
                # case "dict":
                #     data = self.parse_to_dict(response)
                #     print_dict(data)
                case "text/json":
                    data = response.json()
                    self.print_data(data)
                    
                    return data
                    
        except Exception as e :
            e.add_note("Content-type not recognized")
            print(e)
                    
    
    def print_data(self, data: list[dict]):
        
        for dict in data:
            print("----------------")
            print_dict(dict)
        print("----------------")
        
        # try:
        #     CerealPrinter().print_table_of_cereal(data)
        # except Exception as e:
        #     print(e)
    
    def send_post_request(self, params: dict):
               
        
        try:        
            response = requests.post("http://localhost:8080/", params=params)
        except Exception as e:
            print(e)
            return

        print(response.status_code)
        if response.status_code != 200:
            print(response.reason)
            return
        
        print_dict(response.headers)
        print("")
    
    
    def new_cereal(self) -> dict:
        
        new_cereal = {    
            "proc": "add_item",
            "name": "super duper cereal",
            "mfr": "Q",
            "type": "C",
            "calories": 110,
            "protein": 2,
            "fat": 0,
            "sodium": 125,
            "fiber": 1,
            "carbo": 11,
            "sugars": 14,
            "potass": 30,
            "vitamins": 25,
            "shelf": 2,
            "weight": 1,
            "cups": 1,
            "rating": "33.174.094",
        }
        return new_cereal


if __name__ == "__main__":
    
    # params = {
    #     "proc": "get_by_fieldvalue",    
    #     "field": "sodium",
    #     "value": "210", 
    # }
    
    
    
    cli = CerealCLI()
    
    
    # params_post = cli.new_cereal()
    # cli.send_post_request(params_post)
    
