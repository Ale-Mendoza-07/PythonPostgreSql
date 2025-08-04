from sqlalchemy import Column, Integer, String, Numeric, DateTime
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2))
    stock = Column(Integer)
    category = Column(String)
    created_at = Column(DateTime)
