import unittest
import basic_code
from time import sleep
from selenium import webdriver



class Wizztest(unittest.TestCase, basic_code.FillRegistration):
    def setUp(self):
        self.driver = webdriver.Chrome().get("https://wizzair.com/pl-pl#/")
  #      self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testInsertName(self):
        basic_code.name_field = 'null'

        # look up all errors
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        # create an empty list for visible errors:
        visible_error_notices = []
        # insert visible errors into the list
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)

        print(len(visible_error_notices))
        for v in visible_error_notices:
            print(v.text)
        assert len(visible_error_notices) == 1

        # asercja z klasy testcase
        self.assertEqual(visible_error_notices[0].text, 'Wpisz imię pasażera')

        sleep(10)

if __name__ == "__main__":
    unittest.main(verbosity=2)


