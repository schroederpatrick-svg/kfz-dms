from pydantic import BaseModel
from typing import List, Optional

# ===== Kunden =====
class CustomerBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

# ===== Fahrzeuge =====
class VehicleBase(BaseModel):
    license_plate: str
    model: str

class VehicleCreate(VehicleBase):
    customer_id: int

class Vehicle(VehicleBase):
    id: int
    customer_id: int
    class Config:
        orm_mode = True

# ===== Artikel =====
class ArticleBase(BaseModel):
    name: str
    price_net: float
    vat_rate: float = 19.0

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    class Config:
        orm_mode = True

# ===== Order Items =====
class OrderItemBase(BaseModel):
    article_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    article: Article
    class Config:
        orm_mode = True

# ===== Aufträge =====
class OrderBase(BaseModel):
    customer_id: int
    vehicle_id: int
    description: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    id: int
    items: List[OrderItem]
    customer: Customer
    vehicle: Vehicle
    class Config:
        orm_mode = True
