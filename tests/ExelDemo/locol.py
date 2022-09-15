import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import XLutils

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")

driver.get("https://locol.partners/")
driver.maximize_window()
# path = r"C:\Users\Cliffex-Lead\Documents\locol.xlsx"
# row = XLutils.getRowCount(path,'Sheet1')
# driver.get('https://locol.partners/')
# driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#identifier").send_keys("piyush.dravyakar@gmail.com")

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("piyush@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(15)
time.sleep(2)
# driver.find_element(By.XPATH, "//a/i[@class='mr-1 bi bi-plus-lg']").click()

path = r"C:\Users\Cliffex-Lead\Documents\locol.xlsx"

row = XLutils.getRowCount(path,'Sheet1')
print(row, " &&&&&&&&&")
for r in range(2,row+1):
    driver.find_element(By.XPATH, "//a/i[@class='mr-1 bi bi-plus-lg']").click()
    print("-------------------", r)
    image = XLutils.readData(path,'Sheet1',r,1)
    itemNmae = XLutils.readData(path,'Sheet1',r,2)
    discription = XLutils.readData(path,'Sheet1',r,3)
    category = XLutils.readData(path, 'Sheet1', r, 4)
    subCategory = XLutils.readData(path, 'Sheet1', r, 5)
    price = XLutils.readData(path, 'Sheet1', r, 6)
    cta = XLutils.readData(path, 'Sheet1', r, 7)
    link = XLutils.readData(path, 'Sheet1', r, 8)

    driver.find_element(By.CSS_SELECTOR,"#up_file").send_keys(image)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(itemNmae)
    driver.find_element(By.CSS_SELECTOR, "#description").send_keys(discription)
    # Category
    driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[2]/div/main/form/div[2]/div[5]/div[2]/div/div/div[2]/div[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/main/form/div[2]/div[5]/div[2]/div/div/div[1]/div[2]/div/input").send_keys(Keys.ENTER)
    #subcategory
    driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/main/form/div[2]/div[6]/div[2]/div/div/div[2]/div[2]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/main/form/div[2]/div[6]/div[2]/div/div/div[1]/div[2]/div/input").send_keys("testing", Keys.ENTER)
    #price
    driver.find_element(By.CSS_SELECTOR, "#price").send_keys(price)
    #cta
    driver.find_element(By.NAME, "action").send_keys(cta)
    #link
    driver.find_element(By.NAME, "forwardLink").send_keys(link)

    driver.find_element(By.XPATH, "//button[text()='Save Changes']").click()
    driver.execute_script("window.scrollBy(1000,0)")
    time.sleep(9)
    # driver.execute_script("window.scrollBy(1000,0)")

driver.close()










# driver.find_element(By.XPATH, "//a/i[@class='mr-1 bi bi-plus-lg']").click()
#
# driver.find_element(By.XPATH, "//button[text()='Save Changes']").click()
# # a[href*='about_privacy']
#
# driver.implicitly_wait(15)
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"#up_file").send_keys(r"C:\Users\Cliffex-Lead\Downloads\images (21).jpg")

# driver.find_element(By.CSS_SELECTOR, "#name").send_keys("piyush")
# driver.find_element(By.CSS_SELECTOR, "#description").send_keys("description")


# Category
# a = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[2]/div/main/form/div[2]/div[5]/div[2]/div/div/div[2]/div[2]")
# time.sleep(2)
# a.click()
# time.sleep(1)
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/main/form/div[2]/div[5]/div[2]/div/div/div[1]/div[2]/div/input").send_keys(Keys.ENTER)
#
# #Sub-category
# driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/main/form/div[2]/div[6]/div[2]/div/div/div[2]/div[2]").click()
# time.sleep(0.5)
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/main/form/div[2]/div[6]/div[2]/div/div/div[1]/div[2]/div/input").send_keys("testing", Keys.ENTER)

# driver.find_element(By.CSS_SELECTOR, "#price").send_keys(20)

# driver.find_element(By.NAME, "action").send_keys("Buy")

# driver.find_element(By.NAME, "forwardLink").send_keys("https://www.facebook.com/")
#
# driver.find_element(By.XPATH, "//button[text()='Save Changes']").click()
# time.sleep(2)
# driver.close()









