from faker import Faker
import requests
import secrets
fake = Faker("pt_BR")

lero_lero_url = "https://baconipsum.com/api/?type=meat-and-filler"




def create_user() -> list:
        
        person = fake.profile()
        
        name = person['name']
        mail = person['mail']
        password = secrets.token_urlsafe(13)

        return [name, mail, password]



def create_post() -> list:
        request = requests.get(lero_lero_url)
        lero_lero = request.text
        
        title = lero_lero
        description = lero_lero
        return 




if __name__ == "__main__":
        print(create_user())