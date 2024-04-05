from database.database_connection import DatabaseConnection


""" Calls stored procedures in the database, 
    when receiving database requests """
class DatabaseInteraction(object):
    
    def __init__(self, db_connection: DatabaseConnection) -> None:
        self._db_conn = db_connection
    
    
    def handle_db_request(self):
        
        self.call_stored_procedure()
        
        
    
    def call_stored_procedure(self):
        pass