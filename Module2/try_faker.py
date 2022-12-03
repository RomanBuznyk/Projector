from faker import Faker
from try_faker import create_user


fake = Faker()
def create_user(name: str, password: str):
    print(fake.name())
print(create_user('name', 'pass'))

