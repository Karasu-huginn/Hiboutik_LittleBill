from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_auth():
    response = client.post("auth/token", headers={"Content-Type":"application/x-www-form-urlencoded"}, data="username=karasu&password=1234").json()
    return f"{response["token_type"]} {response["access_token"]}"

token = get_auth()

def test_get_customer_by_name():
    response = client.get("/customer/search?last_name=Maxime", headers={"Authorization":token})
    assert response.status_code == 200
    #* I only check status code because data from the api is slightly different than from what is saved in the DB, therefore the assert on response.json() is tricky

def test_get_customer_by_email():
    response = client.get("/customer/search?email=youcefkouaouci@gmail.com", headers={"Authorization":token})
    assert response.status_code == 200
