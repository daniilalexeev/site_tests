#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from attr import attr

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPageCorporate(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://moscow.megafon.ru/corporate'

        super().__init__(web_driver, url)

    # Main search field
    tariff_tab = WebElement(css_selector='[data-testid="MainPageButtonsBanner-bannerButton[1]"]')