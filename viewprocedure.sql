use BD;
DROP VIEW IF EXISTS Pacientes_Funcionarios;
CREATE VIEW Pacientes_Funcionarios AS

SELECT Hospital.Nome AS Nome_Hospital,Pacientes.Nome AS Nome_Paciente,Funcionarios.Nome AS
Nome_Funcionario,Funcionarios.Email,Profissao
FROM (((Funcionarios
RIGHT JOIN Hospital ON Funcionarios.Hospital_Codigo = Hospital.Codigo)
INNER JOIN Hospital_Pacientes ON Hospital_Pacientes.Hospital_Codigo = Hospital.Codigo)
INNER JOIN Pacientes ON Hospital_Pacientes.Pacientes_CPF = Pacientes.CPF);


use BD;
DROP PROCEDURE IF EXISTS EncontraFuncionario;
DELIMITER $$
CREATE PROCEDURE EncontraFuncionario(NOME varchar(65))
BEGIN
	SELECT Nome_Funcionario,Profissao,Email FROM Pacientes_Funcionarios
	WHERE Nome_Paciente = NOME;
END $$
DELIMITER ;

CALL EncontraFuncionario('Virgulino Ferreira');


DROP PROCEDURE IF EXISTS Total_Medicamentos;
DELIMITER $$
CREATE PROCEDURE Total_Medicamentos()
BEGIN
	SELECT Pacientes.Nome,SUM(Preço) AS TOTAL,
    IF(SUM(Preço)>50,"ELEGIVEL","NÃO ELEGIVEL") AS SUBSIDIO 
    FROM Medicamentos,Pacientes_Medicamentos,Pacientes
	WHERE CPF = Pacientes_CPF 
    AND Medicamentos_Codigo = Medicamentos.Codigo 
    GROUP BY Pacientes.Nome;
END $$
DELIMITER ;

CALL Total_Medicamentos()