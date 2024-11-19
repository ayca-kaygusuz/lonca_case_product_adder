© 2024 Ayça Kaygusuz

```markdown
# Lonca Case Product Adder

## Overview
This project is a case study application designed for parsing a given XML file and transforming it into product data stored in MongoDB. The application allows users to specify the XML file path and the database URI, defaulting to `mongodb://localhost:27017/` if not provided.

## Features
- Parse XML files in a specified format.
- Store product data in a MongoDB database.
- Upsert functionality: update existing products or insert new ones.
- User-friendly prompts for file paths and database URIs.

## Requirements
- Python 3.6 or higher
- MongoDB
- Required Python packages:
  - `pymongo`

## Installation
1. **Clone the repository**:

   ```bash
   git clone https://github.com/ayca-kaygusuz/lonca_case_product_adder.git
   cd lonca_case_product_adder
   ```

2. **Install the required packages**:
   You can install the required packages using pip:

   ```bash
   pip install pymongo
   ```

3. **Set up MongoDB**:
   Make sure you have MongoDB running on your local machine or provide a custom URI to connect to a remote instance.

## Usage
1. **Run the application**:
   Execute the main script:

   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   - Enter the path to the XML file when prompted. (The path format is with backslashes and without quoation marks.)
   - Optionally, enter a custom MongoDB URI or press Enter to use the default value.

## XML File Format
The application expects the XML file to be structured in a specific format. Below is a generalized example structure that includes CDATA sections:

```xml
<Products>
    <Product ProductId="PRODUCT_ID" Name="PRODUCT_NAME">
        <Images>
            <Image Path="IMAGE_URL_1"></Image>
            <Image Path="IMAGE_URL_2"></Image>
            <Image Path="IMAGE_URL_3"></Image>
        </Images>
        <ProductDetails>
            <ProductDetail Name="Price" Value="PRODUCT_PRICE"/>
            <ProductDetail Name="DiscountedPrice" Value="PRODUCT_DISCOUNTED_PRICE"/>
            <ProductDetail Name="ProductType" Value="PRODUCT_TYPE"/>
            <ProductDetail Name="Quantity" Value="PRODUCT_QUANTITY"/>
            <ProductDetail Name="Color" Value="PRODUCT_COLOR"/>
            <ProductDetail Name="Series" Value="PRODUCT_SERIES"/>
            <ProductDetail Name="Season" Value="PRODUCT_SEASON"/>
        </ProductDetails>
        <!-- Optional additional Description CDATA Format: -->
        <Description>
            <![CDATA[<ul>
                <li><strong>Product Information:</strong> DESCRIPTION_TEXT</li>
                <li><strong>Fabric Information:</strong> FABRIC_DETAILS</li>
                <li><strong>Product Measurements:</strong> MEASUREMENTS_TEXT</li>
                <li><strong>Model Measurements:</strong> MODEL_MEASUREMENTS_TEXT</li>
                <li>Model is wearing size SIZE_INFO.</li>
                <li>Sizes may vary +/- tolerance.</li>
            </ul>]]>
        </Description>
    </Product>
    <!-- Repeat for more products -->
</Products>
```
## License
This project is licensed under the [GPL-2.0 License](LICENSE). In brief, this licence lets people do almost anything they want with this project, except distributing closed source versions. For further details, please read the license itself. 

## Contact
For questions or feedback, if you already don't have my other personal contact info, you may contact me through LinkedIn, which is linked through my github profile, and also registered with the same name.

© 2024 Ayça Kaygusuz