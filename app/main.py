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
