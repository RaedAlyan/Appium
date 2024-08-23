from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
views = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
views.click()

buttons = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
grid = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')

# Swipe Up
driver.swipe(start_x=grid.location['x'], start_y=grid.location['y'], end_x=buttons.location['x'],
             end_y=buttons.location['y'])

# Swipe Down
tabs = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Tabs')
webview = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='WebView')
driver.swipe(start_x=tabs.location['x'], start_y=tabs.location['y'], end_x=webview.location['x'],
             end_y=webview.location['y'])
driver.quit()
