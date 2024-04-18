from fastapi import FastAPI
import logging

from database import create_connection, create_table
from models import Employee

# define file to store log
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# create instalnce of Fast API application
app = FastAPI()

# create database connection
conn = create_connection()


@app.get('/api/')
def root():
    """
    This route gives information about this API service.
    """
    return {'message': 'Hello! This is employee record management service.'}


@app.on_event("startup")
async def startup_event():
    logging.info('Server Started')
    create_table(connection=conn)
    logging.info('Database initiated.')


@app.post("/employees")
async def add_employee_record(employee: Employee):
    """
    This route adds a new employee record to the database.
    """
    # Generate a new UUID for the employee ID
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO employees (id, name, department) VALUES (?, ?, ?)
                   """,
                   (str(employee.id), employee.name, employee.department))
    conn.commit()

    logging.info('New record added')
    return {"message": "Employee added successfully!", "employee": employee}


@app.get("/employees/")
async def get_employee_record():
    """
    This route retrieves all records of employee from database.
    """
    # Prepare and execute the SELECT query
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM employees
                   """)

    # Fetch the employee data (if any)
    employee_data = cursor.fetchall()

    return {"data": employee_data}


@app.get("/employees/{employee_id}")
async def get_single_employee_record(employee_id: str):
    """
    This route retrieves an employee based on employee id from database.
    """
    # Prepare and execute the SELECT query
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM employees WHERE id = ?
                   """,
                   (employee_id,))

    # Fetch the employee data (if any)
    employee_data = cursor.fetchone()

    # Check if employee exists and return appropriate response
    if employee_data:
        return {"data": employee_data}

    return {"error": 'Employee record not found'}
