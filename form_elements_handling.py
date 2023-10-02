from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.example.com")

text_box = driver.find_element_by_id("username")
text_box.clear()
text_box.send_keys("my_username")
