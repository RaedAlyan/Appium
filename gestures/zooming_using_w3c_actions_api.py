from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from desired_caps import maps
from time import sleep


appium_options = UiAutomator2Options().load_capabilities(maps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_options)
driver.implicitly_wait(15)

window_size = driver.get_window_size()
center_x = window_size['width']/2
center_y = window_size['height']/2

actions = ActionChains(driver)

finger1 = actions.w3c_actions.add_pointer_input('touch', 'finger1')
finger2 = actions.w3c_actions.add_pointer_input('touch', 'finger2')

# Zoom In
finger1.create_pointer_move(x=center_x-100, y=center_y)
finger1.create_pointer_down(button=MouseButton.LEFT)
finger1.create_pause(0.5)
finger1.create_pointer_move(x=center_x-500, y=center_y, duration=50)
finger1.create_pointer_up(button=MouseButton.LEFT)

finger2.create_pointer_move(x=center_x+100, y=center_y)
finger2.create_pointer_down(button=MouseButton.LEFT)
finger2.create_pause(0.5)
finger2.create_pointer_move(x=center_x+500, y=center_y, duration=50)
finger2.create_pointer_up(button=MouseButton.LEFT)

actions.perform()
sleep(5)

# Zoom Out
finger1.create_pointer_move(x=center_x-500, y=center_y)
finger1.create_pointer_down(button=MouseButton.LEFT)
finger1.create_pause(0.5)
finger1.create_pointer_move(x=center_x-100, y=center_y, duration=50)
finger1.create_pointer_up(button=MouseButton.LEFT)

finger2.create_pointer_move(x=center_x+500, y=center_y)
finger2.create_pointer_down(button=MouseButton.LEFT)
finger2.create_pause(0.5)
finger2.create_pointer_move(x=center_x+100, y=center_y, duration=50)
finger2.create_pointer_up(button=MouseButton.LEFT)

actions.perform()
driver.quit()
