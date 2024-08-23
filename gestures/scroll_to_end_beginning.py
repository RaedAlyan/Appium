from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()

# Scroll to end
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                    value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')


# Scroll to beginning
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                    value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')
driver.quit()
