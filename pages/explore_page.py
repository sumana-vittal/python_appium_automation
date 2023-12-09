from pages.base_page import Page
from appium.webdriver.common.appiumby import AppiumBy


class ExplorePage(Page):
    SEARCH_ICON = (AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']")

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)