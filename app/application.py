from pages.base_page import Page
from pages.main_page import MainPage
from pages.signin_page import SigninPage
from pages.settings_page import SettingsPage
from pages.subscription_page import SubscriptionPage

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SigninPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscription_page = SubscriptionPage(driver)