from pydantic import BaseModel


class RestaurantCreate(BaseModel):
    restaurant_name: str
    address: str
    city: str | None = None
    phone_number: str


class RestaurantResponse(RestaurantCreate):
    id: int

    model_config = {
        "from_attributes": True
    }