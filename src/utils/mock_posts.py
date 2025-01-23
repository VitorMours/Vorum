import random
import string
import requests
import secrets

lero_lero_url = "https://baconipsum.com/api/?type=meat-and-filler"

def generate_random_string(length=10):
    # Gera uma string aleatória de letras e números
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_name():
    # Gera um nome fictício simples com random
    first_name = generate_random_string(5).capitalize()
    last_name = generate_random_string(7).capitalize()
    return f"{first_name} {last_name}"

def generate_random_email():
    # Gera um e-mail fictício simples
    return f"{generate_random_string(5)}@example.com"

def create_user() -> list:
    # Gerar um usuário fictício com nome, e-mail e senha
    name = generate_random_name()
    mail = generate_random_email()
    password = secrets.token_urlsafe(13)
    
    print(f"Name: {name}, Email: {mail}, Password: {password}")

    return [name, mail, password]

def create_post() -> list:
    # Gerar um post fictício com título e descrição
    title = generate_random_string(10)
    description = generate_random_string(20)
    
    print(f"Title: {title}, Description: {description}")
        
    request = requests.get(lero_lero_url)
    lero_lero = request.text
    
    title = lero_lero[:10]
    description = lero_lero[:20]

    return [title, description, lero_lero] 

if __name__ == "__main__":
    print(create_user())
