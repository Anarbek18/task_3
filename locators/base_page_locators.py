from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")


class ModalLocators:
    OPENED_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class,'Modal_modal__close')]",
    )
