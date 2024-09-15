from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SETTINGS_LINK = (By.CSS_SELECTOR, "a[href='/settings']")
    MAIN_MENU_MOBILE_LINK = (By.CSS_SELECTOR, "[class='circle-gradient']")
    USER_ICON = (By.CSS_SELECTOR, "[class='menu-img-agent-listing']")

    def open(self):
        self.open_url('https://soft.reelly.io')

    def open_main_menu_mobile(self):
        self.wait_and_click(*self.MAIN_MENU_MOBILE_LINK)

    def click_user_icon_mobile(self):
        self.wait_and_click(*self.USER_ICON)

    def open_settings(self):
        self.wait_and_click(*self.SETTINGS_LINK)

