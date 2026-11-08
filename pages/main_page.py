import allure
from selenium.webdriver.support.ui import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

LOADING_ORDER_NUMBER = 9999


class MainPage(BasePage):
    def wait_constructor_loaded(self):
        self.wait_visible(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.BUN_INGREDIENT)

    def is_ingredient_details_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Добавить булку в конструктор")
    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_AREA)

    def get_bun_counter(self):
        return int(self.get_text(MainPageLocators.BUN_COUNTER))

    @allure.step("Оформить заказ и получить его номер")
    def make_order(self):
        self.add_bun_to_order()
        self.click(MainPageLocators.MAKE_ORDER_BUTTON)
        return self._wait_order_number()

    def _wait_order_number(self):
        def number_loaded(driver):
            text = driver.find_element(*MainPageLocators.ORDER_NUMBER).text
            return int(text) if text.isdigit() and int(text) != LOADING_ORDER_NUMBER else False

        return WebDriverWait(self.driver, 30).until(number_loaded)

    def is_make_order_button_visible(self):
        return self.is_visible(MainPageLocators.MAKE_ORDER_BUTTON)

    def is_constructor_visible(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER)
