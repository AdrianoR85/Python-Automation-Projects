from data.database import DatabaseConfig

class AuthUser:
  @staticmethod
  def login(username, password):
    try:
      conn = DatabaseConfig.get_connection(username, password)
      return conn
    except Exception:
      return False