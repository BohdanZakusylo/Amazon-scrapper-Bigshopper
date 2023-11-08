import pymongo
from datetime import datetime
from Bigshopper.local_settings import MONGO_DSN


def get_mongo_client(collection):
    """Mongo connection"""
    mongo_client = pymongo.MongoClient(host=[MONGO_DSN], tz_aware=True)
    mongo_db = mongo_client["amazon"]

    return mongo_db[collection]


def save_html_page_cache(bid, html):
    """save to html collection"""
    mongo_html_collection = get_mongo_client("html")
    mongo_html_collection.insert_one({
        "html": html,
        "bid": bid,
        "timestamp": datetime.now(),  # change here
    })


def save_product_price_history(bid, original_prices, sale_prices, shipping_prices):
    """save to products's price history"""
    mongo_price_history_collection = get_mongo_client("price_history")
    mongo_price_history_collection.insert_one({
        "bid": bid,
        "original_prices": original_prices,
        "sale_prices": sale_prices,
        "shipping_prices": shipping_prices,
        "timestamp": datetime.now()
    })


def save_product(bid, title, seller_name, original_prices, sale_prices, shipping_prices, condition_info):
    """collection name"""
    mongo_products_collection = get_mongo_client("products")
    if mongo_products_collection.count_documents({"bid": bid}) > 0:
        # update if exists"""
        mongo_products_collection.update_one({"bid": bid}, {"$set": {
            "title": title,
            "seller_name": seller_name,
            "original_prices": original_prices,
            "sale_prices": sale_prices,
            "shipping_prices": shipping_prices,
            "condition_info": condition_info,
            "timestamp": datetime.now()
        }})
    else:
        # insert if not exists
        mongo_products_collection.insert_one({
            "bid": bid,
            "title": title,
            "seller_name": seller_name,
            "original_prices": original_prices,
            "sale_prices": sale_prices,
            "shipping_prices": shipping_prices,
            "condition_info": condition_info,
            "timestamp": datetime.now(),
        })


def save_product_data(bid, data):
    mongo_product_data_collection = get_mongo_client("product_datas")
    if mongo_product_data_collection.count_documents({"bid": bid}) > 0:
        # update if exists
        mongo_product_data_collection.update_one({"bid": bid}, {"$set": {
            "data": data
        }
        })
    else:
        # insert if not exists
        mongo_product_data_collection.insert_one({
            "bid": bid,
            "data": data
        })
