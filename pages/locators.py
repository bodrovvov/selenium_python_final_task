from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.ID, "id_login-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "id_login-password")

    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password")
    REGISTER_PASSWORD__REPEAT_INPUT = (By.ID, "id_registration-password2")