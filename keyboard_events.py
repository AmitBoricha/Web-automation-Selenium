from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# Open a web page
driver.get("https://www.example.com")

text_input_field = driver.find_element_by_id("input_field_id")

# Create an ActionChains object
action = ActionChains(driver)

# Perform a keyboard event (typing text) in the input field
text_to_type = "Hello, Selenium"
action.send_keys_to_element(text_input_field, text_to_type).perform()

# Close the browser
driver.quit()