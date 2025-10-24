from sqlalchemy import Column, ForeignKey, Integer, String
from db import Base

class Customers(Base):
    __tablename__ = "customers"

    customers_id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, index=True, nullable=True)
    first_name = Column(String, index=True, nullable=True)
    email = Column(String, index=True, nullable=True)
    phone = Column(String, index=True, nullable=True)
    country = Column(String, index=True, nullable=True)
    vat = Column(String, index=True, nullable=True)

class Sales(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.customers_id"), nullable=True)
    billing_address = Column(Integer, nullable=True)
    shipping_address = Column(Integer, nullable=True)
    payment = Column(String, nullable=True)
    ext_ref = Column(String, nullable=True)
    store_id = Column(Integer, nullable=True)
    takeaway = Column(Integer, nullable=True)
    resource_id = Column(Integer, nullable=True)
    currency = Column(String, nullable=True)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)