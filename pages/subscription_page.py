from selenium.webdriver.common.by import By

from pages.base_page import Page


class SubscriptionPage(Page):
    TITLE = (By.CSS_SELECTOR, "[class*='h3']")
    UPGRADE_BTN = (By.CSS_SELECTOR, "a[href='/prosub']")
    BACK_BTN = (By.XPATH, "//div[contains(text(), 'Back')]")
    def open_subscription_page(self):
        self.open_url('https://soft.reelly.io/subscription')

    def verify_title(self):
        self.find_elements(*self.TITLE)
        self.verify_text("Subscription & payments", *self.TITLE)

    def verify_btns(self):
        self.find_element(*self.UPGRADE_BTN)
        self.find_element(*self.BACK_BTN)