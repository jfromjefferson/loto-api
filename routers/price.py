from typing import Union

from fastapi import APIRouter, HTTPException

from utils.calculator import Calculator

price_router = APIRouter()


@price_router.get("/price")
def price(game_id: int = 1, game_count: int = 1):
    """
    1 - Lotofácil
    """
    if game_id != 1:
        raise HTTPException(status_code=400, detail="Invalid game id")

    calculator = Calculator(game_id=game_id, game_count=game_count)

    return {"price": calculator.calculate()}
