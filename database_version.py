"""
Database version of the GUI Login System [Python3]

This script is the database version of the main script file. Almost every code is the same, but the difference is the storing of the data. The main.py script file stores the user credentials data in the data.json file, whereas this script would make the use of the sqlite3 databases.

Author : Rishav Das
Created on : May 06, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from sqlite3 import connect

# Connecting to the database.db file
# Note : If the file does not exists, then the connection automatically creates a new blank database file
sql = connect('database.db')
cursor = sql.cursor()

# Checking if the users table exists or not
cursor.execute('SELECT count(name) FROM sqlite_master WHERE type="table" AND name="users";')
if cursor.fetchone()[0] == False:
	# If the users table does not exist, then we create it

	cursor.execute('CREATE TABLE users (username VARCHAR(30), password VARCHAR(100));')
