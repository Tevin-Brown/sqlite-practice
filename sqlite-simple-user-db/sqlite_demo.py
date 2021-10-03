import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:') # allows for in memory db (automatically give you a fresh DB every time)
# conn = sqlite3.connect('employee.db')

c = conn.cursor() # Allows for communication with the db

c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

def insert_emp(emp):
    with conn: # Allows us to ignore adding conn.commit to every function
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last':emp.last, 'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                    {'first': emp.first, 'last':emp.last})



emp_1 = Employee('Varun','Prasad', 80000)
emp_2 = Employee('Gino','Prasad', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Prasad')
print(emps)

remove_emp(emp_1)

emps = get_emps_by_name('Prasad')
print(emps)

conn.commit() # commits the current transaction

conn.close() # closes connection

# c.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay)) // DONT USE. SQL INJECTION

# Both of the following work
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# # c.execute("INSERT INTO employees VALUES ('Tevin', 'Brown', 107000)")
# # c.execute("INSERT INTO employees VALUES ('Ethan', 'Brown', 25000)")
# # conn.commit()



# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Brown'})
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Prasad'})
# print(c.fetchall())