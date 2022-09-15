import pytest
from selenium import webdriver
# from selenium.webdriver.support.ui import webdriverWait
from telnetlib import EC
# from selenium.webdriver.chrome.service import Service
import pytest
import time
import driver
import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r'C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe')

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\firefox\geckodriver.exe")
    # elif browser_name == "IE":
    #     #IE
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    time.sleep(2)
    request.cls.driver = driver
    yield
    # driver.close()
