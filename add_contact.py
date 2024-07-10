import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:deviceName": "Pixel 8 Pro API 26",
    "appium:udid": "emulator-5554",
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
}

desired_capabilities = AppiumOptions()
desired_capabilities.load_capabilities(DESIRED_CAPABILITIES)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=desired_capabilities)
create_new_account_button = WebDriverWait(driver, 30).until(
    ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Create new contact'))
)
create_new_account_button.click()
cancel_button = WebDriverWait(driver, 30).until(
    ec.element_to_be_clickable((AppiumBy.ID, 'com.android.contacts:id/left_button'))
)
cancel_button.click()
first_name_input = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="First name"]'))
)
first_name_input.send_keys('Raed')
last_name_input = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Last name"]'))
)
last_name_input.send_keys('Eleyan')
phone_input = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Phone"]'))
)
phone_input.send_keys('0597774087')
email_input = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Email"]'))
)
email_input.send_keys('raed@gmail.com')
save_button = WebDriverWait(driver, 30).until(
    ec.element_to_be_clickable((AppiumBy.ID, 'com.android.contacts:id/editor_menu_save_button'))
)
save_button.click()
time.sleep(10)
driver.quit()




