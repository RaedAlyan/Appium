from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()

# Swipe Left
galley = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/gallery')
driver.execute_script('mobile: swipeGesture', {
    'elementId': galley,
    'direction': 'left',
    'percent': 0.3,
    'speed': 5000
})
# Swipe Right
galley = driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/gallery')
driver.execute_script('mobile: swipeGesture', {
    'elementId': galley,
    'direction': 'right',
    'percent': 0.3,
    'speed': 3000
})
driver.quit()
