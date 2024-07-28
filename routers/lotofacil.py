from typing import Union

from fastapi import APIRouter, HTTPException, Query

from utils.generator import Generator

lotofacil_router = APIRouter()


@lotofacil_router.get("/lotofacil/random")
async def lotofacil_random(game_count: Union[int, None] = 1):
    if game_count < 1 or game_count > 50:
        raise HTTPException(status_code=400, detail="Game count must be greater than 0 and less or equal to 50")

    generator = Generator()

    try:
        game_dict_list = [
            {
                "game": count + 1,
                "numbers": results[0],
                "mirror": results[1]
            }
            for count in range(game_count)
            for results in [generator.generate_random_numbers()]
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return game_dict_list


@lotofacil_router.get("/lotofacil/chose-5")
def lotofacil_chose_5_numbers(game_count: Union[int, None] = 1, numbers: list[int] = Query(...)):
    if len(numbers) < 5 or len(numbers) > 5:
        raise HTTPException(status_code=400, detail="Numbers count must be equal to 5")

    if game_count < 1 or game_count > 50:
        raise HTTPException(status_code=400, detail="Game count must be greater than 0 and less or equal to 50")

    generator = Generator()

    try:
        game_dict_list = [
            {
                "game": count + 1,
                "numbers": results[0],
                "mirror": results[1]
            }
            for count in range(game_count)
            for results in [generator.generate_random_numbers_10(choices=numbers)]
        ]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return game_dict_list
