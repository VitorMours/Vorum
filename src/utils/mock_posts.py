from faker import Faker
import requests
from ..models import User 

fake = Faker("pt_BR")

lero_lero_url = "https://baconipsum.com/api/?type=meat-and-filler"




def create_post():
          request = requests.get(lero_lero_url)
          print(request.text)



          print("-"*60)
          print(fake.profile())




if __name__ == "__main__":
        create_post()