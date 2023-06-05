import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = 'bagage_tracking_systeem'


if username is None or password is None or host is None:
        raise Exception('Please set the environment variables for the database connection')

print(username, password, host)

if __name__ == '__main__':
        # create database
        conn = mysql.connector.connect(
                user=username, password=password, host=host)
        cursor = conn.cursor()
        cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {database} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        conn.commit()
        conn.close()

        print('Database created')

        with open('schema.sql', 'r') as f:
                query = f.read()

        conn = mysql.connector.connect(
                user=username, password=password, host=host, database=database)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
