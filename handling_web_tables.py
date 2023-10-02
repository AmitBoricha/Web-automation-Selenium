from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser():
    driver = webdriver.Chrome()
    return driver

def close_browser(driver):
    driver.quit()

def get_table_data(driver, table_id):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, table_id)))
        table = driver.find_element(By.ID, table_id)
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [column.text for column in columns]
            table_data.append(row_data)