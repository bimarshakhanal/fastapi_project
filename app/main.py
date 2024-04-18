from fastapi import FastAPI
from database import create_connection, create_table
import logging

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
