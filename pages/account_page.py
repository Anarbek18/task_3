import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Перейти в «Историю заказов»")
    def go_to_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    def get_history_order_numbers(self):
        self.wait_visible(AccountPageLocators.HISTORY_ORDER_NUMBERS)
        elements = self.driver.find_elements(*AccountPageLocators.HISTORY_ORDER_NUMBERS)
        return [int(element.text.lstrip("#")) for element in elements]
