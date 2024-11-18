# ©️ Ayça Kaygusuz 2024

import xml.etree.ElementTree as ET
import re
from datetime import datetime
from product import Product

class ProductParser:
    @staticmethod
    def extract_details(description):
        clean_description = description.strip()
        fabric_match = re.search(r'Kumaş Bilgisi:</strong>\s*(.*?)</li>', clean_description)
        fabric = fabric_match.group(1).strip() if fabric_match else 'Unknown'
        
        product_measurements_match = re.search(r'Ürün Ölçüleri1?:</strong>\s*(.*?)</li>', clean_description)
        product_measurements = product_measurements_match.group(1).strip().replace('&nbsp;', ' ').strip() if product_measurements_match else 'N/A'
        
        sample_size_match = re.search(r'Modelin üzerindeki ürün <strong>(.+?)</strong>', clean_description)
        sample_size = sample_size_match.group(1).strip() if sample_size_match else 'N/A'
        
        model_measurements_match = re.search(r'Model Ölçüleri:</strong>\s*(.*?)</li>', clean_description)
        model_measurements = model_measurements_match.group(1).strip().replace('&nbsp;', ' ').strip() if model_measurements_match else 'N/A'
        
        return fabric, product_measurements, sample_size, model_measurements

    @staticmethod
    def parse_xml(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        products = []

        for product_elem in root.findall('Product'):
            stock_code = product_elem.get('ProductId')
            name = product_elem.get('Name').capitalize()
            images = [image.get('Path') for image in product_elem.findall('.//Image')]

            details = {detail.get('Name'): detail.get('Value') for detail in product_elem.findall('.//ProductDetail')}
            description = product_elem.find('Description').text
            fabric, product_measurements, sample_size, model_measurements = ProductParser.extract_details(description)

            product = Product(
                stock_code=stock_code,
                name=name,
                color=[details.get('Color', '').capitalize()],
                price=float(details.get('Price', '0').replace(',', '.')),
                discounted_price=float(details.get('DiscountedPrice', '0').replace(',', '.')),
                images=images,
                quantity=int(details.get('Quantity', '0')),
                fabric=fabric,
                product_measurements=product_measurements,
                model_measurements=model_measurements,
                sample_size=sample_size,
                series=details.get('Series', ''),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            products.append(product)

        return products