# Ajio Product Scraper

This project is a web scraper built in Python to extract product data from the Ajio website (https://www.ajio.com). The scraper retrieves information such     as product name, brand name, price, coupon status, code, and product link. The extracted data is then stored in a CSV file for further analysis.

## Prerequisites

To run this scraper, make sure you have the following installed:

    Python 3.x
    requests library
    pandas library

## Installation

    Clone the repository:

git clone https://github.com/CodeWithZalak/ajio-product-scraper.git

Install the required libraries:

    pip install requests pandas

## Usage

Open the terminal and navigate to the project directory.
Run the following command to start the data scraping process:

    python ajio_scraper.py

 The scraper will start fetching data from the Ajio website. It will scrape multiple pages and extract product details.
 Once the scraping process is complete, the data will be saved in a CSV file named AJIO_product_details.csv.
 You can then use the CSV file for further analysis, data visualization, or any other purpose.

## License

This project is licensed under the MIT License.
## Acknowledgements

This project utilizes the requests library for making HTTP requests and the pandas library for data manipulation and storage.
The scraping process is designed specifically for the Ajio website and may not work with other websites.
