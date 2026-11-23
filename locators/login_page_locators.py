from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
