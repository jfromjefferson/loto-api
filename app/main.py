from fastapi import FastAPI
from routers.lotofacil import lotofacil_router

app = FastAPI(
    contact={
        "name": "Jefferson Silva",
        "url": "https://github.com/jfromjefferson",
        "email": "jeffsilva1@outlook.com",
        "description": "Brazilian lottery number generator API"
        "Developed by: @jfromjefferson"
    },
    root_path='/api',
    summary="Brazilian lottery number generator API",
)


@app.get('/')
async def main():
    return {
        'message': 'Hi'
    }


app.include_router(lotofacil_router, tags=["lotofacil"])

