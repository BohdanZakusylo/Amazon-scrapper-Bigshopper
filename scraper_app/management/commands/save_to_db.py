from scraper_app.models import Product, Price, ProductSpecification, OtherDistributors
from scraper_app.parse_new import get_new_prices_from_sellers

# Function to save product information to the database
def save_product_info(results, url, new_prices):
    try:
        if results is not None and len(results) >= 7:
            # Ensure 'results' is not None and has at least 7 elements

            # Create a new Product instance and save it to the database
            product = Product(asin=results[5], gtin=results[5], link=url, productTitle=results[1], sellerName=results[6])
            product.save()

            # Create a new Price instance related to the product and save it
            price = Price(product=product, originalPrice=results[3], salePrice=results[2], shippingPrice=results[4])
            price.save()

            # Create a new ProductSpecification instance related to the product and save it
            product_spec = ProductSpecification(product=product, specification=results[0], sellerName=results[6])
            product_spec.save()

            # Loop through the new prices and save them as OtherDistributors related to the product
            for seller, price in new_prices.items():
                other_distributors = OtherDistributors(product=product, normal_price=price, sold_by=seller)
                other_distributors.save()
            print("Data saved to the database successfully.")
        else:
            print("Invalid 'results' data. Cannot save to the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
