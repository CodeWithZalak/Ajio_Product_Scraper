import requests
import pandas as pd

class Ajio_scraper():
    def __init__(self):
        self.product_data = []

    def data_scrape(self):
        
        for i in range(1,35):
            url = f"https://www.ajio.com/api/category/830202001?fields=SITE&currentPage={i}&pageSize=45&format=json&query=:relevance&sortBy=relevance&gridColumns=3&advfilter=true&platform=Desktop&showAdsOnNextPage=false&is_ads_enable_plp=true&displayRatings=true"
            req = requests.get(url)
            response = req.json()
            if "products" in response:
                items = response["products"]

            for item in items:
                name = item["name"]
                brand_name = item['brandTypeName']
                price = item["price"]["value"]
                couponStatus = item["couponStatus"]
                code = item["code"]
                link = item["url"]

                product_info = {'name':name,
                                'brand_name':brand_name,
                                'price':price,
                                'couponStatus':couponStatus,
                                'code':code,
                                'link':link}
                self.product_data.append(product_info)
            
        return self.product_data

    def to_dataframe(self):
        df = pd.DataFrame(self.product_data)
        df.to_csv('AJIO_product_details.csv',index=False)
        print("Data saved to CSV.")

    def main(self):  
        print('starting data scraping....') 
        self.data_scrape()    
        self.to_dataframe()

if __name__ == "__main__":
    Ajio_scraper().main()    

