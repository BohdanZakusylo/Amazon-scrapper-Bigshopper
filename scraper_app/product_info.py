import json
import asyncio
from lxml import html
import requests
import time
import datetime
from .xpath_variables import *
from scraper_app.cache_mongo import save_html_page_cache, save_product_price_history, save_product, save_product_data
from Bigshopper.local_settings import USER_AGENT

headers = USER_AGENT


# Main Funcs


def country_code_parser(url):
    """Function that takes the scraped url and splits the country code from it."""
    first_dot_index = url.find(".")
    if first_dot_index != -1:
        second_dot_index = url.find(".", first_dot_index + 1)

        if second_dot_index != -1:
            slash_index = url.find("/", second_dot_index)

            if slash_index != -1:
                country_code = url[second_dot_index + 1:slash_index]
                return country_code


async def url_parser(url):
    """ Function that returns the current URL """
    return url


async def current_date():
    """Function that return the current date"""
    return datetime.date.today()


async def condition_info_parser(parsed_content, xpath_details):
    """Function that scrapers the condition of an item on amazon."""
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            if element_text is not None:
                return "New"
            return element_text
        except AttributeError:
            return element


async def seller_name_info_parser(parsed_content, xpath_details1, xpath_details2):
    """Function that returns the Sold by: "name"  part from amazon"""
    elements = parsed_content.xpath(xpath_details1)
    if not parsed_content.xpath(xpath_details1):
        elements = parsed_content.xpath(xpath_details2)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            return element_text
        except AttributeError:
            return element


async def normal_price_info_parser(parsed_content, xpath_details):
    """Function that returns the normal price of an item"""
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            return element_text
        except AttributeError:
            print(element)


async def shipping_price_info_parser(parsed_content, xpath_details):
    """Function that returns the shipping price of an item"""
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            return element_text
        except AttributeError:
            return element


async def asin_number_info_parser(parsed_content, xpath_details):
    """Function that returns the ASIN number of an item"""
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            return element_text
        except AttributeError:
            return element


async def title_info_parser(parsed_content, xpath_details):
    """Function that returns the ASIN number of an item"""
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            return element_text
        except AttributeError:
            print(element)


async def product_data_from_table(parsed_content, xpath_details1, xpath_details2, xpath_details3):
    """
    Function that return the product data of an item. There are multitudes of datatables
    on Amazon based on seller preferences therefore it has 3 xpaths to try to scrape which
    ever finds a result
    """
    results = dict()
    elements = parsed_content.xpath(xpath_details1)
    if not elements:
        elements = parsed_content.xpath(xpath_details2)
    if not elements:  # the apple solutions (why apple why????)
        title_elements = parsed_content.xpath(xpath_details3)
        for title_element in title_elements:
            title = title_element.text_content().strip()
            result_element = title_element.getparent().getnext()
            result = result_element.xpath(".//span/text()")[0].strip()

            results[title] = result

    key = None
    for i, element in enumerate(elements):
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").replace("\u200f", "").replace(
                "\u20ac", "").replace("\n", "").replace(" ", "").strip()
            if i % 2 == 0:
                key = element_text
            else:
                results[key] = element_text
        except AttributeError:
            print(element)

    json_string = json.dumps(results)
    return json_string


async def current_price_info_parser(parsed_content, xpath_details):
    """
    Function that scrapes the current price of the item (sales price)
    It scrapes a sentence in reality but this function splits that sentence
    after the first empty space which just returns the price tag
    """
    elements = parsed_content.xpath(xpath_details)
    for element in elements:
        try:
            element_unfiltered = element.text_content()
            element_text = element_unfiltered.replace("\u200b", "").replace("\u200e", "").strip()
            price_element_text = element_text.split(" ", 1)
            return price_element_text[0]
        except AttributeError:
            print(element)


async def get_html_code(parsed_content):
    """ Function that gets all the html from the page"""
    return parsed_content.text_content()


async def gather_all(url, headers):
    """
    Function that makes a get request, parses the html from the page and
    afterward combines all html xpath querying into a single list
    Then it returns a list with the scraped data from the html
    """
    while True:
        response = requests.get(url, headers)
        print(response.status_code)
        await asyncio.sleep(1)
        if response.status_code != 503:
            break
    if response.status_code == 200:
        page_content = response.content
        parsed_content = html.fromstring(page_content)
        xpath_variables = get_xpath_variables(country_code_parser(url))
        # added the async to it, so all the functions ill start working at once.
        tasks = [
            product_data_from_table(parsed_content, xpath_variables["product_data_xpath_1"],
                                    xpath_variables["product_data_xpath_2"], xpath_variables["product_data_xpath_3"]),
            title_info_parser(parsed_content, xpath_variables["title_info_xpath"]),
            current_price_info_parser(parsed_content, xpath_variables["current_price_xpath"]),
            normal_price_info_parser(parsed_content, xpath_variables["normal_price_xpath"]),
            shipping_price_info_parser(parsed_content, xpath_variables["shipping_price_xpath"]),
            asin_number_info_parser(parsed_content, xpath_variables["asin_number_xpath"]),
            seller_name_info_parser(parsed_content, xpath_variables["seller_name_xpath1"],
                                    xpath_variables["seller_name_xpath2"]),
            condition_info_parser(parsed_content, xpath_variables["condition_xpath"]),
            current_date(),
            url_parser(url),
            get_html_code(parsed_content)
        ]
        results = await asyncio.gather(*tasks)
        """ results is not async, just a normal variable """
        return results
    else:
        print("ooops not 200")


async def main_product_info(url):
    """
    Main function that combines the return values in a single variable asynchronously
    here the asyncio gathers all the task
    """
    results = await gather_all(url, headers)

    if results is not None:
        print("Product Data:", results[0])
        print("Title:", results[1])
        print("Current Price:", results[2])
        print("Normal Price:", results[3])
        print("Shipping Price:", results[4])
        print("ASIN Number:", results[5])
        print("Seller Name:", results[6])
        print("Condition Info:", results[7])
        print("Current date:", results[8])
        print("URL:", results[9])


        # save cache to mongo
        save_html_page_cache(results[5], results[10])
        save_product(results[5], results[1], results[6], results[3], results[2], results[4], results[7])
        save_product_data(results[5], results[0])
        save_product_price_history(results[5], results[3], results[2], results[4])

        return results


def call_main(url):
    """main function"""
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main_product_info(url))


