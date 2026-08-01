from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
import models

from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Welcome to Restaurant Management API"}


# RESTAURANT APIs

@app.post("/restaurants", response_model=schemas.RestaurantResponse)
def create_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return crud.create_restaurant(db, restaurant)


@app.get("/restaurants", response_model=list[schemas.RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurants(db)


@app.get("/restaurants/{restaurant_id}",
         response_model=schemas.RestaurantResponse)
def get_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):

    restaurant = crud.get_restaurant(db, restaurant_id)

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return restaurant


@app.put("/restaurants/{restaurant_id}",
         response_model=schemas.RestaurantResponse)
def update_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):

    updated = crud.update_restaurant(db, restaurant_id, restaurant)

    if not updated:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return updated


@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_restaurant(db, restaurant_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return {"message": "Restaurant deleted successfully"}

@app.get("/restaurants/address/{address}")
def address_restaurants(address: str, db: Session = Depends(get_db)):
    restaurant_list = crud.get_restaurant_by_address(db, address)

    if not restaurant_list:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return  restaurant_list