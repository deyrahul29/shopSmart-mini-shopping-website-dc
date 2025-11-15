from flask import Flask, jsonify, request
from flask_cors import CORS
from db import SessionLocal, engine
from models import Base, Product

app = Flask(__name__)
CORS(app)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}, 200

@app.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "image": p.image
        }
        for p in products
    ])

@app.get("/products/<int:id>")
def get_product(id):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()
    db.close()

    if not product:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "image": product.image
    })

@app.post("/cart")
def add_to_cart():
    data = request.json
    print("ADD TO CART:", data)
    return {"message": "Added to cart"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
@app.get("/health")
def health():
    return {"status": "ok"}
