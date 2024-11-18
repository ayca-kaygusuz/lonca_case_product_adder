import logging
from parser import ProductParser
from product_repository import ProductRepository
from config import DB_URI, XML_FILE_PATH

def main():
    logging.basicConfig(level=logging.INFO)
    
    product_repo = ProductRepository(DB_URI, 'lonca_scraper')

    try:
        products = ProductParser.parse_xml(XML_FILE_PATH)
        for product in products:
            product_repo.upsert_product(product)
        logging.info("All products processed and inserted/updated in MongoDB.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()