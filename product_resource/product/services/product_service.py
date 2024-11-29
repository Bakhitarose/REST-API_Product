from product.schemas.product_schema import ProductResponse
from typing import List, Dict

REST_PRODUCT_URL = "/product/"

product_db: Dict[int, ProductResponse] = {}  

def get_products() -> List[ProductResponse]:  
    """Retrieve all products."""  
    return list(product_db.values())  

def create_product(new_product: ProductResponse) -> ProductResponse:  
    """Create a new product."""  
    # Automatically assign an ID (incremental)  
    product_id = max(product_db.keys(), default=0) + 1  
    new_product_with_id = new_product.copy(update={"id": product_id})  
    product_db[product_id] = new_product_with_id  
    return new_product_with_id  