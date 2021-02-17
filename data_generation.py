from faker import Faker
from faker_e164.providers import E164Provider

fake = Faker(['en_GB'])

#person data
gender = fake.random_element(['male','female'])

def name_by_gender():
    if gender == 'male':
        firstname = fake.first_name_male()
    else:
        firstname = fake.first_name_female()
    return firstname



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
phone_number = fake.phone_number()

#email
mail = fake.email()
#password
password = fake.password(length=10, digits=True, upper_case=True, lower_case=True, special_chars = False)

