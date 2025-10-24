import base64
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_URL = f"https://{os.getenv("ACCOUNT")}.hiboutik.com/api"

def gen_token():
    string = f"{os.getenv("API_LOGIN")}:{os.getenv("API_KEY")}"
    string_bytes = string.encode("ascii")
    b64_b = base64.b64encode(string_bytes)
    b64_str = b64_b.decode("ascii")
    return b64_str

def get_customer_sales(customer_id, page):
    page += 1
    token = gen_token()
    headers = {"Accept": "*/*", "Authorization": "Basic "+token}
    url = f"{API_URL}/sales/search?customer_id={customer_id}&p={page}"
    sales = requests.get(url, headers=headers)
    return sales.json()

def get_customer(params):
    token = gen_token()
    headers = {"Accept": "*/*", "Authorization": "Basic "+token}
    url = f"{API_URL}/customers/search?{params}"
    customers = requests.get(url, headers=headers)
    return customers.json()