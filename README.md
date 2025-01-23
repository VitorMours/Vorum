# Contexto
O Book Register é um sistema desenvolvido em **python**, **html**, **css** e 
**javascript** que serve para registrar posts dentro de um site, de forma que 
eles sao mostrados sem especificar o autor, mas sendo modificados apenas pelo 
mesmo.

Para a constuir o projeto faremos uso do micro-webframework **flask**, ele usa diversas outras bibliotecas para criar um servidor web python, que pode ser usado para o desenvolvimento de aplicações, servindo como back-end para elas.

O funcionamento do flask, por ser um micro-framework, se dá de maneira mínima, possuindo apenas o necessário para o funcionamento do mesmo, visando-se necessário a instalação de extensões dentro do nosso projeto, para a adição de funcionalidade que podem vir a ser necessárias. Algumas dessas extensões serão utilizadas no projeto são: 

- **Flask-SQLAlchemy:** ORM utilizado para comunicar entre o banco de dados e o back-end.
- **Flask-Migrate:** Extensão focada para afazer as migrações do banco de dado quando necessárias.
- **Flask-WTForms:** Extensão usada para fazer o processamento, e o uso com 
maior facilidade dos formularios.


# Instalação e Configuração Inicial
### Configurações do flask
Temos que algumas configurações devem ser feitas, para rodarmos o flask de maneira completa, e da maneira a qual ele foi pensada, sendo assim, podemos criar e rodar nossa aplicação de duas maneiras 

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
