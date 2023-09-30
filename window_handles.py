from selenium import webdriver


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the first website
driver.get("https://www.google.com")

# Store the handle of the main window
main_window_handle = driver.window_handles[0]