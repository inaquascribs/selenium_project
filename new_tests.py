import unittest
from time import sleep

import new_basic_code
import data_generation
from faker import Faker
fake = Faker


class RegistrationForm(new_basic_code.BaseView, unittest.TestCase):
    def testInsertEmptyName(self):
        #insert correct and incorrect data
        self.firstName("")
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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
        #saving visible errors
        for error in error_notices:
             if error.is_displayed():
                 visible_error_notices.append(error)
        for v in visible_error_notices:
            print(v.text)
        print(len(visible_error_notices))
        assert len(visible_error_notices) == 1

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text,
                            'Wpisz imię pasażera w formie, w której zostało przedstawione w dokumencie podróżnym. Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!')
        else:
            self.assertEqual(visible_error_notices[0].text,
                             "Please add the passenger's first name as it appears in their travel document.\nPlease use letters without accents (e.g.: á, é, ő) and avoid using special characters!")

        #sleep(10)

    def testInsertSpecialLettersFirstName(self):
        # insert correct and incorrect data
        self.firstName(data_generation.polish_letters)
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Nieprawidłowy znak')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Invalid character')

    def testInsertEmptySurname(self):
        # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text,
                         'Wpisz nazwisko pasażera w formie, w której zostało przedstawione w dokumencie podróżnym. Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!')
        else:
            self.assertEqual(visible_error_notices[0].text,
                             "Please add the passenger's last name as it appears in their travel document.\nPlease use letters without accents (e.g.: á, é, ő) and avoid using special characters!")

    def testInsertSpecialLettersSurname(self):
        # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Nieprawidłowy znak')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Invalid character')

    def testNoGenderSelect(self):
        # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Wybierz')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Please select')

    def testNoCountryCode(self):
        # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Wybierz')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Please select')

    def testNoPhoneNumber(self):
    # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Podaj numer telefonu')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Please add a valid mobile phone number')
        sleep(10)

    def testWrongPhoneNumber(self):
    # insert correct and incorrect data
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.name_by_gender()))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Podaj numer telefonu')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Please add a valid mobile phone number')

    def testEmptyPhoneNumber(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.name_by_gender()))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Podaj numer telefonu')
        else:
            self.assertEqual(visible_error_notices[0].text, 'Please add a valid mobile phone number')

    def testWrongEmail(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, "Nieprawidłowy adres e-mail")
        else:
            self.assertEqual(visible_error_notices[0].text,  'Invalid e-mail')

    def testWrongEmailDomain(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, "Nieprawidłowy adres e-mail")
        else:
            self.assertEqual(visible_error_notices[0].text, 'Invalid e-mail')

    def testWrongPassword(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, "Wpisz hasło")
        else:
            self.assertEqual(visible_error_notices[0].text, "Please add your password")

    def testNoNationality(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Ten kraj nie istnieje.')
        else:
            self.assertEqual(visible_error_notices[0].text, 'This is a non-existing country.')

    def testNoNewsletter(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text, 'Aby kontynuować, musisz wyrazić zgodę na zasady i warunki konta WIZZ.')
        else:
            self.assertEqual(visible_error_notices[0].text, 'You must accept the WIZZ Account Terms and Conditions to continue.')

    def testNoPrivacyPolicy(self):
        self.firstName(data_generation.removeAccents(data_generation.name_by_gender()))
        self.lastName(data_generation.removeAccents(data_generation.lastname))
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

        if data_generation.fake.locales == ["pl_PL"]:
            self.assertEqual(visible_error_notices[0].text,
                             'Aby kontynuować, musisz wyrazić zgodę na politykę prywatności.')
        else:
            self.assertEqual(visible_error_notices[0].text,
                             'You must accept the privacy policy to continue.')

