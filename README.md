# shopSmart-mini-shopping-website-dc
It is a small shopping website build using docker-compose

Folder Structure :

shopsmart/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── config.py
│   ├── seed.py
│   └── requirements.txt
│
├── frontend/
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── api.js
│       ├── pages/
│       │   ├── ProductsPage.js
│       │   └── CartPage.js
│       ├── components/
│       │   ├── ProductCard.js
│       │   └── Navbar.js
│
└── README.md

🔥 Features
Frontend (React)

✔ Browse products
✔ View product details
✔ Add to cart
✔ Remove from cart
✔ Cart total updates dynamically

Backend (Flask)

✔ Products API
✔ Cart API
✔ PostgreSQL integration

Database (PostgreSQL)

✔ products table
✔ cart_items table



#need to run once we up the docker compose
❯ docker exec -it shopsmart-mini-shopping-website-dc-backend-1 python seed.py
✅ Database seeded with products!