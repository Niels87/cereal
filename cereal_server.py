from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler
import http.server
from db_setup import DBRequests
from database.database_handler import DatabaseHandler
from utils import formatting
from urllib.parse import urlparse, parse_qs
import json

class CerealServer(CGIHTTPRequestHandler):
    

    
    def do_GET(self):
        parsed = urlparse(self.path)
        req_params = parse_qs(parsed.query) 
        
        
        if parsed.path == "/db_config":
            self.send_response(200)        
            self.send_header("Content-type", "text/json")
            self.end_headers()
            config = DatabaseHandler()._column_config
            json_data = json.dumps([config])
            self.wfile.write(json_data.encode("utf-8"))
            return
        
        if parsed.path != '/results':
            self.bad_request("url-path not recognized")
            return
        print(req_params.__contains__("field"))
        
        if req_params.__contains__("field"):
            try: 
                field = req_params["field"][0]
                if DatabaseHandler().validate_field(field) == True:
                    self.GET_good_request(req_params)
                else:
                    self.bad_request(f"specified field: {field}, not recognized")
            except Exception as e:
                print("req_params.__contains__(field)")
                self.bad_request(str(e))
        else:
            self.GET_good_request({})


    def GET_good_request(self, req_params: dict[str, list[str]]):
        print("good request")
        self.send_response(200)        
        self.send_header("Content-type", "text/json")
        self.end_headers()
        
        print("\n--- Req-params ---")        
        formatting.print_dict(req_params)
        print("------------------\n")
        
        if req_params.__contains__("field") == False:
            db_data = DatabaseHandler().handle_db_request_get_all()
            json_data = json.dumps(db_data)
            self.wfile.write(json_data.encode("utf-8"))
            return
        
        try:
            db_data = self.request_database(proc="get_by_fieldvalue", query_params=req_params)
            json_data = json.dumps(db_data)
            self.wfile.write(json_data.encode("utf-8"))
        except Exception as e:
            print(f"{e}: {e.args}")
        
    def do_POST(self) -> None:
        
        req_params = parse_qs(urlparse(self.path).query)
        
        for field in DatabaseHandler()._column_config.keys():
            if req_params.__contains__(field) == False:
                self.bad_request(f"field: {field}, not provided")
                return
        
        try:
            self.POST_good_request(req_params)
        except Exception as e:
            self.bad_request(e.__str__())
        
    
    def POST_good_request(self, req_params: dict[str, list[str]]):
        self.send_response(200)  
        self.end_headers()
        
        print("\n--- Req-params ---")        
        formatting.print_dict(req_params)
        print("------------------\n")
        
        try:
            db_data = self.request_database(proc="add_item", query_params=req_params)
            # json_data = json.dumps(db_data)
            # self.wfile.write(json_data.encode("utf-8"))
            
        except Exception as e:
            print(f"{e}: {e.args}")

    def bad_request(self, message: str):
        self.send_error(400, message)
        self.end_headers()

    def request_database(self, proc: str, query_params: dict) -> list[dict]:
        
        data = DatabaseHandler().handle_db_request(proc, query_params)        
        return data
    