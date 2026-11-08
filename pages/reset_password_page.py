import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Ввести новый пароль")
    def type_password(self, password):
        self.type_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать на кнопку показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_ICON)

    def is_password_input_highlighted(self):
        return self.is_visible(ResetPasswordPageLocators.ACTIVE_INPUT_WRAPPER)
