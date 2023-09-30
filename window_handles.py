from selenium import webdriver


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the first website
driver.get("https://www.google.com")

# Store the handle of the main window
main_window_handle = driver.window_handles[0]

# After opening the new window, the focus will shift to it automatically
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Switch to the newly opened window
new_window_handle = driver.window_handles[-1]
driver.switch_to.window(new_window_handle)