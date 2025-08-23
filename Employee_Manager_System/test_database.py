from config.database import DatabaseConfig

if __name__ == "__main__":
  print("Testing database connection...")

  connection = DatabaseConfig.get_connection()
  if connection:
    print("✅ Database connection successfully!")
    connection.close()

    print("Creating users table")
    DatabaseConfig.create_users_table()
  else:
    print("❌ Database connection failed!")