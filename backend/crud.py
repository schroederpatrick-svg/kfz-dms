from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# ----------------------------------
# Kunden
# ----------------------------------
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session):
    return db.query(models.Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()


# ----------------------------------
# Artikel
# ----------------------------------
def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_articles(db: Session):
    return db.query(models.Article).all()


# ----------------------------------
# Aufträge
# ----------------------------------
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        customer_id=order.customer_id,
        vehicle_id=order.vehicle_id,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_item = models.OrderItem(
            order_id=db_order.id,
            article_id=item.article_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(models.Order).all()


# ----------------------------------
# Rechnungen
# ----------------------------------
def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    order = db.query(models.Order).filter(models.Order.id == invoice.order_id).first()
    if not order:
        raise ValueError("Auftrag existiert nicht")

    total_net = sum(item.quantity * item.article.price_net for item in order.items)
    total_vat = total_net * 0.19  # 19% MwSt
    total_gross = total_net + total_vat

    db_invoice = models.Invoice(
        order_id=order.id,
        date_issued=datetime.utcnow(),
        total_net=total_net,
        total_vat=total_vat,
        total_gross=total_gross
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice
