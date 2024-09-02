from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.options.android import UiAutomator2Options
from time import sleep


desired_cap = {
    "appium:appPackage": "com.google.android.apps.messaging",
    "appium:appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity",
    "platformName": "Android",
    "deviceName": "Pixel 8 Pro API 26",
    "udid": "emulator-5554",
}

appium_options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
sleep(10)
# Lunching another app.
driver.execute_script('mobile: startActivity',
                      {'intent': 'com.android.contacts/com.android.contacts.activities.PeopleActivity'})
sleep(10)
driver.quit()
