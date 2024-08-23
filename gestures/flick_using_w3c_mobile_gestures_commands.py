from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import apidemos


appium_options = UiAutomator2Options().load_capabilities(apidemos)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()

# Flick up using elementId
list_view = driver.find_element(by=AppiumBy.ID, value='android:id/list')
list_view_rect = list_view.rect

driver.execute_script('mobile: flingGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 1,
})

# Flick down using coordinates
driver.execute_script('mobile: flingGesture', {
    'left': list_view_rect['x'],
    'top': list_view_rect['y'],
    'direction': 'up',
    'width': list_view_rect['width'],
    'height': list_view_rect['height'],
    'percent': 2,
})

driver.quit()