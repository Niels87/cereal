from database.database_handler import DatabaseHandler
from parser_csv import ParserCSV
from utils.singleton import Singleton


class DBRequests(Singleton):
    
    def __init__(self) -> None:
        super().__init__()
        self._db_handler = self.setup_db()
        
    
    def setup_db(self) -> DatabaseHandler:
        
        db_config = {
            "user": "root", # edit this
            "password": "Kom12345", # edit this
            "host": "localhost", # can edit, but should be fine
            "db_name": "supersupercereal", # can edit, but not necessary
            "sql_folder": "database/", # relative to main.py
            "create_tables": "create_tables.sql", 
            "create_procedures": "create_stored_procedures.sql",
            "delimiter": "--#--new--#", # delimiter for parsing sql-files, dont change!
        }
        
        db_handler = DatabaseHandler(db_config)
        db_handler.drop_database()
        db_handler.create_and_set_database()
        db_handler.initialize_database()
        
        csv_data = ParserCSV().parse_csv("Cereal.csv")
        for row in csv_data:
            values = list(row.values())
            # print(row.values())
            # print(values)
            db_handler.db_connection.call_stored_procedure("add_item", values)
        
        return db_handler
        

    def get_from_database(self) -> list:
        cereal = self._db_handler.db_connection.call_stored_procedure("get_by_id", [1])
        print(cereal)
        return cereal
        