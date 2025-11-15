from db import SessionLocal
from models import Product

session = SessionLocal()

products = [
    Product(
        name="iPhone 15",
        price=1200,
        description="Latest Apple iPhone",
        image="https://via.placeholder.com/200?text=iPhone+15"
    ),
    Product(
        name="Samsung Galaxy S24",
        price=1100,
        description="Flagship Samsung Phone",
        image="https://via.placeholder.com/200?text=Galaxy+S24"
    ),
    Product(
        name="Sony Headphones",
        price=250,
        description="Noise Cancelling Headphones",
        image="https://via.placeholder.com/200?text=Sony+Headphones"
    ),
    Product(
        name="MacBook Air M3",
        price=1600,
        description="Latest MacBook Air with M3 chip",
        image="https://via.placeholder.com/200?text=MacBook+Air+M3"
    ),
]

session.add_all(products)
session.commit()
session.close()

print("✅ Database seeded with products!")