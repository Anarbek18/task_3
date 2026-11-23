import allure

import config
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_page(self):
        self.open(config.LOGIN_URL)
        self.wait_visible(LoginPageLocators.HEADER)

    @allure.step("Войти с почтой и паролем")
    def login(self, email, password):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать «Восстановить пароль»")
    def click_restore_password_link(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_LINK)
