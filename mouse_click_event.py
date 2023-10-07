from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Initialize the WebDriver
driver = webdriver.Chrome()

driver.get("https://www.example.com")

# Locate the element to click
element_to_click = driver.find_element_by_id("element_id")

# Create an ActionChains object
action = ActionChains(driver)