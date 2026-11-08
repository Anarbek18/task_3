import pytest
from selenium import webdriver

import config
from helpers import api
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.set_window_size(1920, 1080)
    browser.get(config.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def user():
    created_user = api.create_user()
    yield created_user
    api.delete_user(created_user["token"])


@pytest.fixture
def logged_in_driver(driver, user):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(user["email"], user["password"])
    MainPage(driver).is_make_order_button_visible()
    return driver
