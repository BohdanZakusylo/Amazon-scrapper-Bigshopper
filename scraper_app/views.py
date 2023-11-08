from django.shortcuts import render
from lxml import html
import requests
import re
import Levenshtein
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Product, Price, ProductSpecification
from Bigshopper.local_settings import USER_AGENT


class Result(View):
    template = 'result.html'

    def get(self, request):
        products = Product.objects.all()
        prices = Price.objects.all()
        specifications = ProductSpecification.objects.all()


        print("Products:", products)  # Add this line for debugging
        print("Prices:", prices)      # Add this line for debugging
        print("Specification", specifications)

        if products and prices:
            return render(request, self.template, {'products': products, 'prices': prices, 'specification': specifications })
        else:
            return HttpResponse("No products or prices found in the database.")  # Add a message for debugging


def extract_decimal_number(value):
    decimal_pattern = r'\d+(\.\d+)?'
    match = re.search(decimal_pattern, value)
    if match:
        return match.group()
    return None


def scrape_amazon(product_title, website):
    url = f"https://www.{website}/s?k={product_title.replace(' ', '+')}"
    headers = USER_AGENT

    while True:
        response = requests.get(url, headers)
        if response.status_code != 503:
            break

    if response.status_code == 200:
        tree = html.fromstring(response.text)
        levenshtein_threshold = float("inf")

        product_containers = tree.xpath("//div[@data-asin and @data-component-type='s-search-result']")

        for product_container in product_containers:
            title_element = product_container.xpath(".//span[@class='a-size-base-plus a-color-base a-text-normal']")
            price_element = product_container.xpath(".//span[@class='a-offscreen']")

            if title_element and price_element:
                title = title_element[0].text_content().strip()
                raw_price = price_element[0].text_content().strip()
                price_value = extract_decimal_number(raw_price)

                if price_value:
                    levenshtein_distance = Levenshtein.distance(product_title, title)

                    if "sponsored" not in title and levenshtein_distance < levenshtein_threshold:
                        levenshtein_threshold = levenshtein_distance
                        product_link = product_container.xpath(
                            ".//a[@class='a-size-base a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal']")
                        if product_link:
                            best_result_link = f'https://www.{website}' + product_link[0].get("href")
                            return best_result_link
    else:
        raise Exception("503 error, reload the parser")