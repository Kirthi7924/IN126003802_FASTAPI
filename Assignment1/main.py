from fastapi import FastAPI

app = FastAPI()

# Product data
products = [
    {"id": 1, "name": "Smartphone", "price": 18000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Coffee Mug", "price": 199, "category": "Kitchen", "in_stock": True},
    {"id": 3, "name": "Notebook", "price": 89, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Table Lamp", "price": 799, "category": "Home", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {
        "store": "Tech & Home Store",
        "product_count": len(products),
        "items": products
    }

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):

    result = [p for p in products if p["category"].lower() == category_name.lower()]

    if not result:
        return {"status": "No items available in this category"}

    return {
        "category": category_name,
        "items_found": len(result),
        "items": result
    }

@app.get("/products/instock")
def get_instock():

    available = [p for p in products if p["in_stock"]]

    return {
        "available_products": available,
        "available_count": len(available)
    }

@app.get("/store/summary")
def store_summary():

    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))

    return {
        "store": "Tech & Home Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "matches": results,
        "total_matches": len(results)
    }

@app.get("/products/deals")
def get_deals():

    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }