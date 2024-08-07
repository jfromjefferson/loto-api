from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from routers.lotofacil import lotofacil_router
from routers.price import price_router

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=['3/seconds'],
    storage_uri="memory://"  # Can be redis://[password]@localhost:6379/0
)
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
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.get('/')
async def main():
    return {
        'message': 'Hi'
    }


app.include_router(price_router, tags=["price"])
app.include_router(lotofacil_router, tags=["lotofacil"])

