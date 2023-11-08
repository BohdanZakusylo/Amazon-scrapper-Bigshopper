from django.core.management.base import BaseCommand
from scraper_app.product_info import call_main
from scraper_app.views import scrape_amazon
from .save_to_db import save_product_info
from scraper_app.parse_new import get_new_prices_from_sellers



class Command(BaseCommand):
    help = "Scrape Amazon product information"

    def add_arguments(self, parser):
        parser.add_argument("website", help="Input either amazon.de or amazon.nl", type=str)
        parser.add_argument("search", help="Input the search query (gtin, title)", type=str)
        parser.add_argument("--headless", action='store_true', help="Input the headless options")

    def handle(self, *args, **kwargs):
        website = kwargs["website"]
        search = kwargs["search"]
        option = kwargs["headless"]
        print(option)
        url = scrape_amazon(search, website)
        result = call_main(url)
        new_prices = get_new_prices_from_sellers(url, option)
        print(new_prices)
        save_product_info(result, url, new_prices)
