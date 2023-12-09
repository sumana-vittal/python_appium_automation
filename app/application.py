from pages.base_page import Page
from pages.search_page import SearchPage
from pages.explore_page import ExplorePage
from pages.onboarding_page import OnboardingPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.search_page = SearchPage(driver)
        self.explore_page = ExplorePage(driver)
        self.onboarding_page = OnboardingPage(driver)

