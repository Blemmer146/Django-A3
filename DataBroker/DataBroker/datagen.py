import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataBroker.settings')
import django
django.setup()
from faker import Faker
from random import randint
from DataFaker.models import FakeUser

insertion=eval( input("Enter the number of fake users to be inserted: "))


def mob():
    d=randint(6,9)
    ph=''+str(d)
    for i in range(9):
        ph+=str(randint(0,9))
    return int(ph)

def store(insertion):
    for i in range(insertion):
        fake=Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()
        fake_phone_number = mob()
        fake_age = randint(18, 65)
        FakeUser.objects.create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email,
            phone_number=fake_phone_number,
            age=fake_age
        )
    print(f"{insertion} fake users inserted successfully.")

store(insertion)