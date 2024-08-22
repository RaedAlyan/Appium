from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


desired_cap = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=desired_cap)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()
check_box1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Checkbox 1')
check_box1_location = check_box1.location
driver.tap([(check_box1_location['x'], check_box1_location['y'])])  # double tap using W3C Actions API.
driver.tap([(check_box1_location['x'], check_box1_location['y'])])  # double tap using W3C Actions API.
# This command is used to Perform double tap using mobile gestures command.
# driver.execute_script('mobile: doubleClickGesture', {'x': check_box1_location['x'], 'y': check_box1_location['y']})
driver.quit()
