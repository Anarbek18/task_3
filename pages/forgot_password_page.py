import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Ввести почту и нажать «Восстановить»")
    def restore_password(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)
