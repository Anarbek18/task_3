from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_HIDE_PASSWORD_ICON = (By.XPATH, "//div[contains(@class,'input__icon')]")
    ACTIVE_INPUT_WRAPPER = (By.XPATH, "//div[contains(@class,'input_status_active')]")
