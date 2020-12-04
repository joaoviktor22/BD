	use BD;
    insert into Regiao values(01,'A Norte',5000);
	insert into Regiao values(02,'A Sul',15000);
	insert into Regiao values(03,'A Oeste',7500);
	insert into Regiao values(04,'A Leste',10000);
	insert into Regiao values(05,'B Norte',100000);
    
    insert into Hospital values(01,'Hospital Santa Luzia','Privado','Avenida Centro-Sul Lote 14',150000,'01');
    insert into Hospital values(02,'Hospital Regional 01','Público','SHIS 68 Quadra 15 Bloco 2',100000,'01');
    insert into Hospital values(03,'Hospital Oswaldo Cruz','Privado','Rua Gilberto Freyre Bloco A',80000,'02');
    insert into Hospital values(04,'Hospital Municipal Francisco Chagas','Público','Rua dos Hortelães Lote 2',200000,'03');
    insert into Hospital values(05,'Hospital do Centro','Privado','Setor Central Rua 18 Lote 1',120000,'05');
    
    insert into Funcionarios values(088576324,'Jussara Cardoso','Enfermeira','1987-08-04',10000,'Rua do Ouvidor Casa 12','jussara@hotmail.com',01);
    insert into Funcionarios values(894764555,'Emília Novaes','Médica da Família','1962-12-31',1000,'Rua de Matacavalos Casa 18, RJ','emilia@hotmail.com',01);
    insert into Funcionarios values(100000565,'Justiniano Lima','Porteiro','1952-05-05',100000,'Rua do Empreiteiro Gutierrez Quadra A Casa 15','justiniano@gmail.com',01);
    insert into Funcionarios values(100000410,'Alarico Mendes','Clínico Geral','1991-01-03',800,'Jardim Alemanha Rua dos Visigodos Casa 410','alarico@hotmail.com',05);
    insert into Funcionarios values(100001791,'Maria Antonieta Silva','Enfermeira','1971-12-10',1400,'Setor Habsburgo Rua dos Brioches Casa 2','antonieta@gmail.com',05);
    
	insert into Pacientes values(098765123,'Antonia Magalhães','Casa das Couves 41','amagalhaes@hotmail.com', '1971-08-04');
    insert into Pacientes values(001002003,'Virgulino Ferreira','Avenida Central Lote 1','vferreira@hotmail.com', '1972-08-04');
    insert into Pacientes values(023555666,'Kátia Maria de Sá','Rua Verde Casa 15','kmsa@gmail.com', '1948-11-13');
    insert into Pacientes values(098745623,'Marília Neves','Casa dos Alforjes 45','mneves@hotmail.com', '1992-06-05');
    insert into Pacientes values(055678875,'João Campos','Rua Miguel Arraes Casa 40','jcampos@outlook.com', '1992-06-06');
    
    insert into Hospital_Pacientes values(01,098765123);
    insert into Hospital_Pacientes values(01,055678875);
    insert into Hospital_Pacientes values(01,098745623);
    insert into Hospital_Pacientes values(01,023555666);
    insert into Hospital_Pacientes values(05,001002003);
    
    insert into Telefone_Funcionario values(33428766,088576324);
    insert into Telefone_Funcionario values(33557895,894764555);
    insert into Telefone_Funcionario values(33556788,100000565);
    insert into Telefone_Funcionario values(33020233,100000410);
    insert into Telefone_Funcionario values(32451789,100001791);
    
    insert into Recurso values(01,'Equipamentos Hospitalares','Doação Privada',01);
    insert into Recurso values(02,'Testes','Federal',01);
    insert into Recurso values(03,'Testes','Federal',02);
    insert into Recurso values(04,'Máscaras','Doação Privada',02);
    insert into Recurso values(05,'Testes','Federal',03);
    
    insert into Equipamentos values(01,'Maca','A',5);
    insert into Equipamentos values(02,'Maca','B',7);
    insert into Equipamentos values(03,'Ventilador Mecânico','A',5);
    insert into Equipamentos values(04,'Ventilador Mecânico','A',10);
    insert into Equipamentos values(05,'Antitérmico','B',50);
    
    insert into Hospital_Equipamentos values(01,01);
    insert into Hospital_Equipamentos values(01,02);
    insert into Hospital_Equipamentos values(01,03);
    insert into Hospital_Equipamentos values(02,04);
    insert into Hospital_Equipamentos values(03,05);
    
    insert into Medicamentos values(01,50);
    insert into Medicamentos values(02,20);
    insert into Medicamentos values(03,10);
    insert into Medicamentos values(04,30);
    insert into Medicamentos values(05,40);
    
    insert into Telefone_Pacientes values(34890000,098765123);
    insert into Telefone_Pacientes values(99992599,001002003);
    insert into Telefone_Pacientes values(34891657,023555666);
    insert into Telefone_Pacientes values(35228900,098745623);
    insert into Telefone_Pacientes values(98715467,055678875);
    
    insert into Pacientes_Medicamentos values (098765123,01);
    insert into Pacientes_Medicamentos values (098765123,02);
    insert into Pacientes_Medicamentos values (098765123,03);
    insert into Pacientes_Medicamentos values (023555666,01);
    insert into Pacientes_Medicamentos values (055678875,01);
    
    insert into Boletim_de_COVID values(01,500,0,250,4000,'2020-05-04','Baixa',0.7,01);
    insert into Boletim_de_COVID values(02,600,1,250,4500,'2020-05-05','Baixa',0.77,01);
    insert into Boletim_de_COVID values(03,750,5,250,5200,'2020-05-06','Baixa',0.79,02);
    insert into Boletim_de_COVID values(04,810,6,300,4000,'2020-05-07','Baixa',0.8,02);
    insert into Boletim_de_COVID values(05,830,0,320,4000,'2020-05-08','Baixa',0.8,03);
    
    insert into Testes values(01,'Sorologico','Positivo','Laboratorio Gomes',098765123);
    insert into Testes values(02,'Sorologico','Negativo','Laboratorio Chebab',055678875);
    insert into Testes values(03,'Sorologico','Positivo','Laboratorio Gomes',023555666);
    insert into Testes values(04,'Sorologico','Positivo','Laboratorio Chebab',098745623);
    insert into Testes values(05,'RT-PCR','Positivo','Laboratorio Chebab',055678875);
    
	insert into Enfermidades values('Diabetes','Moderada','Não-infecciosa');
    insert into Enfermidades values('Sarampo','Moderada','Infecciosa');
    insert into Enfermidades values('Bronquite','Moderada','Não-infecciosa');
    insert into Enfermidades values('Pressão Alta','Moderada','Não-infecciosa');
    insert into Enfermidades values('Catapora','Baixa','Infecciosa');
    
    insert into Pacientes_Enfermidades values(098765123,'Diabetes');
    insert into Pacientes_Enfermidades values(055678875,'Bronquite');
    insert into Pacientes_Enfermidades values(055678875,'Sarampo');
    insert into Pacientes_Enfermidades values(023555666,'Diabetes');
    insert into Pacientes_Enfermidades values(098745623,'Diabetes');
    
    
    SELECT * FROM Hospital;