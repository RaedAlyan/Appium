from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
views = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
views.click()
controls = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls')
grid = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')


driver.flick(start_x=grid.location['x'], start_y=grid.location['y'], end_x=controls.location['x'],
             end_y=controls.location['y'])

driver.quit()

