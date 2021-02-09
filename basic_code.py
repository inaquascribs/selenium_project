from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import data_generation

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ReachRegistraion:
    #czy to tutaj, czy gdzie indziej? Muszę gdziesz jeszcze Firefox i Safari zrobić
#    self.driver = webdriver.Chrome().get("https://wizzair.com/pl-pl#/")
#    self.driver.maximize_window()
    def go_to_registration_page(self):
        wait = WebDriverWait(self.driver,60)
        login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        login_btn.click()
        register_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="registration"]')))
        register_btn.click()
class FillRegistration(ReachRegistraion):
    def name(self):
        #in data_generation code in define name by gender
        #czy ta metoda i metoda gender będą lecieć osobno? ujednolicić gender tu i w metodzie gender
        name_field = self.driver.find_element_by_name("firstName")
        name_field.send_keys(data_generation.name_by_gender())
        pass
    def surname(self):
        surname_field = self.driver.find_element_by_name("lastName")
        surname_field.send_keys(data_generation.lastname)
    def gender(self):
        if self.data_generation.gender == 'women':
            sex = self.driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]')
            sex.click()
        elif self.data_generation.gender == 'men':
            self.driver.find_element_by_name("firstName").click()
            sex = self.driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            sex.click()
        else:
            print('you gave wrong gender! We have only 2 at this site')
    def country_code(self):
        self.driver.find_element_by_xpath(
            '//div[@data-test="booking-register-country-code"]').click()
        self.driver.find_element_by_name(
            'phone-number-country-code').send_keys(data_generation.country_phone_code + Keys.RETURN)
    def phone(self):
        #zmień zmienną w danych, GB i PL. Uwarunkuj długości numerów
        self.driver.find_element_by_name("phoneNumberValidDigits").send_keys(data_generation.phone_number)
    def email(self):
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-email"]').send_keys(
            data_generation.mail + Keys.RETURN)
    def password(self):
        password_input = self.driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        password_input.send_keys(data_generation.password)
    def nationality(self):
        country_container = self.driver.find_element_by_xpath(
            '//div[@class="register-form__country-container__locations"]')
        countries = country_container.find_elements_by_tag_name('label')
        for country in countries:
            option = country.find_element_by_tag_name('small')
            option.get_attribute('innerText')
            if option.get_attribute('innerText') == data_generation.country_code:
                # przewijamy do elementu
                option.location_once_scrolled_into_view
                # klikamy
                option.click()
                # opuszczamy pętlę
                break

    def newsletter(self):
        action = ActionChains(self.driver)
        policy_checkbox = self.driver.find_element_by_xpath(
            '//label[@for="data-test="registration-newsletter-checkbox"]/i')
        action.move_to_element(policy_checkbox).click().perform()
    def privacy_policy(self):
        action2 = ActionChains(self.driver)
        policy_checkbox = self.driver.find_element_by_xpath('//label[@for="checkbox-privacyPolicy"]/i')
        action2.move_to_element(policy_checkbox).click().perform()
    def terms_conditions(self):
        action3 = ActionChains(self.driver)
        terms_and_conditions_checkbox = self.driver.find_element_by_xpath(
            '//label[@for="checkbox-wizzAccountPolicy"]/i')
        action3.move_to_element(terms_and_conditions_checkbox).click().perform()
