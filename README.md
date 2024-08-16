# Contexto
O Book Register é um sistema desenvolvido em **python**, **html**, **css** e 
**javascript** que serve para registrar livros dentro de uma base de dados, de forma que possamos salvar nossos livros, a nossas leituras, editar elas, e deletar nossos registros.

Para isso, iremos fazer uso do micro-webframework **flask** para desenvolvermos nosso projeto, ele é uma biblioteca que usa diversas outras bibliotecas para criar um servidor web python, que pode ser usado para o desenvolvimento de aplicações, servindo como back-end para elas.

O funcionamento do flask, por ser um micro-framework, se dá de maneira mínima, possuindo apenas o necessário para o funcionamento do mesmo, visando-se necessário a instalação de extensões dentro do nosso projeto, para a adição de funcionalidade que podem vir a ser necessárias. Algumas dessas extensões serão utilizadas no projeto são: 

- **Flask-SQLAlchemy:** ORM utilizado para comunicar entre o banco de dados e o back-end
- **Flask-Migrate:** Extensão focada para afazer as migrações do banco de dado quando necessárias




# Instalação e Configuração Inicial
### Configurações do flask
Temos que algumas configurações devem ser feitas, para rodarmos o flask de maneira completa, e da maneira a qual ele foi pensada, sendo assim, podemos criar e rodar nossa aplicação de duas maneiras 

- Por meio do script `run.sh`
- por meio de comandos diretos no terminal

#### Usando o script bash


#### Rodando comandos no terminal


```bash
export FLASK_APP=src
```

Nesse caso, como temos que o nome da nossa aplicação se dá por src, que é a pasta que contém o código fonte da nossa aplicação, podemos então exportar ela como nossa aplicação


### Configuração de variáveis de ambiente 
As variáveis de ambiente são uma forma dentro de código, que podemos usar para guardar informações e configurações essenciais, de forma que elas estejam mais seguram, e não sejam expostas para o público.

# 



