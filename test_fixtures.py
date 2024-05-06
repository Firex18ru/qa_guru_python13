import time
from selene import browser, by, have

def test_search():
    browser.open('https://google.com')
    time.sleep(3)
    browser.element(by.name('q')).type('asus graphics card').press_enter()
    time.sleep(3)
    browser.element('[id="search"]').should(have.text('asus graphics card'))

#    browser.all('.web-result').first.element('.result__link').click()

#    browser.should(have.title_containing('asus/asus graphics card'))