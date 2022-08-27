from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'key': 'Hello!'}  #'Hello!'


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {'key': pk, 'q': q}


@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


