from selene import browser, by, have


def test_search():
    browser.open('https://google.com')

    browser.element(by.name('q')).type('asus graphics card').press_enter()

    browser.element('[id="search"]').should(have.text('graphics card'))


def test_wrong_search():
    browser.open('https://google.com')

    browser.element(by.name('q')).type('hfndуцпцgfewrwrfdsfwerkcvklлсяув').press_enter()

    browser.element('[id="search"]').should(have.text('неверный hfndуцпцgfewrwrfdsfwerkcvklлсяув запрос'))
