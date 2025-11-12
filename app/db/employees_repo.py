from app.db.connection import get_conn

def add_employees(first_name, last_name, address, country, phone):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees(first_name, last_name, address, country, phone)" \
        "VALUES (%s, %s, %s, %s, %s)" \
        "RETURNING id",
        (first_name, last_name, address, country, phone)
    )    
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id


def get_all_employees():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM employees"        
    )
    all_data = cur.fetchall()
    cur.close()
    conn.close()
    return all_data

def get_employee_by_id(employees_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM employees WHERE id = %s",(employees_id,)        
    )
    emp_data = cur.fetchone()
    cur.close()
    conn.close()
    return emp_data

def update_employee(first_name, last_name, address, country, phone, employees_id,):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        (
        "UPDATE employees SET "
        "first_name = %s, "
        "last_name = %s, "
        "address = %s, "
        "country =%s, "
        "phone = %s "
        "WHERE id = %s"
        ),
        (first_name, last_name, address, country, phone, employees_id,)
         
    )
    conn.commit()
    cur.close()
    conn.close()
    return    

def delete_employee(employees_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM employees WHERE id = %s",(employees_id,)        
    )
    conn.commit()
    cur.close()
    conn.close()
    return

def phone_exists(phone):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM employees WHERE phone = %s", (phone,))
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count > 0