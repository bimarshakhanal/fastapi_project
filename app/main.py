'''Fast api application for employee management.'''
from contextlib import asynccontextmanager
from typing import Optional
import logging

from fastapi import FastAPI, HTTPException

from database import create_connection, create_table
from models import Employee

# define file to store log
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@asynccontextmanager
async def lifespan(app):
    '''Lifecycle function'''
    logging.info('Server Started')
    create_table(connection=conn)
    logging.info('Database initiated.')
    yield

# create instalnce of Fast API application
app = FastAPI(lifespan=lifespan)

# create database connection
conn = create_connection()


@app.get('/api/')
def root():
    """
    This route gives information about this API service.
    """
    return {'message': 'Hello! This is employee record management service.'}


@app.post("/api/employees/")
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


@app.get("/api/employees/")
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


@app.get("/api/employees/{employee_id}")
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
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/api/employees/{employee_id}")
async def delete_employee_record(employee_id: str):
    """
    This route deletes an employee record based on their ID from the database.
    """
    # Prepare and execute the DELETE query
    cursor = conn.cursor()
    cursor.execute("""
                   DELETE FROM employees WHERE id = ?
                   """,
                   (employee_id,))
    conn.commit()

    # Return a success message
    if cursor.rowcount:
        return {"message": "Employee deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/api/employees/{employee_id}/{column}/{new_value}")
async def update_employee_detail(
        employee_id: str, column: str, new_value: Optional[str] = None,):
    """
    This route updates a specific detail (column) of an employee record based on their ID.
    """
    # Validate input data (optional)
    # if column not in ("name", "department"):
    #   return {"message": "Invalid column name"}

    # Prepare and execute the UPDATE query
    cursor = conn.cursor()
    # Use parameter substitution to prevent SQL injection vulnerabilities
    cursor.execute(f"""
                   UPDATE employees SET {column} = ? WHERE id = ?
                   """,
                   (new_value, employee_id),
                   )
    conn.commit()

    # Check if employee exists and return appropriate response
    if cursor.rowcount:
        return {"message": "Employee detail updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
