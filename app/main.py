from fastapi import FastAPI
app = FastAPI()


@app.get('/api/')
def root():
    """
    This route gives information about this API service.
    """
    return {'message': 'Hello! This is employee record management service.'}
