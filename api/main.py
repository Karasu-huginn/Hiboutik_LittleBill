from typing import Annotated, List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import or_
import hiboutik_connector as HC
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db, engine
import models
import auth

#* FastAPI Init
app = FastAPI()
app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174","http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#* DB ORM & dependencies
models.Base.metadata.create_all(bind=engine)
db_dep = Annotated[Session, Depends(get_db)]
user_dep = Annotated[dict, Depends(auth.get_current_user)]

class SaleBase(BaseModel):
    vendor_id:int
    billing_address:int
    shipping_address:int
    payment:str
    ext_ref:str
    store_id:int
    takeaway:int
    resource_id:int
    currency:str

class CustomerBase(BaseModel):
    last_name:str
    first_name:str
    email:str
    phone:str
    country:str
    vat:str
    sales:List[SaleBase]
    

#* FastAPI Routes
@app.get("/customer/search")
def customer_search(user:user_dep, db:db_dep, last_name:str="", first_name:str="", email:str="", phone:str="", country:str="", vat:str=""):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    customers = db.query(models.Customers).filter(or_(
        models.Customers.last_name==last_name,
        models.Customers.first_name==first_name, 
        models.Customers.email==email, 
        models.Customers.phone==phone, 
        models.Customers.country==country, 
        models.Customers.vat==vat
        )).all()
    # not optimal : perfect comparison instead of searching 

    if not customers:
        params = {"last_name":last_name, "first_name":first_name, "email":email, "phone":phone, "country":country, "vat":vat}
        params = [f"{key}={value}" for key,value in params.items() if value] #* deletes empty params
        params_str = "&".join(params)
        customers = HC.get_customer(params_str)
        for customer in customers:
            db_customer = models.Customers(
                customers_id=customer["customers_id"],
                last_name=customer["last_name"],
                first_name=customer["first_name"], 
                email=customer["email"], 
                phone=customer["phone"], 
                country=customer["country"], 
                vat=customer["vat"]
            )
            db.add(db_customer)
        db.commit()
    return {"customers":customers, "count":len(customers)}

@app.get("/sales/customer/{customer_id}")
def customer_sales(user:user_dep, customer_id:int, db: db_dep, page:int=0):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    sales = db.query(models.Sales).filter(models.Sales.customer_id == customer_id).all()
    if not sales:
        sales = HC.get_customer_sales(customer_id, page)
        for sale in sales:
            #todo handle foreign key not found error
            db_sale = models.Sales(
                sale_id=sale["sale_id"],
                vendor_id=sale["vendor_id"],
                customer_id=sale["customer_id"],
                billing_address=sale["billing_address"],
                shipping_address=sale["shipping_address"],
                payment=sale["payment"],
                ext_ref=sale["sale_ext_ref"],
                store_id=sale["store_id"],
                takeaway=sale["takeaway"],
                resource_id=sale["resource_id"],
                currency=sale["currency"]
            )
            db.add(db_sale)
        db.commit()
    return {"sales":sales[page*5:(page+1)*5], "count":len(sales), "page":page, "last_page":(page+1)*5>=len(sales)}
