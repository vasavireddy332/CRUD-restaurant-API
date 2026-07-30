from sqlalchemy.orm import Session
import models
import schemas


def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()


def get_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()


def update_restaurant(
    db: Session,
    restaurant_id: int,
    restaurant: schemas.RestaurantCreate
):
    db_restaurant = get_restaurant(db, restaurant_id)

    if not db_restaurant:
        return None

    db_restaurant.restaurant_name = restaurant.restaurant_name
    db_restaurant.address = restaurant.address
    db_restaurant.city = restaurant.city
    db_restaurant.phone_number = restaurant.phone_number
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def delete_restaurant(db: Session, restaurant_id: int):
    db_restaurant = get_restaurant(db, restaurant_id)
    if not db_restaurant:
        return None
    db.delete(db_restaurant)
    db.commit()

    return db_restaurant