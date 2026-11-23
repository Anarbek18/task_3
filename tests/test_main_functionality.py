import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход в «Конструктор» по клику на кнопку в шапке")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()

        main_page.go_to_constructor()

        assert main_page.is_constructor_visible()

    @allure.title("Переход в «Ленту заказов» по клику на кнопку в шапке")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_order_feed()

        assert OrderFeedPage(driver).is_opened()

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_click_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.wait_constructor_loaded()

        main_page.click_ingredient()

        assert main_page.is_ingredient_details_visible()

    @allure.title("Окно с деталями ингредиента закрывается по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.wait_constructor_loaded()
        main_page.click_ingredient()

        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("Добавление ингредиента в заказ увеличивает его счётчик")
    def test_adding_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.wait_constructor_loaded()

        main_page.add_bun_to_order()

        assert main_page.get_bun_counter() == 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_make_order(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)

        order_number = main_page.make_order()

        assert order_number > 0 and main_page.is_modal_opened()
