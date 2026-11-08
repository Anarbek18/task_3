import allure

import config
from pages.account_page import AccountPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_go_to_account(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)

        account_page.go_to_account()
        account_page.wait_url_contains("account/profile")

        assert account_page.get_current_url() == config.ACCOUNT_URL

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)
        account_page.go_to_account()

        account_page.go_to_order_history()
        account_page.wait_url_contains("order-history")

        assert account_page.get_current_url() == config.ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)
        account_page.go_to_account()

        account_page.logout()
        account_page.wait_url_contains("login")

        assert account_page.get_current_url() == config.LOGIN_URL
