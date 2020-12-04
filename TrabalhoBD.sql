drop database BD;
create database BD;
use BD;
DROP TABLE IF EXISTS Hospital;
DROP TABLE IF EXISTS Funcionarios;
DROP TABLE IF EXISTS Telefone_Funcionario;
DROP TABLE IF EXISTS Hospital_Pacientes;
DROP TABLE IF EXISTS Recurso;
DROP TABLE IF EXISTS Hospital_Equipamentos;
DROP TABLE IF EXISTS Equipamentos;
DROP TABLE IF EXISTS Regiao;
DROP TABLE IF EXISTS Boletim_de_COVID;
DROP TABLE IF EXISTS Pacientes;
DROP TABLE IF EXISTS Telefones_Pacientes;
DROP TABLE IF EXISTS Testes;
DROP TABLE IF EXISTS Pacientes_Medicamentos;
DROP TABLE IF EXISTS Medicamentos;
DROP TABLE IF EXISTS Pacientes_Enfermidades;
DROP TABLE IF EXISTS Enfermidades;

CREATE TABLE  Regiao #######
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Nome 		varchar(65) NOT NULL,
	 Numero_de_Habitantes	INTEGER UNSIGNED NOT NULL
     );
CREATE TABLE  Hospital###########
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Nome 		varchar(65) NOT NULL,
	 Natureza	varchar(150) NOT NULL,
	 Endereço		varchar(150) NOT NULL,
     Orçamento 		float NOT NULL,
     Regiao_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Regiao_Codigo) references Regiao(Codigo)
     );
CREATE TABLE  Boletim_de_COVID
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Numero_de_Infectados	INTEGER UNSIGNED NOT NULL,
     Numero_de_Obitos	INTEGER UNSIGNED NOT NULL,
     Numero_de_Recuperados	INTEGER UNSIGNED NOT NULL,
     Numero_de_Testes	INTEGER UNSIGNED NOT NULL,
	 Data_de_Publicacao		DATE NOT NULL,
	 Status_de_Gravidade		varchar(65) NOT NULL,
     Taxa_de_Transmissao_COVID 		FLOAT NOT NULL,
	 Regiao_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Regiao_Codigo) references Regiao(Codigo)
     );
CREATE TABLE  Funcionarios ###########
	(CPF		INTEGER UNSIGNED PRIMARY KEY,
	 Nome 		varchar(65) NOT NULL,
     Profissao 		varchar(65) NOT NULL,
     Data_de_Nascimento 	DATE NOT NULL,
	 Salario	FLOAT NOT NULL,
	 Endereço		varchar(150) NOT NULL,
     Email 		varchar(65) NOT NULL,
     Hospital_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Hospital_Codigo) references Hospital(Codigo)
     );
CREATE TABLE  Telefone_Funcionario
	(Telefone		INTEGER UNSIGNED PRIMARY KEY,
	 Funcionarios_CPF INTEGER UNSIGNED,
     FOREIGN KEY (Funcionarios_CPF) references Funcionarios(CPF)
     );
CREATE TABLE  Recurso
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Finalidade 		varchar(65) NOT NULL,
     Origem 		varchar(65) NOT NULL,
     Hospital_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Hospital_Codigo) references Hospital(Codigo)
     );
CREATE TABLE  Equipamentos #########
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Nome 		varchar(65) NOT NULL,
     Ala 		varchar(65) NOT NULL,
     Quantidade INTEGER UNSIGNED NOT NULL
     );
CREATE TABLE  Hospital_Equipamentos
	(Hospital_Codigo INTEGER UNSIGNED,
     Equipamentos_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Hospital_Codigo) references Hospital(Codigo),
     FOREIGN KEY (Equipamentos_Codigo) references Equipamentos(Codigo)
     );
CREATE TABLE  Pacientes ##############
	(CPF		INTEGER UNSIGNED PRIMARY KEY,
	 Nome 		varchar(65) NOT NULL,
     Endereço 		varchar(65) NOT NULL,
     Email 		varchar(65) NOT NULL,
     Data_de_Nascimento DATE NOT NULL
     );
CREATE TABLE  Hospital_Pacientes
	(Hospital_Codigo INTEGER UNSIGNED,
     Pacientes_CPF INTEGER UNSIGNED,
     FOREIGN KEY (Hospital_Codigo) references Hospital(Codigo),
     FOREIGN KEY (Pacientes_CPF) references Pacientes(CPF)
     );
CREATE TABLE  Testes
	(Codigo		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 Tipo_de_Teste 		varchar(65) NOT NULL,
     Resultado 		varchar(65) NOT NULL,
     Origem 		varchar(65) NOT NULL,
     Pacientes_CPF INTEGER UNSIGNED,
     FOREIGN KEY (Pacientes_CPF) references Pacientes(CPF)
     );
CREATE TABLE  Enfermidades ########
	(Nome		varchar(65) PRIMARY KEY,
	 Gravidade 		varchar(65) NOT NULL,
     Natureza 		varchar(65) NOT NULL
     );
CREATE TABLE  Pacientes_Enfermidades
	(Pacientes_CPF INTEGER UNSIGNED,
	 Enfermidade_Nome varchar(65),
	 FOREIGN KEY (Pacientes_CPF) references Pacientes(CPF),
	 FOREIGN KEY (Enfermidade_Nome) references Enfermidades(Nome)
	 );
CREATE TABLE  Telefone_Pacientes
	(Telefone		INTEGER UNSIGNED PRIMARY KEY,
     Pacientes_CPF INTEGER UNSIGNED,
	 FOREIGN KEY (Pacientes_CPF) references Pacientes(CPF)
     );
CREATE TABLE  Medicamentos #########
	(Codigo INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
     Preço FLOAT NOT NULL
     );
CREATE TABLE  Pacientes_Medicamentos
	(Pacientes_CPF INTEGER UNSIGNED,
     Medicamentos_Codigo INTEGER UNSIGNED,
     FOREIGN KEY (Pacientes_CPF) references Pacientes(CPF),
     FOREIGN KEY (Medicamentos_Codigo) references Medicamentos(Codigo)
     );
     


     
     
     
     
     
     
     
     
     
     
     
     