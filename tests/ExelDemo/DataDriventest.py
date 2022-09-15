from selenium.webdriver.common.by import By

import XLutils

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()


path = r"C:\Users\Cliffex-Lead\Documents\piyushexcel.xlsx"

row = XLutils.getRowCount(path,'Sheet1')

for r in range(2,row+1):
    username = XLutils.readData(path,'Sheet1',r,1)
    password = XLutils.readData(path,'Sheet1',r,2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//input[@name='submit']").click()

    if driver.title == "Login: Mercury Tours" :
        print("test is passes")
        XLutils.writeData(path,"Sheet1",r,3,"test passed")

    else:
        print("test failed")
        XLutils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element(By.LINK_TEXT, "Home").click()








