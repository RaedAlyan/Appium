from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from desired_caps import contacts

appium_options = UiAutomator2Options().load_capabilities(contacts)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)

# locate all contacts.
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")

# Create an instance from ActionChains class.
actions = ActionChains(driver)

# Create a "touch" type of pointer input. By default, it is "mouse"
touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')

# Override pointer action as 'touch'
actions.w3c_actions = ActionBuilder(driver, mouse=touch_input)

# Press and Hold using W3C actions on first contact
actions.w3c_actions.pointer_action.click_and_hold(contacts[0])
actions.perform()

# Get element coordinates (position in the page)
# element_coord = contacts[0].location
# Long press using W3C Mobile Gestures Commands
# driver.execute_script('mobile: longClickGesture', {'x': element_coord['x'], 'y': element_coord['y'],
#                                                    'duration': 1000})
driver.quit()
