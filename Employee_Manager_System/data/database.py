import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
  BASE_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT',5432))
  }

  @classmethod
  def get_connection(cls, user=None, password=None):
    if not user or not password:
      raise ValueError("User and Password are required.")
    
    config = cls.BASE_CONFIG.copy()
    config['user'] = user
    config['password'] = password

    try:
      connection = psycopg2.connect(**config)
      return connection
    except psycopg2.Error as e:
      print(f"Error connecting to database: {e}")
      raise e