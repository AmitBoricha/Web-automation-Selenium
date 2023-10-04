from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.example.com")

# Locate and select a checkbox element
checkbox = driver.find_element_by_id("checkbox_id")  # Replace with the actual element locator
if not checkbox.is_selected():
    checkbox.click()  # Select the checkbox

radio_button = driver.find_element_by_id("radio_button_id")  # Replace with the actual element locator
if not radio_button.is_selected():
    radio_button.click()  # Select the radio button


# Close the browser
driver.quit()