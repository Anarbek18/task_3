import allure
from selenium.webdriver.support.ui import WebDriverWait

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def is_opened(self):
        return self.is_visible(OrderFeedPageLocators.HEADER)

    @allure.step("Кликнуть на заказ в ленте")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER_CARD)

    def get_feed_order_numbers(self):
        self.wait_visible(OrderFeedPageLocators.ORDER_NUMBERS)
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBERS)
        return [int(element.text.lstrip("#")) for element in elements]

    def get_total_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_COUNTER))

    def get_today_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_COUNTER))

    @allure.step("Дождаться номера заказа в разделе «В работе»")
    def is_order_in_progress(self, order_number):
        def order_listed(driver):
            text = driver.find_element(*OrderFeedPageLocators.IN_PROGRESS_LIST).text
            return order_number in {int(item) for item in text.split() if item.isdigit()}

        try:
            return WebDriverWait(self.driver, 15).until(order_listed)
        except Exception:
            return False
