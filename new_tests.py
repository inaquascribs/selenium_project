import unittest
from time import sleep

import new_basic_code
import data_generation
from faker import Faker
fake = Faker()



class EnterEmptyName(new_basic_code.BaseView, unittest.TestCase):
    def testInsertEmptyName(self):
        #insert correct and incorrect data
        self.firstName("")
        self.lastName(data_generation.lastname)
        #print(data_generation.lastname)
        self.gender(data_generation.gender)
        #print(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        #saving visible errors
        for error in error_notices:
             if error.is_displayed():
                 visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,
                         'Wpisz imię pasażera w formie, w której zostało przedstawione w dokumencie podróżnym. Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!')


 #       sleep(10)

    def testInsertSpecialLettersFirstName(self):
        # insert correct and incorrect data
        self.firstName(data_generation.polish_letters)
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        # test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1


        self.assertEqual(visible_error_notices[0].text, 'Nieprawidłowy znak')

    def testInsertEmptySurname(self):
        # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName("")
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,
                         'Wpisz nazwisko pasażera w formie, w której zostało przedstawione w dokumencie podróżnym. Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!')

    def testInsertSpecialLettersSurname(self):
        # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.polish_letters)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        # test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text, 'Nieprawidłowy znak')

    def testNoGenderSelect(self):
        # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        # test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,"Wybierz")

    def testNoCountryCode(self):
        # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)

        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        # test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,"Wybierz")

    def testNoPhoneNumber(self):
    # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text, 'Podaj numer telefonu')

    def testWrongPhoneNumber(self):
    # insert correct and incorrect data
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.name_by_gender())
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(fake.lexify())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        #self.assertEqual(visible_error_notices[0].text,'Podaj prawidłowy numer telefonu')

    def testEmptyPhoneNumber(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.name_by_gender())
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone('      ')
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        # test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        # self.assertEqual(visible_error_notices[0].text,'Podaj prawidłowy numer telefonu')

    def testWrongEmail(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(fake.lexify())
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

            #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                 visible_error_notices.append(error)
        for v in visible_error_notices:
             print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,"Nieprawidłowy adres e-mail.")

    def testWrongEmailDomain(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.wrong_mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

            #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                 visible_error_notices.append(error)
        for v in visible_error_notices:
             print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,"Nieprawidłowy adres e-mail")

    def testWrongPassword(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(fake.lexify())
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

            #test
        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                 visible_error_notices.append(error)
        for v in visible_error_notices:
             print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text,"Wpisz hasło")

    def testNoNationality(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.terms_conditions()
        self.privacy_policy()
        self.newsletter()

        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        self.assertEqual(visible_error_notices[0].text, "Podaj kraj")

    def testNoNewsletter(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.privacy_policy()

        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 0

    def testNoTermsConditions(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.newsletter()
        self.privacy_policy()

        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

    def testNoPrivacyPolicy(self):
        self.firstName(data_generation.name_by_gender())
        self.lastName(data_generation.lastname)
        self.gender(data_generation.gender)
        self.country_code(data_generation.country_phone_code)
        self.phone(data_generation.generate_phone_number())
        self.email(data_generation.mail)
        self.generate_password(data_generation.password)
        self.nationality(data_generation.country_code)
        self.terms_conditions()
        self.newsletter()

        error_notices = self.driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_error_notices = []
        # saving visible errors
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1