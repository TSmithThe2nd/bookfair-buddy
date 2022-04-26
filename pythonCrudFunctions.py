# import all packages here
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Connect functions

# connect to data base function
def create_server_connection(host_name, user_name, user_password):
    connection=None
    try:
        connection= mysql.connector.connect(
            host= host_name,
            user= user_name,
            password= user_password
        )

        print("SQL Database connection succesful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#connect to database function
def create_db_connection(host_name, user_name, user_password, database_name):
    connection=None
    try:
        connection= mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        )
        print("SQL Database connection Succesful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection
############################################

# Create functions

#creates create database function
def create_database(connection, query):
    cursor= connection.cursor()
    try:
        cursor.execute(query)
        print('Database created!')
    except Error as err:
        print(f"Error: '{err}'")

# Query execute funtion
# takes a string and return a querey execution
def execute_query(connection, query):
    cursor= connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successfull")
    except Error as err:
        print(f"Error:'{err}'")

######################################################

# read function
# Create read function
def read_query(connection, query):
    cursor= connection.cursor()
    result= None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")