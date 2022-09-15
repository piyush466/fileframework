import time
#from selenium.webdriver.support.ui import webdriverWait
from telnetlib import EC
# from selenium.webdriver.chrome.service import Service

import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r'C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Shop").click()
time.sleep(2)
