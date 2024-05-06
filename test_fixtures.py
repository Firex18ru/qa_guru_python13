import time

import pytest
from selene import browser, by, have


def test_search(browser):
    browser.open('https://google.com')
    time.sleep(10)
    browser.element(by.name('q')).type('asus graphics card').press_enter()
    time.sleep(10)
    browser.all('.web-result').first.element('.result__link').click()

    browser.should(have.title_containing('asus'))