from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)


app = FastAPI()
items: dict[int, Item] = {}


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="Item ID does not match URL")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None
