"""
  - Project Description: This is an automated test for registering a user through an Android app.
  - Project Goal: Using Appium and Python to automate the process.
  - Owner: Raed Eleyan.
  - Date: 05/30/2024.
  - Contact: raedmalyan@gmail.com.
"""
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy as By


DESIRED_CAPABILITIES = {
  "platformName": "Android",
  "appium:deviceName": "Pixel 8 Pro API 26",
  "appium:appPackage": "io.selendroid.testapp",
  "appium:appActivity": ".HomeScreenActivity",
  "appium:app": "D:\\Appium\\registering_users_project\\selendroid-test-app.apk",
  "appium:udid": "emulator-5554"
}

USER_NAME = 'Raed Eleyan'
EMAIL = 'raed@gmail.com'
PASSWORD = '123456'
NAME_LABEL = 'Eng. Raed'

desired_capabilities = AppiumOptions()
desired_capabilities.load_capabilities(DESIRED_CAPABILITIES)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=desired_capabilities)
user_register_btn = driver.find_element(By.ACCESSIBILITY_ID, 'startUserRegistrationCD')
user_register_btn.click()
user_name_element = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="io.selendroid.testapp:id/inputUsername"]')
user_name_element.send_keys(USER_NAME)
email_element = driver.find_element(By.ACCESSIBILITY_ID, 'email of the customer')
email_element.send_keys(EMAIL)
password_element = driver.find_element(By.XPATH, ' //android.widget.EditText[@resource-id="io.selendroid.testapp:id/inputPassword"]')
password_element.send_keys(PASSWORD)
name_element = driver.find_element(By.ID, 'io.selendroid.testapp:id/inputName')
name_element.clear()
name_element.send_keys(NAME_LABEL)
accept_data_checkbox_element = driver.find_element(By.CLASS_NAME, 'android.widget.CheckBox')
accept_data_checkbox_element.click()
register_user_btn = driver.find_element(By.ID, 'io.selendroid.testapp:id/btnRegisterUser')
register_user_btn.click()
driver.quit()




