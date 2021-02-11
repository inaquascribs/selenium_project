import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import data_generation

from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseView(unittest.TestCase):
    # should driver be global, or is it enough to be only in setup?
    #global driver
    #driver = webdriver.Chrome().get("https://wizzair.com/pl-pl#/")

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 60)
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        login_btn.click()
        register_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="registration"]')))
        register_btn.click()

    def tearDown(self):
        self.driver.quit()

    def firstName(self,name_field):
        # in data_generation code in define name by gender
        # todo czy ta metoda i metoda gender będą lecieć osobno? ujednolicić gender tu i w metodzie gender\
        click_name = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'firstName')))
        click_name = self.driver.find_element_by_name("firstName").send_keys(name_field)



    sleep(10)