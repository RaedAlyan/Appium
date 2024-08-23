from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()

# Scroll Right
driver.execute_script('mobile: scrollGesture', {
    'left': 500, 'top': 500, 'width': 500, 'height': 0,
    'direction': 'right',
    'percent': 1.0
})

# Scroll Left
driver.execute_script('mobile: scrollGesture', {
    'left': 500, 'top': 500, 'width': 500, 'height': 0,
    'direction': 'left',
    'percent': 1.0
})
driver.quit()
