# Warehouse Management System
A system for managing the warehouse of an online store or similar. At the moment it is designed as an employee facing application running in the command-line. 

## Functionality

It allows the user to search for items in the warehouse database, as well as add, remove and update information about the items. Some desired functionality is still missing:

- Report generation (eg. more advanced search)
- Logging of changes in the database (a transaction table is created, but it currently not used)

It currently doesn't handle consumer facing functionality, such as orders, sales, returns etc. But the application is designed with extensibility in mind.

## Application Design

The application is designed around 3 main components, with some additional smaller utility components.

- Command-line interface (cli.py)
- Database handling (database_handler.py)
- Event-system (event_handler.py)

The command-line layer talks to the database layer through the event-system. The user actions of addding, removing, updating and searching for items are all implemented as pairs of requests and responses through the event-system. Queries to the database are implemented as stored procedures.

I made this choice with extensibility in mind. Any additional functionality, fx something consumer related, can just hook into the event-system, without touching the rest of the application. If new database queries are needed, they can be added as stored procedures.

## Dependencies

- A running MySQL server
- Python 3.12 (can probably work with earlier versions, but it was tested with this one)
- Packages specified in requirements.txt

## Setup

- Make sure you have a running MySQL server. 
- Setup the virtual environment with requirements.txt

- Edit the config dictionary in **main.py** with the correct information for your system:

```python
   # in main.py, main()
   
   db_config = {

        "user": "root", # edit this
        "password": "PASSWORD", # edit this 
        "host": "localhost", # can edit, but should be fine
        "db_name": "warehousedb", # can edit, but not necessary
        "sql_folder": "database/db_config/", # relative to main.py
        "create_tables": "create_tables.sql", 
        "create_procedures": "create_stored_procedures.sql",
        "delimiter": "--#--new--#", # delimiter for parsing sql-files, dont change!

    }
```
- Run main.py from a terminal.

The application builds the database when its starts and drops it when it shuts down (assuming it shuts down correctly). To shut down correctly, make sure you exit the application by pressing escape from the main menu.
