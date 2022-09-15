# from selenium.webdriver.support.ui import webdriverWait
from telnetlib import EC
# from selenium.webdriver.chrome.service import Service
import pytest
import driver
import time
import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from pageObject.homePage import HomePage
from utilities.Baseclsass import Baseclass


@pytest.mark.usefixtures("setup")

class TestOne(Baseclass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shoItems().click()
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        time.sleep(2)
        print(self.driver.find_element(By.XPATH, "//div[@class='card h-100']/div/h4/a").text)
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td/button[@class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        final = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert "Thank you!" in final



        # self.driver.close()

        # product = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # for products in product:
        #     print(products.driver.find_element(By.XPATH, "div/h4/a").text)






