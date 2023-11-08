xpath = {
    "nl": {
        "condition_xpath": '//*[@id="newAccordionCaption_feature_div"]/div/span',
        "seller_name_xpath1": '//a[@id="sellerProfileTriggerId"]',
        "seller_name_xpath2": '//div[@class="offer-display-feature-text a-spacing-none"]/span',
        "normal_price_xpath": (
            '//div[@id="corePriceDisplay_desktop_feature_div"]//span[@class="aok-relative"]/span[not('
            'contains(@class,"pricePerUnit"))]//span[@class="a-offscreen"]'),
        "current_price_xpath": '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]',
        "shipping_price_xpath": '//span[@data-csa-c-delivery-price]/@data-csa-c-delivery-price',
        "asin_number_xpath": '//div[@data-csa-c-asin][@data-csa-c-asin and @data-csa-c-asin != ""]/@data-csa-c-asin',
        "title_info_xpath": '//*[@id="productTitle"]',
        "product_data_xpath_1": ('//th[@class="a-color-secondary a-size-base prodDetSectionEntry"] | //td['
                                 '@class="a-size-base prodDetAttrValue"]'),
        "product_data_xpath_2": ('//div[@id="detailBullets_feature_div"]//li/span/span[1] | //div['
                                 '@id="detailBullets_feature_div"]//li/span/span[2]'),
        "product_data_xpath_3": '//td[@class="ucc-attribute-title"]/span',
        "other_seller_button": '//*[@id="olpLinkWidget_feature_div"]/div[2]/span/a/div',
        "overlay_xpath": '//*[@id="sp-cc-rejectall-link"]',
        "other_seller_parent_xpath": '//*[@id="aod-offer-list"]',
        "other_seller_condition_xpath": '//div[@id="aod-offer-list"]//div[@id="aod-offer-heading"]',
        "other_seller_price_xpath": '//span[contains(@class, "a-price") and contains(@class, "aok-align-center") and '
                                    'contains(@class, "centralizedApexPricePriceToPayMargin")]',
        "other_seller_sold_by_xpath": '//*[@id="aod-offer-soldBy"]/div/div/div[2]/a'
    },
    "de": {
        "condition_xpath": '//*[@id="newAccordionCaption_feature_div"]/div/span',
        "seller_name_xpath": '//a[@id="sellerProfileTriggerId"]',
        "normal_price_xpath": (
            '//div[@id="corePriceDisplay_desktop_feature_div"]//span[@class="aok-relative"]/span[not('
            'contains(@class,"pricePerUnit"))]//span[@class="a-offscreen"]'),
        "shipping_price_xpath": '//span[@data-csa-c-delivery-price]/@data-csa-c-delivery-price',
        "asin_number_xpath": '//div[@data-csa-c-asin][@data-csa-c-asin and @data-csa-c-asin != ""]/@data-csa-c-asin',
        "title_info_xpath": '//*[@id="productTitle"]',
        "product_data_xpath_1": ('//th[@class="a-color-secondary a-size-base prodDetSectionEntry"] | //td['
                                 '@class="a-size-base prodDetAttrValue"]'),
        "product_data_xpath_2": ('//div[@id="detailBullets_feature_div"]//li/span/span[1] | //div['
                                 '@id="detailBullets_feature_div"]//li/span/span[2]'),
        "product_data_xpath_3": '//td[@class="ucc-attribute-title"]/span'
    },
    "com": {
        "condition_xpath": '//*[@id="newAccordionCaption_feature_div"]/div/span',
        "seller_name_xpath": '//a[@id="sellerProfileTriggerId"]',
        "normal_price_xpath": (
            '//div[@id="corePriceDisplay_desktop_feature_div"]//span[@class="aok-relative"]/span[not('
            'contains(@class,"pricePerUnit"))]//span[@class="a-offscreen"]'),
        "shipping_price_xpath": '//span[@data-csa-c-delivery-price]/@data-csa-c-delivery-price',
        "asin_number_xpath": '//div[@data-csa-c-asin][@data-csa-c-asin and @data-csa-c-asin != ""]/@data-csa-c-asin',
        "title_info_xpath": '//*[@id="productTitle"]',
        "product_data_xpath_1": ('//th[@class="a-color-secondary a-size-base prodDetSectionEntry"] | //td['
                                 '@class="a-size-base prodDetAttrValue"]'),
        "product_data_xpath_2": ('//div[@id="detailBullets_feature_div"]//li/span/span[1] | //div['
                                 '@id="detailBullets_feature_div"]//li/span/span[2]'),
        "product_data_xpath_3": '//td[@class="ucc-attribute-title"]/span'
    },
}


def get_xpath_variables(country_code):
    return xpath[country_code]
