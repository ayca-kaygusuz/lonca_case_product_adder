# ©️ Ayça Kaygusuz 2024

import logging
from parser import ProductParser
from product_repository import ProductRepository
from config import DB_URI

def main():
    
    # customized logging so it prints the cleaner message without INFO:root and ERROR:root identifiers
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    # prompt for user to enter the XML path
    XML_FILE_PATH = input("Please enter the path to the XML file (Example: C:\Downloads): ")
    
    # Prompt user for the database URI
    # if blank, use default MongoDB URI mongodb://localhost:27017/
    custom_db_uri = input(f"Please enter the database URI or no input to use the default URI: {DB_URI}: ") or DB_URI
    
    product_repo = ProductRepository(custom_db_uri, 'lonca_scraper')

    try:
        products = ProductParser.parse_xml(XML_FILE_PATH)
        for product in products:
            product_repo.upsert_product(product)
        logging.info("All products processed and inserted/updated in MongoDB.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()