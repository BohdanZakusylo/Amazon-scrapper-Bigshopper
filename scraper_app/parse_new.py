import time
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from Bigshopper.local_settings import USER_AGENT

def get_new_prices_from_sellers(url, option):
    seller_name_price_dict = {}
    user_agent = USER_AGENT

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")
    if option:
        options.add_argument("headless")

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try:
        element = driver.find_element(By.XPATH, '//*[@id="olpLinkWidget_feature_div"]/div[2]/span/a/div')
    except NoSuchElementException:
        return seller_name_price_dict

    overlay = driver.find_element(By.XPATH, '//*[@id="sp-cc-rejectall-link"]')
    overlay.click()
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

    element.click()

    time.sleep(2)

    parent_xpath = driver.find_element(By.XPATH, '//*[@id="aod-offer-list"]')

    new_or_not = parent_xpath.find_elements(By.XPATH, '//div[@id="aod-offer-list"]//div[@id="aod-offer-heading"]')

    prices_whole = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-price') and contains(@class, 'aok-align-center') and contains(@class, 'centralizedApexPricePriceToPayMargin')]")

    for i in range(0, (len(prices_whole)) - len(new_or_not)):
        prices_whole.pop(i)

    solds_by = parent_xpath.find_elements(By.XPATH, '//*[@id="aod-offer-soldBy"]/div/div/div[2]/a')
    counter = 0
    for i in new_or_not:
        if i.text == "Nieuw" or i.text == "New" or i.text == "Neu":
            if not solds_by[counter].text:
                seller_name_price_dict["Amazon"] = prices_whole[counter].text.replace("\n", '.')
            else:
                seller_name_price_dict[solds_by[counter].text] = prices_whole[counter].text.replace("\n", '.')
        counter += 1
    driver.close()

    driver.quit()
    return seller_name_price_dict
