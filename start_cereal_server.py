from http.server import HTTPServer
from cereal_server import CerealServer
from database.database_handler import DatabaseHandler
from parser_csv import ParserCSV


    
class ServerRunner():
    
    def __init__(self, db_config: dict, server_config: dict) -> None:
        self._host_name = server_config["host_name"]
        self._server_port = server_config["server_port"]
        self._db = self.setup_db(db_config)
    
    
    def setup_db(self, db_config: dict) -> DatabaseHandler:
        db_handler = DatabaseHandler()
        db_handler.initialize_database(db_config)
        
        parser = ParserCSV()
        csv_data = parser.parse_csv(db_config["data_csv_file"])
        db_handler.set_db_column_config( parser._fieldnames_with_types )
        
        for row in csv_data:
            values = list(row.values())
            db_handler.db_connection.call_stored_procedure("add_item", values)
        
        return db_handler
    
    def run_server(self):
        
        webServer = HTTPServer((self._host_name, self._server_port), CerealServer)
        
        print("Server started http://%s:%s" % (self._host_name, self._server_port))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")
        
        
from config import db_config, server_config

if __name__ == "__main__":        
    runner = ServerRunner(db_config, server_config)
    runner.run_server()
    runner._db.db_builder.drop_database()
    
    
