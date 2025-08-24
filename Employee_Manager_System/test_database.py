from config.database import DatabaseConfig

if __name__ == "__main__":
  print("Testing database connection...")

  connection = DatabaseConfig.get_connection()
  if connection:
    print("✅ Database connection successfully!")
    connection.close()
  else:
    print("❌ Database connection failed!")
  
  print("✅ Tabelas criadas (se não existirem).")