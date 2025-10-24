from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, index=True)
    first_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    country = Column(String, index=True)
    vat = Column(String, index=True)

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    billing_address = Column(Integer, index=True)
    shipping_address = Column(Integer, index=True)
    payment = Column(String, index=True)
    ext_ref = Column(String, index=True)
    store_id = Column(Integer, index=True)
    takeaway = Column(Integer, index=True)
    resource_id = Column(Integer, index=True)
    currency = Column(String, index=True)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)