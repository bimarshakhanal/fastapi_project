## Fast API project

This project demonstrates a robust FastAPI application for managing employee data using a SQLite database. It enables CRUD (Create, Read, Update, Delete) operations on employee records, providing a solid foundation for building user-friendly employee management systems.

### Steps to setup this app
1. Clone this repo  
```git clone https://github.com/bimarshakhanal/fastapi_project.git```

2. Create and activate virtual enviroment
    ```
    python -m virtualenv .venv
    source .venv/bin/activate
    ```
3. Install required libraries  
    ```pip install -r requirements.txt```

4. Start FastAPI application
    ```
    cd app
    uvicorn main:app --reload
    ```

### Dockerize this application
1. Create docker image  
    ```
    docker build -t <image_name> .
    ```
2. Run dockerized application
    ```
    docker run -d --name <container_name> -p 80:<local_machine_port> <image_name> 
    ```
