from data.models import Employee

class EmployeeService:

  @staticmethod
  def add_employee(employee: Employee, conn):
    sql = """
      INSERT INTO employee (name, phone, role, gender, salary)
      VALUES (%s,%s,%s,%s,%s)
      RETURNING id;
    """
    cursor = conn.cursor()
    cursor.execute(sql, employee.to_tuple_insert())
    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return new_id
  
  @staticmethod
  def list_employee(conn):
    sql = "SELECT id, name, phone, role, gender, salary FROM employee;"
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows
  
  @staticmethod
  def update_employee(conn):
    sql = """
      UPDATE employee
      SET name=%s, phone=%s, role=%s, gender=%s, salary=%s
      WHERE id=%s
    """
    cursor = conn.cursor()
    cursor.execute(sql, Employee.to_tuple_update)
    conn.commit()
    cursor.close()
  
  @staticmethod
  def delete_employee(emp_id: int, conn):
    sql = "DELETE FROM employee WHERE id=%s"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()