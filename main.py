from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Главная страница"}


@app.get("/torty/{tort_id}")
async def read_torty(torty_id: id, nametort: Union[str, None] = None):
    return {"torty_id": torty_id, "name_tort": nametort}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
