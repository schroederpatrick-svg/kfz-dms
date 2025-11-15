from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# ===== Kunden =====
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)

    vehicles = relationship("Vehicle", back_populates="owner")
    orders = relationship("Order", back_populates="customer")

# ===== Fahrzeuge =====
class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    license_plate = Column(String, unique=True)
    model = Column(String)
    
    owner = relationship("Customer", back_populates="vehicles")
    orders = relationship("Order", back_populates="vehicle")

# ===== Artikel =====
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price_net = Column(Float)
    vat_rate = Column(Float, default=19.0)

    order_items = relationship("OrderItem", back_populates="article")

# ===== Aufträge =====
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    description = Column(String, nullable=True)

    customer = relationship("Customer", back_populates="orders")
    vehicle = relationship("Vehicle", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

# ===== Order Items =====
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    article = relationship("Article", back_populates="order_items")

