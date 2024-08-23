from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from desired_caps import wdio


appium_options = UiAutomator2Options().load_capabilities(wdio)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.implicitly_wait(5)

drag_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drag')
drag_element.click()
draggable_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drag-c1')
droppable_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'drop-c1')

driver.execute_script('mobile: dragGesture', {
    'elementId': draggable_element,
    'endX': droppable_element.location['x'],
    'endY': droppable_element.location['y']
})
driver.quit()
