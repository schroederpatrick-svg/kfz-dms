from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KFZ-DMS Backend")

# CORS für das Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------
# Test-Endpoint
# ------------------------------------
@app.get("/")
def home():
    return {"message": "KFZ-DMS Backend läuft!"}


# ------------------------------------
# Kunden (CRUD)
# ------------------------------------
@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)


@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)


@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_customer(db, customer_id)


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    crud.delete_customer(db, customer_id)
    return {"message": "Kunde gelöscht"}


# ------------------------------------
# Artikel (Warenwirtschaft)
# ------------------------------------
@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db, article)


@app.get("/articles/", response_model=list[schemas.Article])
def read_articles(db: Session = Depends(get_db)):
    return crud.get_articles(db)


# ------------------------------------
# Aufträge
# ------------------------------------
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@app.get("/orders/", response_model=list[schemas.Order])
def read_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)


# ------------------------------------
# Rechnungen
# ------------------------------------
@app.post("/invoices/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice)
