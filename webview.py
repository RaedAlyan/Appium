from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.options.android import UiAutomator2Options
from time import sleep


desired_cap = {
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main",
    "platformName": "Android",
    "deviceName": "Pixel 8 Pro API 26",
    "udid": "emulator-5554",
    "chromedriverExecutable": "D:\\Files\\Appium\\Chrome Driver\\chromedriver-win32_128.0.6613.84\\chromedriver.exe"

}

appium_options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.implicitly_wait(120)
continue_button = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/signin_fre_continue_button')
continue_button.click()
thanks_button = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/button_secondary')
thanks_button.click()
ack_button = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/ack_button')
ack_button.click()
search_box = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/search_box_text')
search_box.send_keys('Python')
driver.press_keycode(66)  # to press Enter.
sleep(5)
contexts = driver.contexts
print(f'Available contexts are: {contexts}')
webview_context = [context for context in contexts if 'WEBVIEW' in context]
if webview_context:
    driver.switch_to.context(webview_context[0])
    print(f'Switched to WebView context: {driver.current_context}')
    python_link = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.XPATH,
                                        '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/a/div/div[2]/div'))
    )
    python_link.click()
    print(f'The current title is: {driver.title}')
    driver.switch_to.context('NATIVE_APP')  # return back to the NATIVE_APP context.
else:
    print("WebView context not found")
driver.quit()
