from .base_page import BasePage
from ..pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "https://selenium1py.pythonanywhere.com/" in self.browser.current_url, f"url is not valid and is {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "login form is not exists"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "register form is not exists"