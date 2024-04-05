from utils.singleton import Singleton
import mysql.connector


class DatabaseConnection(Singleton):

    def __init__(self, config: dict) -> None:
        self._config = config
        self._connection = self._connect_mysql()

    @property
    def connection(self):
        return self._connection
    
    
    def _connect_mysql(self) -> mysql.connector.MySQLConnection:
        self._connection = mysql.connector.connect(
            host = self._config["host"],
            user = self._config["user"],
            password = self._config["password"]
        )
        return self._connection
    
    def set_database(self):
        self.connection.database = self._config["db_name"]
        
    def query_database(self, query: str) -> dict:
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        if cursor.with_rows == True:
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
        self.connection.commit()
        cursor.close()
        return result
    
    def call_stored_procedure(self, proc_name: str, proc_args: list) -> dict:
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.callproc(proc_name, proc_args)
            for r in cursor.stored_results():
                result = r.fetchall()
            warnings = cursor.warnings
        self.connection.commit()
        try:
            return result
        except:
            return warnings
        
    def get_field_names(self):
        with self.connection.cursor() as c:
            columns = c.description
            
        return columns