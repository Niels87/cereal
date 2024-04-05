from database import database_connection, database_builder, database_interaction
from utils.singleton import Singleton

"""A wrapper class around the
    DatabaseConnection (handles the connection),
    DatabaseBuilder (sets up the database incl. stored procedures),
    and DatabaseInteraction (calls stored procedures) classes."""
class DatabaseHandler(Singleton):
    
    def __init__(self) -> None:
        super().__init__()
        
        #self._db_interaction = database_interaction.DatabaseInteraction(self._db_connection)
    
    @property
    def config(self):
        return self._config

    @property
    def db_connection(self):
        return self._db_connection

    # @property
    # def db_interaction(self):
    #     return self._db_interaction

    @property
    def db_builder(self):
        return self._db_builder

    # create_database() must be run befor set_database().
    # cannot connect to a database, that doesn't exist.
    def initialize_database(self, config: dict, drop_first=True):
        self._config = config
        
        self._db_connection = database_connection.DatabaseConnection(config)
        self._db_builder = database_builder.DatabaseBuilder(self.db_connection, config)
        if drop_first == True:
            self.db_builder.drop_database()    
        
        self.db_builder.create_database() 
        self.db_connection.set_database()
        self.db_builder.create_tables()
        self.db_builder.create_procedures()

    def set_db_column_config(self, names_with_types: dict):
        self._column_config = names_with_types

    
    def handle_db_request_get_all(self) -> list[dict]:
        db_data = self.db_connection.call_stored_procedure(
            proc_name="get_all",
            proc_args=[0]
        )
        return db_data
    
    def handle_db_request(self, proc: str, req_params: dict) -> list[dict]:
        
        match proc:
            case "get_by_fieldvalue":
                args = self.format_GET_args(req_params)
            case "add_item":
                args = self.format_POST_args(req_params)
        db_data = self.db_connection.call_stored_procedure(
            proc_name=proc, 
            proc_args=args
            )
        return db_data
    
    def format_GET_args(self, req_params: dict) -> tuple:
        field = req_params["field"]
        value = req_params["value"]
        return (field[0], value[0], 0)
    
    def format_POST_args(self, req_params: dict) -> tuple:
        args = []
        for cn in self._column_config:
            args.append( self.type_cast_column(cn,req_params[cn][0]))
        
        return tuple(args)
    
    def type_cast_column(self, field: str, value: str) -> int | float | str:
        
        try:
            match self._column_config[field]:
                case "Int":
                    return int(value)
                case "Float":
                    return float(value)
                case _:
                    return value
        except:
            return value
        
        
    def validate_field(self, field: str) -> bool:
        if self._column_config.keys().__contains__(field):
            return True
        else:
            return False
        
        