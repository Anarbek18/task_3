from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
