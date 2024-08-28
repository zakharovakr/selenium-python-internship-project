from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):
    SUBSCR_LINK = (By.CSS_SELECTOR, "a[href='/subscription']")
    def open_subscription_payments(self):
        self.click(*self.SUBSCR_LINK)
