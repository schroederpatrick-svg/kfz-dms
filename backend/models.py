from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


# ----------------------------------
# Kunden
# ----------------------------------
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    street = Column(String)
    city = Column(String)
    phone = Column(String)
    email = Column(String)

    vehicles = relationship("Vehicle", back_populates="owner")


# ----------------------------------
# Fahrzeuge
# ----------------------------------
class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    manufacturer = Column(String)
    model = Column(String)
    license_plate = Column(String, index=True)
    vin = Column(String)

    owner = relationship("Customer", back_populates="vehicles")
    orders = relationship("Order", back_populates="vehicle")


# ----------------------------------
# Artikel (Warenwirtschaft)
# ----------------------------------
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price_net = Column(Float, nullable=False)
    vat_rate = Column(Float, default=19.0)
    stock = Column(Integer, default=0)

    order_items = relationship("OrderItem", back_populates="article")


# ----------------------------------
# Aufträge
# ----------------------------------
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    description = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer")
    vehicle = relationship("Vehicle", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    invoice = relationship("Invoice", back_populates="order", uselist=False)


# ----------------------------------
# Auftragspositionen
# ----------------------------------
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    quantity = Column(Integer, default=1)

    order = relationship("Order", back_populates="items")
    article = relationship("Article", back_populates="order_items")


# ----------------------------------
# Rechnungen
# ----------------------------------
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    date_issued = Column(DateTime, default=datetime.utcnow)
    total_net = Column(Float)
    total_vat = Column(Float)
    total_gross = Column(Float)

    order = relationship("Order", back_populates="invoice")
