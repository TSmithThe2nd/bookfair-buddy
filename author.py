#imports
from pythonCrudFunctions import create_db_connection, execute_query
import pythonCrudFunctions

#varibles
connection = create_db_connection("localhost", "root",pw, "bookfairbuddy")
first_name=None
last_name=None
pw=""
# todo create basic crud functions each should be SQL queries
#with varibles ready for user input. 
#create new author
new_author= f"""
INSERT INTO author VALUES
(10, '{first_name}','{last_name}')
"""
execute_query(connection, new_author)

#read (all authors, all books from author)

#update(change authors name)

#delete