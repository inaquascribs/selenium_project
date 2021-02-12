import unittest
from time import sleep

import new_basic_code
import data_generation
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


class EnterEmptyName(new_basic_code.BaseView, unittest.TestCase):

    def testInsertEmptyName(self):
        self.firstName("")
        self.lastName(data_generation.lastname)
        #print(data_generation.lastname)
        self.gender(data_generation.gender)
        #print(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.phone_number)
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()



        sleep(10)