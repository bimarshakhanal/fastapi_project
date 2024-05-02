# use python 3.9 image 
FROM python:3.9

# define workdir inside container 
WORKDIR /code

# copy requirements to container
COPY ./requirements.txt /code/requirements.txt

# install requirements in container
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy source code to container
COPY . /code/

# change working directory ( to make relative imports work)
WORKDIR /code/app

# command to start fastapi application 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]