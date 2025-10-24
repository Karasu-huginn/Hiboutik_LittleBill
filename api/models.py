from sqlalchemy import Column, ForeignKey, Integer, String
from db import Base

class Customers(Base):
    __tablename__ = "customers"

    customers_id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, index=True)
    first_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    country = Column(String, index=True)
    vat = Column(String, index=True)

class Sales(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.customers_id"))
    billing_address = Column(Integer)
    shipping_address = Column(Integer)
    payment = Column(String)
    ext_ref = Column(String)
    store_id = Column(Integer)
    takeaway = Column(Integer)
    resource_id = Column(Integer)
    currency = Column(String)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)