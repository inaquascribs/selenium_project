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
        #self.name_field.send_keys(data_generation.name_by_gender())

        # click_name = wait.until(
        #         EC.element_to_be_clickable((By.NAME, 'firstName')))
        self.firstName(""+ Keys.RETURN)
        sleep(10)