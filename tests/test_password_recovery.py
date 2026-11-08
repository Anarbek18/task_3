import allure

import config
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_forgot_password_page_from_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()

        login_page.click_restore_password_link()

        assert login_page.get_current_url() == config.FORGOT_PASSWORD_URL

    @allure.title("Ввод почты и клик по «Восстановить» открывает страницу сброса пароля")
    def test_restore_password_opens_reset_page(self, driver, user):
        driver.get(config.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.restore_password(user["email"])
        forgot_password_page.wait_url_contains("reset-password")

        assert forgot_password_page.get_current_url() == config.RESET_PASSWORD_URL

    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле")
    def test_show_password_button_highlights_input(self, driver, user):
        driver.get(config.FORGOT_PASSWORD_URL)
        ForgotPasswordPage(driver).restore_password(user["email"])
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_url_contains("reset-password")
        reset_password_page.type_password("NewPassword123")

        reset_password_page.click_show_hide_password()

        assert reset_password_page.is_password_input_highlighted()
