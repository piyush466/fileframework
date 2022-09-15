import driver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def shoItems(self):
        return self.driver.find_element(*HomePage.shop)
