from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hiboutik_connector as HC

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174","http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"var":"value"}

@app.get("/customer/search")
def customer_search(last_name:str="", first_name:str="", email:str="", phone:str="", country:str="", vat:str=""):
    params = {"last_name":last_name, "first_name":first_name, "email":email, "phone":phone, "country":country, "vat":vat}
    params = [f"{key}={value}" for key,value in params.items() if value != ""] #* deletes empty params
    params_str = "&".join(params)
    customers = HC.get_customer(params_str)
    return {"customers":customers, "count":len(customers)}

@app.get("/sales/customer/{customer_id}")
def customer_search(customer_id:int, page:int=1):
    return HC.get_customer_sales(customer_id, page)