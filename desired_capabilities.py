from selenium import webdriver

# Define desired capabilities for Chrome
chrome_capabilities = {
    "browserName": "chrome",
    "version": "latest",
    "platform": "ANY",
    "chromeOptions": {
        "args": ["--start-maximized", "--disable-extensions"]
    }
}

driver = webdriver.Chrome(desired_capabilities=chrome_capabilities)

# Perform actions with the WebDriver
driver.get("https://www.example.com")