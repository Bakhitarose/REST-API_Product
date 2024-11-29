from fastapi import FastAPI
from product.routes import product_routes

product = FastAPI()

product.include_router(product_routes.router)

# Entry endpoint
@product.get("/")  
async def root():  
    return {"message": "Welcome to the FastAPI Product API"}  