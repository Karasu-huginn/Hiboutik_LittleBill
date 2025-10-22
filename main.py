from fastapi import FastAPI
import hiboutik_connector as HC

app = FastAPI()

@app.get('/')
def root():
    return {"var":"value"}

@app.get("/customer/search")
def customer_search(last_name:str="", first_name:str="", email:str="", phone:str="", country:str="", vat:str=""):
    params = {"last_name":last_name, "first_name":first_name, "email":email, "phone":phone, "country":country, "vat":vat}
    params = [f"{key}={value}" for key,value in params.items() if value != ""] #* deletes empty params
    params_str = "&".join(params)
    return HC.get_customer(params_str)