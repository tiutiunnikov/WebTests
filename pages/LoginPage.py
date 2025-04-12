from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocator:
    LOGIN_FIELD = (By.XPATH, 'field_email"')
    PASSWORD_FIELD = (By.XPATH, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CANT_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass