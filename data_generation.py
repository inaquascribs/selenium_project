from faker import Faker
from faker_e164.providers import E164Provider

PL = 'pl_PL'
UK = 'en_GB'

fake = Faker([PL])

#person data
gender = fake.random_element(['male','female'])

def name_by_gender():
 #   fake = Faker([UK])
    if gender == 'male':
        firstname = fake.first_name_male()
    else:
        firstname = fake.first_name_female()
    return firstname
# name_by_gender()
polish_letters = fake.bothify(text='??????', letters='ążźęćśńół')
#print(polish_letters)
lastname = fake.last_name()

# country, adress
postode = fake.postcode()
street_name = fake.street_name()
building_number = fake.building_number()
country = fake.country()
country_code = fake.country_code()
city = fake.city()

#phone
country_phone_code = fake.country_calling_code()
fake.add_provider(E164Provider)

def generate_phone_number():
    if fake == Faker([PL]):
        phone_number = fake.numerify(text='#########')
    else:
        phone_number = fake.numerify(text='##########')
    return phone_number


#email

mail = fake.email()
wrong_mail = fake.bothify(text='??????') + "@" + fake.bothify(text='??.##')

#print(wrong_mail)
#password
password = fake.password(length=10, digits=True, upper_case=True, lower_case=True, special_chars = False)

