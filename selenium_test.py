from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_domain():

    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    driver = webdriver.Chrome(options=options)

    driver.get("https://example.com")

    assert driver.title == "Example Domain"

    driver.quit()