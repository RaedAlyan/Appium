from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos
from time import sleep

appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
views = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
views.click()

# Scroll Down
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 2,
})

# Scroll Up
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 0.5,
    'speed': 1000
})
sleep(15)
driver.quit()
