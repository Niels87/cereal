db_config = {
            "user": "root", # edit this
            "password": "Kom12345", # edit this
            "host": "localhost", # can edit, but should be fine
            "db_name": "superdupercereal", # can edit, but not necessary
            "data_csv_file": "data/Cereal.csv",
            "sql_folder": "database/", # relative to main.py
            "create_tables": "create_tables.sql", 
            "create_procedures": "create_stored_procedures.sql",
            "delimiter": "--#--new--#", # delimiter for parsing sql-files, dont change!
        }

server_config = {
    "host_name": "localhost",
    "server_port": 8080,
    
}