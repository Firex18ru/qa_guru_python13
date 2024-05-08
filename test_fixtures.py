from selene import browser, by, have


def test_search():
    browser.open('https://google.com')

    browser.element(by.name('q')).type('asus graphics card').press_enter()

    browser.element('[id="search"]').should(have.text('graphics card'))


def test_wrong_search():
    string = "rtdfwabcvnch ufgdsswyr weqqqvdsqz"

    browser.open('https://google.com')
    browser.element(by.name('q')).type(string).press_enter()

    browser.element('[id="rcnt"]').should(have.text('По запросу rtdfwabcvnch ufgdsswyr weqqqvdsqz ничего не найдено.'))