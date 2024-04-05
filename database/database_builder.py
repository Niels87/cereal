import os
from database.database_connection import DatabaseConnection
import itertools

""" Handles creation/dropping of the database and
    setting up tables and stored procedures"""
class DatabaseBuilder(object):
    
    
    def __init__(self, db_connection: DatabaseConnection, config: dict) -> None:
        self._db = db_connection.connection
        self._config = config

    @property
    def config(self):
        return self._config
    
    @property
    def db(self):
        return self._db
    
    def create_database(self):
        query = "CREATE DATABASE IF NOT EXISTS " + self.config["db_name"] + ";"
        with self.db.cursor() as cursor:
            cursor.execute(query)
        self.db.commit()
    
    def drop_database(self):
        query = "DROP DATABASE IF EXISTS " + self.config["db_name"] + ";"
        with self.db.cursor() as cursor:
            cursor.execute(query)
        self.db.commit()
    
    def create_tables(self):
        file = self.config["sql_folder"] + self.config["create_tables"]
        with open(file, 'r') as f:
            queries = f.read().split( self.config["delimiter"] )
            for query in queries:
                with self.db.cursor() as cursor:
                    cursor.execute(query, multi=True)
                self.db.commit()
    
    def create_procedures(self):
        file = self.config["sql_folder"] + self.config["create_procedures"]
        with open(file, 'r') as f:
            queries = f.read().split( self.config["delimiter"] )
            for query in queries:
                with self.db.cursor() as cursor:
                    cursor.execute(query, multi=True)
                self.db.commit()
        