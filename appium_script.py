from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/Users/raman/PycharmProjects/python_appium_automation/mobile_app/wikipedia.apk"
}

appium_server_url = "http://localhost:4723/wd/hub"
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button").click()
driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']").click()
driver.find_element(AppiumBy.ID, "org.wikipedia:id/search_src_text").send_keys('Python (programming language)')

expected_result = 'Python (programming language)'
actual_result = driver.find_element(AppiumBy.ID, "org.wikipedia:id/page_list_item_title").text

assert expected_result == actual_result, \
    f"Expected result {expected_result} didn't match the actual result '{actual_result}'"

driver.quit()
