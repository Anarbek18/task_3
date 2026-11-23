import allure

from helpers import api
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик по заказу в ленте открывает окно с деталями")
    def test_order_click_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.is_opened()

        order_feed_page.click_first_order()

        assert order_feed_page.is_modal_opened()

    @allure.title("Заказы из «Истории заказов» отображаются в «Ленте заказов»")
    def test_user_history_orders_are_shown_in_feed(self, driver, user):
        api.create_order(user["token"])
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login(user["email"], user["password"])
        account_page = AccountPage(driver)
        account_page.go_to_account()
        account_page.go_to_order_history()
        history_numbers = account_page.get_history_order_numbers()

        account_page.go_to_order_feed()
        feed_numbers = OrderFeedPage(driver).get_feed_order_numbers()

        assert set(history_numbers) & set(feed_numbers)

    @allure.title("При создании заказа растёт счётчик «Выполнено за всё время»")
    def test_total_counter_increases_after_order(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(logged_in_driver)
        total_before = order_feed_page.get_total_counter()
        order_feed_page.go_to_constructor()
        main_page.make_order()
        main_page.close_modal()

        main_page.go_to_order_feed()

        assert order_feed_page.get_total_counter() > total_before

    @allure.title("При создании заказа растёт счётчик «Выполнено за сегодня»")
    def test_today_counter_increases_after_order(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(logged_in_driver)
        today_before = order_feed_page.get_today_counter()
        order_feed_page.go_to_constructor()
        main_page.make_order()
        main_page.close_modal()

        main_page.go_to_order_feed()

        assert order_feed_page.get_today_counter() > today_before

    @allure.title("Номер оформленного заказа появляется в разделе «В работе»")
    def test_new_order_appears_in_progress(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        order_number = main_page.make_order()
        main_page.close_modal()

        main_page.go_to_order_feed()

        assert OrderFeedPage(logged_in_driver).is_order_in_progress(order_number)
