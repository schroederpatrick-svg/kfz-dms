from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# ----------------------------------
# Kunden
# ----------------------------------
class CustomerBase(BaseModel):
    name: str
    street: Optional[str] = None
    city: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True


# ----------------------------------
# Fahrzeuge
# ----------------------------------
class VehicleBase(BaseModel):
    manufacturer: str
    model: str
    license_plate: str
    vin: Optional[str] = None

class VehicleCreate(VehicleBase):
    customer_id: int

class Vehicle(VehicleBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


# ----------------------------------
# Artikel
# ----------------------------------
class ArticleBase(BaseModel):
    name: str
    price_net: float
    vat_rate: Optional[float] = 19.0
    stock: Optional[int] = 0

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True


# ----------------------------------
# Aufträge
# ----------------------------------
class OrderItemBase(BaseModel):
    article_id: int
    quantity: int = 1

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    article: Article

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    customer_id: int
    vehicle_id: int
    description: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate] = []

class Order(OrderBase):
    id: int
    items: List[OrderItem] = []

    class Config:
        orm_mode = True


# ----------------------------------
# Rechnungen
# ----------------------------------
class InvoiceBase(BaseModel):
    order_id: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    date_issued: datetime
    total_net: float
    total_vat: float
    total_gross: float

    class Config:
        orm_mode = True
