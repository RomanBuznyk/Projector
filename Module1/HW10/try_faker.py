from faker import Faker
import re

fake = Faker()

def password_check(password):
    x = True 
    while x:
        if (len(password)<=8):
            print = ('Not valid password: must contain at least 8 characters')
            break
        elif not re.search("[_@$]", password):
            print = ('Not valid password: must contain at least one non-alphabetic character')
            break
        elif re.search("\s" , password):
            break
        else:
            print("Valid Password")
            x = False
            break
    return

def create_user(name: str, password: str):
    if not name:
        name = fake.name()
    if not password:
        password = fake.password()
    print(f'user name is "{name}", password "{password}"')
    print(password_check(password))
    return name, password