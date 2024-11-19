# ©️ Ayça Kaygusuz 2024

from pymongo import MongoClient
from datetime import datetime

class ProductRepository:
    def __init__(self, db_uri, db_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['products']

    def upsert_product(self, product):
        # Prepare the product data for the database
        product_data = {
            'stock_code': product.stock_code,
            'name': product.name,
            'color': product.color,
            'price': product.price,
            'discounted_price': product.discounted_price,
            'images': product.images,
            'quantity': product.quantity,
            'fabric': product.fabric,
            'product_measurements': product.product_measurements,
            'model_measurements': product.model_measurements,
            'sample_size': product.sample_size,
            'series': product.series,
            'updatedAt': datetime.now()  # Always update this timestamp
        }

        # Prepare the upsert query
        upsert_query = {
            'stock_code': product.stock_code
        }

        # Use $set to update fields, and set createdAt only if inserting
        self.collection.update_one(
            upsert_query,
            {
                '$set': product_data,
                '$setOnInsert': {
                    'createdAt': datetime.now()  # Only set this on insert
                }
            },
            upsert = True  # Perform insert if not found
        )