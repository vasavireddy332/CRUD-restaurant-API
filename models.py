from sqlalchemy import Column, Integer, String
from database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String(150), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=False)
    city = Column(String(100), unique=True, nullable=True)