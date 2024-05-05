import pytest

@pytest.fixture(scope="session")
def browser():
    print("браузер!")
    yield
    print("закрываем браузер!")
@pytest.fixture
def login_page(browser):
    print("логин пейдж!")
    pass
@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
#    assert 1 == 2

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"