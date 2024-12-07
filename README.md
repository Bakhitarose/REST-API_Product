# REST-API_Product

## Overview
This project is a simple REST API for managing a collection of products. It provides endpoints to create and read products that has a name, description and price.

## Actions 
- Create a new product
- Retrieve a list of all products
- handle the requests

## Setting Up
Create a virtual environment:
 ```bash
python -m venv .venv
```

Activate the virtual environment:
In Powershell,
 ```bash
 .\.venv\Scripts\Activate.ps1
```

Install dependency:
```bash
pip install requests uvicorn fastapi
```

Create project directory:
```bash
mkdir project_resource
cd product_resource
```

Create application:
```bash
mkdir product
cd product
```
```python
from fastapi import FastAPI
#from product.routes import product_routes

product = FastAPI()

product.include_router(product_routes.router)

# Entry endpoint
@product.get("/")  
async def root():  
    return {"message": "Welcome to the FastAPI Product API"}
```

Run the Server:
```bash
uvicorn main:product --reload
```

