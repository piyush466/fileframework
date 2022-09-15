from selenium.webdriver.common.by import By



from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

driver.find_element(By.NAME, "userName").send_keys("mercury")
driver.find_element(By.NAME, "password").send_keys("mercury")

driver.find_element(By.XPATH, "//input[@name='submit']").click()
print(driver.title)


