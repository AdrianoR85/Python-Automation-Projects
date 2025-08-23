import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
  DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('BD_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
  }

  @classmethod
  def get_connection(cls):
    try:
      connection = psycopg2.connect(**cls.DB_CONFIG)
      return connection
    except psycopg2.Error as e:
      print(f"Error connection to database: {e}")
      return None

  @classmethod
  def create_users_table(cls):
    connection = cls.get_connection()
    if connection:
      try:
        cursor = connection.cursor()
        
        create_users_table_query = """
          CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          );
        """
        cursor.execute(create_users_table_query)
        connection.commit()
        print(f"Table users created successfully!")
      except psycopg2.Error as e:
        print(f"Error creating users table: {e}")
      finally:
        cursor.close()
        connection.close()
  
  @classmethod
  def create_employees_table(cls):
    connection = cls.get_connection()
    if connection:
      try:
        cursor = connection.cursor()

        create_employee_table_query = """
        CREATE TABLE IF NOT EXISTS employee (
          id SERIAL PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          phone VARCHAR(50) NOT NULL,
          role VARCHAR(50) NOT NULL,
          gender VARCHAR(10) NOT NULL,
          salary NUMERIC(10,2) NOT NULL 
        );
        """
        cursor.execute(create_employee_table_query)
        connection.commit()
      except psycopg2.Error as e:
        print(f"Error creating employee table: {e}")
      finally:
        cursor.close()
        connection.close()