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

-- DATABASE TRABALHO EM GRUPO SENAC MODULO 3 --

CREATE DATABASE escola;
USE escola;

CREATE TABLE aluno( 
id_aluno INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
nome VARCHAR(60) NOT NULL,
cpf VARCHAR(11) NOT NULL,
email VARCHAR(50) NOT NULL,
telefone VARCHAR(11) NOT NULL,
endereco_completo VARCHAR(100) NOT NULL
);

CREATE TABLE turma(
id_turma INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
numero_sala INT(6) NOT NULL,
turno VARCHAR (20) NOT NULL
);

CREATE TABLE curso(
id_curso INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
nome_curso VARCHAR(40) NOT NULL,
data_inicio DATE NOT NULL,
data_termino DATE NOT NULL
);

CREATE TABLE modulos(
id_modulo INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
data_inicio DATE NOT NULL,
data_termino DATE NOT NULL
);

CREATE TABLE disciplina(
id_disciplina INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
nome_disciplina VARCHAR(50) NOT NULL
);

CREATE TABLE facilitador(
id_facilitador INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
nome VARCHAR(60) NOT NULL,
cpf VARCHAR(11) NOT NULL,
email VARCHAR(50) NOT NULL,
telefone VARCHAR(11) NOT NULL,
endereco_completo VARCHAR(100) NOT NULL,
disciplina VARCHAR(50) NOT NULL
);

ALTER TABLE aluno
ADD COLUMN id_turma INT(11) NOT NULL,
ADD CONSTRAINT fk_id_turma FOREIGN KEY (id_turma) REFERENCES turma(id_turma);

ALTER TABLE turma
ADD COLUMN id_curso INT(11) NOT NULL,
ADD CONSTRAINT fk_id_curso_turma FOREIGN KEY (id_curso) REFERENCES curso(id_curso);

ALTER TABLE disciplina
ADD COLUMN id_modulo INT(11) NOT NULL,
ADD CONSTRAINT fk_id_modulo FOREIGN KEY (id_modulo) REFERENCES modulos(id_modulo);

ALTER TABLE disciplina
ADD COLUMN id_facilitador INT(11) NOT NULL,
ADD CONSTRAINT fk_id_facilitador FOREIGN KEY (id_facilitador) REFERENCES facilitador(id_facilitador);

ALTER TABLE modulos
ADD COLUMN id_curso INT(11) NOT NULL,
ADD CONSTRAINT fk_id_curso_modulos FOREIGN KEY (id_curso) REFERENCES curso(id_curso);

INSERT INTO facilitador(nome, cpf, email, telefone, endereco_completo, disciplina) VALUES 
('Pedro', '12345678917', 'pedro@gmail.com', '21977777777', 'Rua oito do dez N 6', 'Programação Avançada'),
('Fernanda', '12345678918', 'fernanda@gmail.com', '21988888888', 'Rua nove do doze N 7', 'Gestão Empresarial'),
('Roberto', '12345678919', 'roberto@gmail.com', '21999999999', 'Rua dez do quatorze N 8', 'Banco de Dados');

INSERT INTO disciplina(nome_disciplina, id_modulo, id_facilitador) VALUES 
('Programação Avançada', 1, 1),
('Gestão Empresarial', 2, 2),
('Banco de Dados', 3, 3);

INSERT INTO modulos(data_inicio, data_termino, id_curso) VALUES 
('2022-01-15', '2022-05-30', 1),
('2022-06-01', '2022-10-30', 1),
('2022-02-01', '2022-06-30', 2),
('2022-07-01', '2022-11-30', 2),
('2022-03-10', '2022-07-31', 3);

INSERT INTO curso(nome_curso, data_inicio, data_termino) VALUES 
('Engenharia de Software', '2022-01-15', '2023-12-20'),
('Administração', '2022-02-01', '2023-11-30'),
('Ciência da Computação', '2022-03-10', '2023-10-15');

INSERT INTO turma(numero_sala, turno, id_curso) VALUES 
(101, 'Manhã', 1),
(202, 'Tarde', 2),
(303, 'Noite', 1);

INSERT INTO aluno(nome, cpf, email, telefone, endereco_completo, id_turma) VALUES 
('Ana', '12345678912', 'ana@gmail.com', '21922222222', 'Rua três do quatro N 1', 1),
('Lucas', '12345678913', 'lucas@gmail.com', '21933333333', 'Rua quatro do seis N 2', 2),
('Carla', '12345678914', 'carla@gmail.com', '21944444444', 'Rua cinco do oito N 3', 1),
('Mariana', '12345678915', 'mariana@gmail.com', '21955555555', 'Rua seis do dez N 4', 1),
('João', '12345678916', 'joao@gmail.com', '21966666666', 'Rua sete do doze N 5', 2);

