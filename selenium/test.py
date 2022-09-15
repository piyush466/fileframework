from selenium import
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get('https://dev.mmabetclub.com/login')


print(driver.title) # title of the page

print(driver.current_url)

print(driver.page_source)
