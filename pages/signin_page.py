from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASS_FIELD = (By.ID, 'field')
    LOGIN_BNT = (By.CSS_SELECTOR, "[class*='login-button']")


    def open_signin_page(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login(self):
        self.input_text('zakharova.kr+test_careerist@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Pa55word!', *self.PASS_FIELD)
        self.wait_and_click(*self.LOGIN_BNT)

