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
start_point = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')

end_point = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')

# Perform scroll
driver.scroll(origin_el=start_point, destination_el=end_point)
sleep(15)

# Scroll Up
start_point = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
end_point = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls')
driver.scroll(origin_el=start_point, destination_el=end_point)
driver.quit()
