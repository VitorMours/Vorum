from faker import Faker
from random import choice
import requests
import secrets

fake = Faker("pt_BR")

lero_lero_url = "https://baconipsum.com/api/?type=meat-and-filler"


def create_user() -> list:
        
        person = fake.profile()
        
        name = person['name']
        mail = person['mail']
        password = secrets.token_urlsafe(13)
        print(person)

        return [name, mail, password]

def create_post() -> list:
        name = fake.name()
        email = fake.email()
        print(name)
        print(email)
        
        request = requests.get(lero_lero_url)
        lero_lero = request.text
        
        title = lero_lero[:10]
        description = lero_lero[:20]

        return [title, description, lero_lero] 




if __name__ == "__main__":
        print(create_user())