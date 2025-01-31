# Contexto
O Vorum é um sistema desenvolvido em **python**, **html**, **css** e 
**javascript** que funciona simulando o funcionamento de um forum, em que 
diversos usuários podem fazer login, e publicarem posts de autoria própria, 
de forma em que a customização e a adição de novos elementos são possibilidades
em todo o momento de criação e edição das postagens.


Para a constuir o projeto foi usado o micro-webframework **flask**, ele usa diversas outras bibliotecas para criar um servidor web python, que pode ser usado para o desenvolvimento de aplicações, servindo como back-end para elas.

O funcionamento do flask, por ser um micro-framework, se dá de maneira mínima, possuindo apenas o necessário para o funcionamento do mesmo, visando-se necessário a instalação de extensões dentro do projeto, para a adição de funcionalidade que podem vir a ser necessárias. Algumas dessas extensões são: 

- **Flask-SQLAlchemy:** ORM utilizado para comunicar entre o banco de dados e o back-end.
- **Flask-Migrate:** Extensão focada para afazer as migrações do banco de dado quando necessárias.
- **Flask-WTForms:** Extensão usada para fazer o processamento, e o uso com 
maior facilidade dos formularios.


# Instalação e Configuração Inicial
### Configurações do flask
Temos que algumas configurações devem ser feitas, para o flask funcionar corretamente,  sendo assim, podemos criar e rodar nossa aplicação de duas maneiras 

- Por meio do script `run.sh`
- por meio de comandos diretos no terminal

#### Usando o script bash

```sh
./run.sh
```

#### Rodando comandos no terminal

```sh
export FLASK_APP=src
flask --app src run
```

Nesse caso, como temos que o nome da nossa aplicação se dá por src, que é a pasta que contém o código fonte da nossa aplicação, podemos então exportar ela como nossa aplicação
