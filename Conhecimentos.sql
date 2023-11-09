CREATE DATABASE Floricultura
USE Floricultura;

CREATE TABLE cliente(
codcliente INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
cpf INT(11) NOT NULL,
rg INT(9) NOT NULL,
nome VARCHAR(50) NOT NULL,
telefone INT(11) NOT NULL,
endereco VARCHAR(40) NOT NULL,
email VARCHAR(30) NOT NULL
);

CREATE TABLE produto(
codproduto INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
valor FLOAT(10) NOT NULL,
tipo VARCHAR(20) NOT NULL,
quantidade INT(10) NOT NULL
);

CREATE TABLE pedido(
datacompra DATE NOT NULL,
codcliente INT(10) NOT NULL,
codproduto INT(10) NOT NULL,
FOREIGN KEY (codcliente) REFERENCES cliente(codcliente),
FOREIGN KEY (codproduto) REFERENCES produto(codproduto)
);
