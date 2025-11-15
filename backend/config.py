import os

class Config:
    DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@db:5432/shopdb"
    )

