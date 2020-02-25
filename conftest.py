import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe", options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()
