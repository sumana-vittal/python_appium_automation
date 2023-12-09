from pages.base_page import Page
from appium.webdriver.common.appiumby import AppiumBy


class SearchPage(Page):
    SEARCH_FIELD = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULT = (AppiumBy.ID, "org.wikipedia:id/page_list_item_title")

    def input_search_text(self):
        self.input('Python (programming language)', *self.SEARCH_FIELD)

    def verify_search_result(self):
        self.verify_text('Python (programming language)', *self.SEARCH_RESULT)