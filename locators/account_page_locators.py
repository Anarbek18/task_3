from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_ORDER_NUMBERS = (
        By.XPATH,
        "//a[contains(@class,'OrderHistory_link')]//p[contains(@class,'text_type_digits-default')]",
    )
