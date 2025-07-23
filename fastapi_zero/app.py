from http import HTTPStatus
from fastapi import FastAPI
from fastapi_zero.schemas import Message
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/exercicio-HTML', response_class=HTMLResponse)
def exercicio_html():
    return """
    <html>
        <head>
            <title>Exercício HTML</title>
        </head>
        <body>
            <h1>Ola Mundo</h1>
        </body>
    </html>
    """