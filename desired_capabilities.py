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