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

        return table_data
        except:
        print("Table with ID '{}' not found.".format(table_id))
        return None
# Example usage:
if __name__ == "__main__":
    driver = open_browser()
    driver.get("https://www.example.com")
    # Locate and extract data from a table with the specified ID
    table_id = "example-table"
    table_data = get_table_data(driver, table_id)

    if table_data:
        for row in table_data:
            print(" | ".join(row))  # Print table data with pipe separators