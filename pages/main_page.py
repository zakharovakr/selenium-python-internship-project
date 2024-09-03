from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SETTINGS_LINK = (By.CSS_SELECTOR, "a[href='/settings']")


    def open(self):
        self.open_url('https://soft.reelly.io')

    def open_settings(self):
        self.wait_and_click(*self.SETTINGS_LINK)

