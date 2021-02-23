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
        click_name = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'firstName')))
        click_name = self.driver.find_element_by_name("firstName").send_keys(name_field)

    def lastName(self,surname_field):
        surname = self.driver.find_element_by_name("lastName")
        surname.send_keys(surname_field)
        self.driver.find_element_by_name("firstName").click()

    def gender(self,gender):
        if gender == 'female':
            actions = ActionChains(self.driver)
            sex = self.driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]')
            actions.move_to_element(sex).click().perform()
            actions.move_to_element_with_offset(sex,1,2)
        else:
            actions = ActionChains(self.driver)
            self.driver.find_element_by_xpath(
                '//div[@data-test="booking-register-country-code"]').click()
            sex = self.driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            actions.move_to_element(sex).click().perform()
            actions.move_to_element_with_offset(sex, 1, 2)

    def country_code(self,country_phone_code):
        # todo actions - make it general
        # actions = ActionChains(self.driver)
        # country_code_click = self.driver.find_element_by_xpath(
        #     '//div[@data-test="booking-register-country-code"]')
        # actions.move_to_element(country_code_click).click().perform()
        # actions.move_to_element_with_offset(country_code_click,1,2)
        self.driver.find_element_by_xpath(
                 '//div[@data-test="booking-register-country-code"]').click()
        self.driver.find_element_by_name(
            'phone-number-country-code').send_keys(country_phone_code + Keys.RETURN)

    def phone(self,phone_number):
        # todo zmień zmienną w danych, GB i PL. Uwarunkuj długości numerów
        self.driver.find_element_by_name("phoneNumberValidDigits").send_keys(phone_number)

    def email(self,mail):
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-email"]').send_keys(
            mail)

    def generate_password(self, password):
        password_input = self.driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        password_input.send_keys(password+Keys.TAB)
        sleep(10)
        #password_input.click()

    def nationality(self,country_code):
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-country"]').click()
        country_container = self.driver.find_element_by_xpath(
            '//div[@class="register-form__country-container__locations"]')
        countries = country_container.find_elements_by_tag_name('label')
        for country in countries:
            option = country.find_element_by_tag_name('small')
            option.get_attribute('innerText')
            if option.get_attribute('innerText') == country_code:
                # scroll to element
                option.location_once_scrolled_into_view
                # clicl
                option.click()
                # leave loop
                break


    def privacy_policy(self):
        #self.driver.find_element_by_xpath('//input[@data-test="booking-register-password"]').click()
        action = ActionChains(self.driver)
        policy_checkbox = self.driver.find_element_by_xpath('//label[@for="checkbox-privacyPolicy"]/i')
        action.move_to_element(policy_checkbox).click().perform()

    def terms_conditions(self):
        action = ActionChains(self.driver)
        terms_and_conditions_checkbox = self.driver.find_element_by_xpath(
            '//label[@for="checkbox-wizzAccountPolicy"]/i')
        action.move_to_element(terms_and_conditions_checkbox).click().perform()

    def newsletter(self):
        action = ActionChains(self.driver)
        newsletter_checkbox = self.driver.find_element_by_name(
            'newsletter')
        action.move_to_element(newsletter_checkbox).click().perform()
        action.move_to_element_with_offset(newsletter_checkbox,1,2)

    # def error_list(self):
    #     error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
    #     visible_error_notices = []
    #     for error in error_notices:
    #         if error.is_displayed():
    #             visible_error_notices.append(error)

    sleep(10)