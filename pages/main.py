#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://moscow.megafon.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(xpath='//*[@id="mount"]/div/div/div/main/div/div[1]/div/div/div/div/h2/a')

    # Search button
    #search_run_button = WebElement(xpath='//html/body/div[3]/div[2]/noindex/div/div/div[2]/div[2]/div/div/form/div/button')

    # Titles of the products in search results
    #products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    #sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    #products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')