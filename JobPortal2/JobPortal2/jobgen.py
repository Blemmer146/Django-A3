import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobPortal2.settings')
import django
django.setup()
from faker import Faker
from random import randint
from JobDetails.models import PuneJob, HyderabadJob, MumbaiJob

insertion = eval(input("Enter the number of fake jobs to be inserted: "))

def generate_mobile_number():
    """Generate a random mobile number starting with 6, 7, 8, or 9."""
    prefix = str(randint(6, 9))
    return prefix + ''.join(str(randint(0, 9)) for _ in range(9))

def create_fake_job(model):
    """Create a fake job entry in the specified model."""
    fake = Faker()
    return model.objects.create(
        company_name=fake.company(),
        designation=fake.job(),
        package=f"{randint(3, 20)} LPA",
        location=fake.city(),
        email=fake.company_email(),
        contact_number=generate_mobile_number()
    )

def store_fake_jobs(insertion):
    """Store fake jobs in the database."""
    for _ in range(insertion):
        create_fake_job(PuneJob)
        create_fake_job(HyderabadJob)
        create_fake_job(MumbaiJob)
    print(f"{insertion} fake jobs inserted successfully.")


store_fake_jobs(insertion)
