import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_product_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract relevant information using CSS selectors or other methods
        product_title = soup.select_one(".product-title").get_text()
        product_price = soup.select_one(".product-price").get_text()
        product_description = soup.select_one(".product-description").get_text()

        return {
            "title": product_title,
            "price": product_price,
            "description": product_description
        }
    else:
        print("Failed to retrieve the page.")

def main():
    product_url = input("Enter the product URL: ")
    product_data = scrape_product_details(product_url)

    if product_data:
        print("Product Title:", product_data["title"])
        print("Product Price:", product_data["price"])
        print("Product Description:", product_data["description"])

        # Create a DataFrame
        df = pd.DataFrame([product_data])

        # Save the DataFrame to an Excel file
        df.to_excel("product_data.xlsx", index=False)
        print("Product data saved to 'product_data.xlsx'")

if __name__ == "__main__":
    main()
