# ©️ Ayça Kaygusuz 2024

from pymongo import MongoClient
from datetime import datetime

class ProductRepository:
    def __init__(self, db_uri, db_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['products']

    def upsert_product(self, product):
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
            'createdAt': product.created_at,
            'updatedAt': datetime.now()  # Update timestamp on every upsert
        }

        # Upsert logic: Check if the product exists
        existing_product = self.collection.find_one({'stock_code': product.stock_code})
        if existing_product:
            # Update the existing product
            self.collection.update_one({'stock_code': product.stock_code}, {'$set': product_data})
        else:
            # Insert new product
            product_data['createdAt'] = datetime.now()
            self.collection.insert_one(product_data)