import sqlite3

def connect_db():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Employee (
        ID TEXT PRIMARY KEY,
        Name TEXT,
        Age INTEGER,
        Salary REAL,
        Department TEXT
    )""")
    con.commit()
    return con

def add_employee(id, name, age, salary, dept):
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?)", (id, name, age, salary, dept))
        con.commit()
        return "Employee added successfully."
    except sqlite3.IntegrityError:
        return "Employee ID already exists."
    finally:
        con.close()

def update_employee(id, name, age, salary, dept):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""UPDATE Employee SET 
        Name=?, Age=?, Salary=?, Department=? WHERE ID=?""",
        (name, int(age), float(salary), dept, id))
    con.commit()
    con.close()
    return "Employee updated."

def delete_employee(id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM Employee WHERE ID=?", (id,))
    con.commit()
    con.close()
    return "Employee deleted."

def fetch_employees():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee ORDER BY ID ASC")
    rows = cur.fetchall()
    con.close()
    return rows
