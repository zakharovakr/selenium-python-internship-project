from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SettingsPage(Page):
    PROFILE_NAME = (By.CSS_SELECTOR, ".name-prifile-setting")
    SUBSCR_LINK = (By.CSS_SELECTOR, "a[href='/subscription']")
    def open_subscription_payments(self):
        self.wait.until(EC.text_to_be_present_in_element(self.PROFILE_NAME, "test"))
        self.wait_and_click(*self.SUBSCR_LINK)
