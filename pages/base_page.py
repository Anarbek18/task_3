import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import HeaderLocators, ModalLocators

DEFAULT_TIMEOUT = 10

DRAG_AND_DROP_SCRIPT = """
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();
const fire = (element, type) => element.dispatchEvent(
    new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer})
);
fire(source, 'dragstart');
fire(target, 'dragenter');
fire(target, 'dragover');
fire(target, 'drop');
fire(source, 'dragend');
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_url_contains(self, part, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(part))

    def click(self, locator):
        element = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, source, target)

    @allure.step("Перейти в «Конструктор»")
    def go_to_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в «Ленту заказов»")
    def go_to_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)

    @allure.step("Перейти в «Личный кабинет»")
    def go_to_account(self):
        self.click(HeaderLocators.ACCOUNT_LINK)

    @allure.step("Закрыть модальное окно крестиком")
    def close_modal(self):
        self.click(ModalLocators.CLOSE_BUTTON)
        self.wait_invisible(ModalLocators.OPENED_MODAL)

    def is_modal_opened(self):
        return self.is_visible(ModalLocators.OPENED_MODAL)

    def is_modal_closed(self):
        try:
            self.wait_invisible(ModalLocators.OPENED_MODAL)
            return True
        except Exception:
            return False
