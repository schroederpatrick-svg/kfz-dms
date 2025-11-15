from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

# ===== Datenbank-Setup =====
Base.metadata.create_all(bind=engine)

app = FastAPI(title="KFZ Werkstatt DMS API")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ===== Dependency =====
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ===== Kunden Endpoints =====
@app.get("/api/customers", response_model=list[schemas.Customer])
def read_customers(db: Session = next(get_db())):
    return db.query(models.Customer).all()

@app.post("/api/customers", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = next(get_db())):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.delete("/api/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = next(get_db())):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted"}

# ===== Artikel Endpoints =====
@app.get("/api/articles", response_model=list[schemas.Article])
def read_articles(db: Session = next(get_db())):
    return db.query(models.Article).all()

@app.post("/api/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = next(get_db())):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# ===== Aufträge Endpoints =====
@app.get("/api/orders", response_model=list[schemas.Order])
def read_orders(db: Session = next(get_db())):
    return db.query(models.Order).all()

@app.post("/api/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = next(get_db())):
    db_order = models.Order(
        customer_id=order.customer_id,
        vehicle_id=order.vehicle_id,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Order Items
    for item in order.items:
        db_item = models.OrderItem(
            order_id=db_order.id,
            article_id=item.article_id,
            quantity=item.quantity
        )
        db.add(db_item)
    db.commit()
    return db_order

# ===== Rechnungen Endpoints =====
@app.get("/api/invoices")
def read_invoices(db: Session = next(get_db())):
    invoices = []
    orders = db.query(models.Order).all()
    for o in orders:
        total = sum([item.article.price_net * item.quantity * (1 + item.article.vat_rate / 100) for item in o.items])
        invoices.append({
            "id": o.id,
            "order_id": o.id,
            "customer": o.customer,
            "total": total
        })
    return invoices

# PDF-Download Endpoint (Dummy, später mit ReportLab o.ä. generieren)
@app.get("/api/invoices/{invoice_id}/pdf")
def download_invoice(invoice_id: int):
    from fastapi.responses import FileResponse
    return FileResponse("backend/sample_invoice.pdf", media_type="application/pdf", filename=f"invoice_{invoice_id}.pdf")
