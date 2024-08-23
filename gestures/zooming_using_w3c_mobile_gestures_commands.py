from appium import webdriver
from appium.options.android import UiAutomator2Options
from desired_caps import maps
from time import sleep

appium_options = UiAutomator2Options().load_capabilities(maps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.implicitly_wait(15)

# Zoom In
driver.execute_script('mobile: pinchOpenGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 0.5,
})

sleep(5)  # For demo purpose

# Zoom Out
driver.execute_script('mobile: pinchCloseGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 1,
})
driver.quit()
