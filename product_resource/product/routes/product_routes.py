from fastapi import APIRouter, HTTPException, status  
from services.product_service import (  
    get_products,  
    create_product,  
    ProductResponse  
)  

router = APIRouter()  

@router.get("/products/", response_model=list[ProductResponse])  
def read_products():  
    """Retrieve a list of all products."""  
    return get_products()  

@router.post("/products/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)  
def create_product_route(new_product: ProductResponse):  
    """Accept a JSON object to create a new product."""  
    try:  
        return create_product(new_product)  
    except Exception as e:  
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))  


