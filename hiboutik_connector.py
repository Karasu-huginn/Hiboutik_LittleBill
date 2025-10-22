import base64
import requests
import json

with open("creds.json", "r") as file:
    creds = json.loads(file.read())

API_URL = f"https://{creds["account"]}.hiboutik.com/api"

def gen_token():
    string = f"{creds["api_login"]}:{creds["api_key"]}"
    string_bytes = string.encode("ascii")
    b64_b = base64.b64encode(string_bytes)
    b64_str = b64_b.decode("ascii")
    return b64_str

def get_customer_sales(customer_id):
    token = gen_token()
    url = f"{API_URL}/sales/search?customer_id={customer_id}"
    headers = {"Accept": "*/*", "Authorization": "Basic "+token}
    sales = requests.get(url, headers=headers)
    return sales.json()

def get_customer(params):
    token = gen_token()
    url = f"{API_URL}/customers/search?{params}"
    print(url)
    headers = {"Accept": "*/*", "Authorization": "Basic "+token}
    customers = requests.get(url, headers=headers)
    return customers.json()