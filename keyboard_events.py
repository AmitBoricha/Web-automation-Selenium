from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# Open a web page
driver.get("https://www.example.com")

text_input_field = driver.find_element_by_id("input_field_id")