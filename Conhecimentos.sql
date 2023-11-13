-- DATABASE DE ESCOLA, TRABALHO EM GRUPO MÓDULO 1 --

CREATE DATABASE escola;
USE escola;

CREATE TABLE aluno(
id_aluno INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
telefone INT(11) NOT NULL,
email VARCHAR(30) NOT NULL,
endereco VARCHAR(30) NOT NULL,
complemento_endereco VARCHAR(30),
cpf INT(11) NOT NULL
);

CREATE TABLE facilitador(
id_facilitador INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
telefone INT(11) NOT NULL,
email VARCHAR(30) NOT NULL,
endereço VARCHAR(30) NOT NULL,
complemento_endereco VARCHAR(30),
cpf INT(11) NOT NULL,
materia VARCHAR(30) NOT NULL
);

CREATE TABLE turma(
nome_turma VARCHAR(50) NOT NULL PRIMARY KEY,
numero_sala INT(5) NOT NULL
);

CREATE TABLE presença(
data_aula DATE NOT NULL
);

ALTER TABLE presença
ADD COLUMN id_aluno INT(11) NOT NULL,
ADD CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno);

ALTER TABLE presença
ADD COLUMN id_facilitador INT(11) NOT NULL,
ADD CONSTRAINT fk_id_facilitador FOREIGN KEY (id_facilitador) REFERENCES facilitador(id_facilitador);

ALTER TABLE presença
ADD COLUMN nome_turma VARCHAR(50) NOT NULL,
ADD CONSTRAINT fk_nome_turma FOREIGN KEY (nome_turma) REFERENCES turma(nome_turma);

CREATE TABLE reprovados(
data_rep DATE NOT NULL
);

ALTER TABLE reprovados
ADD COLUMN id_aluno INT(11) NOT NULL,
ADD CONSTRAINT fk2_id_aluno FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno);

ALTER TABLE reprovados 
ADD COLUMN nome_turma VARCHAR(50) NOT NULL,
ADD CONSTRAINT fk2_nome_turma FOREIGN KEY (nome_turma) REFERENCES turma(nome_turma);

-- DATABASE CONSULTÓRIO EXERCÍCIO --

CREATE DATABASE consultorio;
USE consultorio;

CREATE TABLE paciente(
id_paciente INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(70) NOT NULL
);

CREATE TABLE medico(
id_medico INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
crm VARCHAR(50) NOT NULL,
nome VARCHAR(70) NOT NULL,
epecializacao VARCHAR(50) NOT NULL
);

CREATE TABLE consulta(
id_consulta INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
data_consulta DATE NOT NULL
);

ALTER TABLE consulta
ADD COLUMN id_paciente INT(11) NOT NULL,
ADD CONSTRAINT fk_id_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente);

ALTER TABLE consulta
ADD COLUMN id_medico INT(11) NOT NULL,
ADD CONSTRAINT fk_id_medico FOREIGN KEY (id_medico) REFERENCES medico(id_medico);
