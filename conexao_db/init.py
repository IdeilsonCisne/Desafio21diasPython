"""
show database;
create database desafio_21_dias_python;
use desafio_21_dias_python;

CREATE TABLE usuarios (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(30) NOT NULL,
  email VARCHAR(100) NOT NULL,
  endereco VARCHAR(255),
  data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;

#Inserir novos dados na tabela
insert into usuarios(nome, email, endereco)
values('Ideilson', 'ideilson.cisne@gmail.com', 'Rua teste');

#atualizar campos da tabela
update usuarios set nome = 'de', email = 'teste', endereco = 'teste'
where id = 1;

#deletar
delete from usuarios where id = 2;

https://pynative.com/python-mysql-database-connection/

# instalação diretamente no sistema operacional
pip install mysql-connector-python
pip install mysql-connector
pip install mysqlclient

# instalação diretamente no python
python -m pip install mysql-connector-python

python3 -m venv mysql_app
source conexao_db/mysql_app/bin/activate
"""


import mysql.connector
from mysql.connector import Error
import os

try:
  connection = mysql.connector.connect(host='os.getenv(HOST)',
                                       database='os.getenv(DATABASE)',
                                       user='os.getenv(USER)',
                                       password='os.getenv(PASS)')
  if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

except Error as e:
  print("Error while connecting to MySQL", e)
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
