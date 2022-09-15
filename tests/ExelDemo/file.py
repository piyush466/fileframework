from selenium.webdriver.common.by import By

import XLutils

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()


# path = r"C:\Users\Cliffex-Lead\Documents\piyushexcel.xlsx"


driver.find_element(By.NAME,"userName").send_keys("op")

driver.find_element(By.NAME,"password").send_keys("dgsfgsdf213")

driver.find_element(By.NAME,"submit").click()
