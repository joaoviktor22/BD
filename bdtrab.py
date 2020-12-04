import mysql.connector

conn = mysql.connector.connect(
   host="localhost",
  user="root",
  password="",
   database="BD"
)
def Criar():
  mycursor = conn.cursor()
  mycursor.execute("DROP TABLE IF EXISTS Hospital")
  mycursor.execute("DROP TABLE IF EXISTS Funcionarios")
  mycursor.execute("DROP TABLE IF EXISTS Telefones_Funcionarios")
  mycursor.execute("DROP TABLE IF EXISTS Telefone_Funcionario")
  mycursor.execute("DROP TABLE IF EXISTS Telefone_Funcionarios")
  mycursor.execute("DROP TABLE IF EXISTS Telefone_Pacientes")
  mycursor.execute("DROP TABLE IF EXISTS Hospital_Pacientes")
  mycursor.execute("DROP TABLE IF EXISTS Recurso")
  mycursor.execute("DROP TABLE IF EXISTS Hospital_Equipamentos")
  mycursor.execute("DROP TABLE IF EXISTS Equipamentos")
  mycursor.execute("DROP TABLE IF EXISTS Regiao")
  mycursor.execute("DROP TABLE IF EXISTS Boletim_de_COVID")
  mycursor.execute("DROP TABLE IF EXISTS Pacientes")
  mycursor.execute("DROP TABLE IF EXISTS Telefones_Pacientes")
  mycursor.execute("DROP TABLE IF EXISTS Testes")
  mycursor.execute("DROP TABLE IF EXISTS Pacientes_Medicamentos")
  mycursor.execute("DROP TABLE IF EXISTS Medicamentos")
  mycursor.execute("DROP TABLE IF EXISTS Pacientes_Enfermidades")
  mycursor.execute("DROP TABLE IF EXISTS Enfermidades")
  mycursor.execute("CREATE TABLE  Regiao(Codigo		INTEGER UNSIGNED PRIMARY KEY,Nome 		varchar(65) NOT NULL,Numero_de_Habitantes	INTEGER UNSIGNED NOT NULL)")
  mycursor.execute("CREATE TABLE  Hospital(Codigo		INTEGER UNSIGNED PRIMARY KEY,Nome 		varchar(65) NOT NULL,Natureza	varchar(150) NOT NULL,Endereço		varchar(150) NOT NULL,Orçamento 		float NOT NULL,Regiao_Codigo INTEGER UNSIGNED references Regiao(Codigo))")
  mycursor.execute("CREATE TABLE  Boletim_de_COVID(Codigo		INTEGER UNSIGNED PRIMARY KEY,Numero_de_Infectados	INTEGER UNSIGNED NOT NULL,Numero_de_Obitos	INTEGER UNSIGNED NOT NULL,Numero_de_Recuperados	INTEGER UNSIGNED NOT NULL,Numero_de_Testes	INTEGER UNSIGNED NOT NULL,Data_de_Publicacao		DATE NOT NULL,Status_de_Gravidade		varchar(65) NOT NULL,Taxa_de_Transmissao_COVID 		FLOAT NOT NULL);")
  mycursor.execute("CREATE TABLE  Funcionarios(CPF		INTEGER UNSIGNED PRIMARY KEY,Nome 		varchar(65) NOT NULL,Profissao 		varchar(65) NOT NULL,Data_de_Nascimento 	DATE NOT NULL,Salario	FLOAT NOT NULL,Endereço		varchar(150) NOT NULL,Email 		varchar(65) NOT NULL,Hospital_Codigo INTEGER UNSIGNED references Hospital(Codigo))")
  mycursor.execute("CREATE TABLE  Telefones_Funcionarios(Telefone		INTEGER UNSIGNED PRIMARY KEY,Funcionarios_CPF INTEGER UNSIGNED references Funcionarios(CPF))")
  mycursor.execute("CREATE TABLE  Recurso(Codigo		INTEGER UNSIGNED PRIMARY KEY,Finalidade 		varchar(65) NOT NULL,Origem 		varchar(65) NOT NULL,Hospital_Codigo INTEGER UNSIGNED references Hospital(Codigo))")
  mycursor.execute("CREATE TABLE  Equipamentos(Codigo		INTEGER UNSIGNED PRIMARY KEY,Nome 		varchar(65) NOT NULL,Ala 		varchar(65) NOT NULL,Quantidade INTEGER UNSIGNED NOT NULL)")
  mycursor.execute("CREATE TABLE  Hospital_Equipamentos(Hospital_Codigo INTEGER UNSIGNED references Hospital(Codigo),Equipamentos_Codigo INTEGER UNSIGNED references Equipamentos(Codigo))")
  mycursor.execute("CREATE TABLE  Pacientes(CPF		INTEGER UNSIGNED PRIMARY KEY,Nome 		varchar(65) NOT NULL,Endereço 		varchar(65) NOT NULL,Email 		varchar(65) NOT NULL,Data_de_Nascimento DATE NOT NULL)")
  mycursor.execute("CREATE TABLE  Hospital_Pacientes(Hospital_Codigo INTEGER UNSIGNED references Hospital(Codigo),Pacientes_CPF INTEGER UNSIGNED references Pacientes(CPF))")
  mycursor.execute("CREATE TABLE  Testes(Codigo		INTEGER UNSIGNED PRIMARY KEY,Tipo_de_Teste 		varchar(65) NOT NULL,Resultado 		varchar(65) NOT NULL,Origem 		varchar(65) NOT NULL,Pacientes_CPF INTEGER UNSIGNED references Pacientes(CPF))")
  mycursor.execute("CREATE TABLE  Enfermidades(Nome		varchar(65) PRIMARY KEY,Gravidade 		varchar(65) NOT NULL,Natureza 		varchar(65) NOT NULL)")
  mycursor.execute("CREATE TABLE  Pacientes_Enfermidades(Pacientes_CPF INTEGER UNSIGNED references Pacientes(CPF),Enfermidade_Nome varchar(65) references Enfermidades(Nome))")
  mycursor.execute("CREATE TABLE  Telefones_Pacientes(Telefone		INTEGER UNSIGNED PRIMARY KEY,Pacientes_CPF INTEGER UNSIGNED references Pacientes(CPF))")
  mycursor.execute("CREATE TABLE  Medicamentos(Codigo INTEGER UNSIGNED PRIMARY KEY,Preço FLOAT NOT NULL)")
  mycursor.execute("CREATE TABLE  Pacientes_Medicamentos(Pacientes_CPF INTEGER UNSIGNED references Pacientes(CPF),Medicamentos_Codigo INTEGER UNSIGNED references Medicamentos(Codigo))")
  mycursor.execute("insert into Regiao values(01,'A Norte',5000);")
  mycursor.execute("insert into Regiao values(02,'A Sul',15000);")
  mycursor.execute("insert into Regiao values(03,'A Oeste',7500);")
  mycursor.execute("insert into Regiao values(04,'A Leste',10000);")
  mycursor.execute("insert into Regiao values(05,'B Norte',100000);")
  mycursor.execute("insert into Hospital values(01,'Hospital Santa Luzia','Privado','Avenida Centro-Sul Lote 14',150000,'01');")
  mycursor.execute("insert into Hospital values(02,'Hospital Regional 01','Público','SHIS 68 Quadra 15 Bloco 2',100000,'01');")
  mycursor.execute("insert into Hospital values(03,'Hospital Oswaldo Cruz','Privado','Rua Gilberto Freyre Bloco A',80000,'02');")
  mycursor.execute("insert into Hospital values(04,'Hospital Municipal Francisco Chagas','Público','Rua dos Hortelães Lote 2',200000,'03');")
  mycursor.execute("insert into Hospital values(05,'Hospital do Centro','Privado','Setor Central Rua 18 Lote 1',120000,'05');")
  mycursor.execute("insert into Funcionarios values(088576324,'Jussara Cardoso','Enfermeira','1987-08-04',10000,'Rua do Ouvidor Casa 12','jussara@hotmail.com',01);")
  mycursor.execute("insert into Funcionarios values(894764555,'Emília Novaes','Médica da Família','1962-12-31',1000,'Rua de Matacavalos Casa 18, RJ','emilia@hotmail.com',01);")
  mycursor.execute("insert into Funcionarios values(100000565,'Justiniano Lima','Porteiro','1952-05-05',100000,'Rua do Empreiteiro Gutierrez Quadra A Casa 15','justiniano@gmail.com',01);")
  mycursor.execute("insert into Funcionarios values(100000410,'Alarico Mendes','Clínico Geral','1991-01-03',800,'Jardim Alemanha Rua dos Visigodos Casa 410','alarico@hotmail.com',05);")
  mycursor.execute("insert into Funcionarios values(100001791,'Maria Antonieta Silva','Enfermeira','1971-12-10',1400,'Setor Habsburgo Rua dos Brioches Casa 2','antonieta@gmail.com',05);")
  mycursor.execute("insert into Pacientes values(098765123,'Antonia Magalhães','Casa das Couves 41','amagalhaes@hotmail.com', '1971-08-04');")
  mycursor.execute("insert into Pacientes values(001002003,'Virgulino Ferreira','Avenida Central Lote 1','vferreira@hotmail.com', '1972-08-04');")
  mycursor.execute("insert into Pacientes values(023555666,'Kátia Maria de Sá','Rua Verde Casa 15','kmsa@gmail.com', '1948-11-13');")
  mycursor.execute("insert into Pacientes values(098745623,'Marília Neves','Casa dos Alforjes 45','mneves@hotmail.com', '1992-06-05');")
  mycursor.execute("insert into Pacientes values(055678875,'João Campos','Rua Miguel Arraes Casa 40','jcampos@outlook.com', '1992-06-06');")
  mycursor.execute("insert into Hospital_Pacientes values(01,098765123);")
  mycursor.execute("insert into Hospital_Pacientes values(01,055678875);")
  mycursor.execute("insert into Hospital_Pacientes values(01,098745623);")
  mycursor.execute("insert into Hospital_Pacientes values(01,023555666);")
  mycursor.execute("insert into Hospital_Pacientes values(05,001002003);")
  mycursor.execute("insert into Telefones_Funcionarios values(33428766,088576324);")
  mycursor.execute("insert into Telefones_Funcionarios values(33557895,894764555);")
  mycursor.execute("insert into Telefones_Funcionarios values(33556788,000000565);")
  mycursor.execute("insert into Telefones_Funcionarios values(33020233,000000410);")
  mycursor.execute("insert into Telefones_Funcionarios values(32451789,000001791);")
  mycursor.execute("insert into Recurso values(01,'Equipamentos Hospitalares','Doação Privada',01);")
  mycursor.execute("insert into Recurso values(02,'Testes','Federal',01);")
  mycursor.execute("insert into Recurso values(03,'Testes','Federal',02);")
  mycursor.execute("insert into Recurso values(04,'Máscaras','Doação Privada',02);")
  mycursor.execute("insert into Recurso values(05,'Testes','Federal',03);")
  mycursor.execute("insert into Equipamentos values(01,'Maca','A',5);")
  mycursor.execute("insert into Equipamentos values(02,'Maca','B',7);")
  mycursor.execute("insert into Equipamentos values(03,'Ventilador Mecânico','A',5);")
  mycursor.execute("insert into Equipamentos values(04,'Ventilador Mecânico','A',10);")
  mycursor.execute("insert into Equipamentos values(05,'Antitérmico','B',50);")
  mycursor.execute("insert into Hospital_Equipamentos values(01,01);")
  mycursor.execute("insert into Hospital_Equipamentos values(01,02);")
  mycursor.execute("insert into Hospital_Equipamentos values(01,03);")
  mycursor.execute("insert into Hospital_Equipamentos values(02,04);")
  mycursor.execute("insert into Hospital_Equipamentos values(03,05);")
  mycursor.execute("insert into Medicamentos values(01,50);")
  mycursor.execute("insert into Medicamentos values(02,20);")
  mycursor.execute("insert into Medicamentos values(03,10);")
  mycursor.execute("insert into Medicamentos values(04,30);")
  mycursor.execute("insert into Medicamentos values(05,40);")
  mycursor.execute("insert into Telefones_Pacientes values(34890000,098765123);")
  mycursor.execute("insert into Telefones_Pacientes values(99992599,001002003);")
  mycursor.execute("insert into Telefones_Pacientes values(34891657,023555666);")
  mycursor.execute("insert into Telefones_Pacientes values(35228900,098745623);")
  mycursor.execute("insert into Telefones_Pacientes values(98715467,055678875);")
  mycursor.execute("insert into Pacientes_Medicamentos values (098765123,01);")
  mycursor.execute("insert into Pacientes_Medicamentos values (098765123,02);")
  mycursor.execute("insert into Pacientes_Medicamentos values (098765123,03);")
  mycursor.execute("insert into Pacientes_Medicamentos values (023555666,01);")
  mycursor.execute("insert into Pacientes_Medicamentos values (055678875,01);")
  mycursor.execute("insert into Boletim_de_COVID values(01,500,0,250,4000,'2020-05-04','Baixa',0.7);")
  mycursor.execute("insert into Boletim_de_COVID values(02,600,1,250,4500,'2020-05-05','Baixa',0.77);")
  mycursor.execute("insert into Boletim_de_COVID values(03,750,5,250,5200,'2020-05-06','Baixa',0.79);")
  mycursor.execute("insert into Boletim_de_COVID values(04,810,6,300,4000,'2020-05-07','Baixa',0.8);")
  mycursor.execute("insert into Boletim_de_COVID values(05,830,0,320,4000,'2020-05-08','Baixa',0.8);")
  mycursor.execute("insert into Testes values(01,'Sorologico','Positivo','Laboratorio Gomes',098765123);")
  mycursor.execute("insert into Testes values(02,'Sorologico','Negativo','Laboratorio Chebab',055678875);")
  mycursor.execute("insert into Testes values(03,'Sorologico','Positivo','Laboratorio Gomes',023555666);")
  mycursor.execute("insert into Testes values(04,'Sorologico','Positivo','Laboratorio Chebab',098745623);")
  mycursor.execute("insert into Testes values(05,'RT-PCR','Positivo','Laboratorio Chebab',055678875);")
  mycursor.execute("insert into Pacientes_Enfermidades values(098765123,'Diabetes');")
  mycursor.execute("insert into Pacientes_Enfermidades values(055678875,'Bronquite');")
  mycursor.execute("insert into Pacientes_Enfermidades values(055678875,'Sarampo');")
  mycursor.execute("insert into Pacientes_Enfermidades values(023555666,'Diabetes');")
  mycursor.execute("insert into Pacientes_Enfermidades values(098745623,'Diabetes');")
  mycursor.execute("insert into Enfermidades values('Diabetes','Moderada','Não-infecciosa');")
  mycursor.execute("insert into Enfermidades values('Sarampo','Moderada','Infecciosa');")
  mycursor.execute("insert into Enfermidades values('Bronquite','Moderada','Não-infecciosa');")
  mycursor.execute("insert into Enfermidades values('Pressão Alta','Moderada','Não-infecciosa');")
  mycursor.execute("insert into Enfermidades values('Catapora','Baixa','Infecciosa');")
  conn.commit()
  mycursor.close()

#Criar()  #resetar banco de dados e inserir os 5 registros de cada entidade
def menu():
  #Criar()
  entrada = 0
  while(entrada != '5'):
    print("Secretaria de COVID")
    print("1)Inserir")
    print("2)Deletar")
    print("3)Modificar")
    print("4)Ver Dados")
    print("5)Sair")
    entrada = input("Qual operação você deseja fazer?")
    if(entrada == '1'):
      c = conn.cursor()
      sql = "SHOW TABLES"
      c.execute(sql)
      i = 1
      for x in c:
        print(i,":",x[0])
        i=i+1
      c.close()
      escolha = input("Quer inserir em qual tabela? Escreva Nome ou Numero")
      if(escolha == "13" or escolha == "Regiao"):
        c = conn.cursor(buffered=True)
        nome_regiao = input("Qual nome da regiao?")
        habitantes = int(input("Qual o numero de habitantes"))
        sql = "SELECT Codigo FROM Regiao"
        c.execute(sql)
        sql = """insert into Regiao (Nome,Numero_de_Habitantes) values(%s,%s);"""
        try:
          c.execute(sql, (nome_regiao,habitantes,))
        except Exception as e:
          print(e)
          print("Nome ou Numero de Habitantes errados")
        conn.commit()
        c.close()
      if(escolha == "5" or escolha == "Hospital"):
        c = conn.cursor(buffered=True)
        try:
          nome_hospital = input("Qual nome do hospital?")
          natureza = input("Qual a natureza do hospital")
          endereco = input("Qual o endereco?")
          orcamento = float(input("Qual o orcamento"))
          sql = "SELECT Nome FROM Regiao"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          regiao = input("Qual o nome da regiao?")
          sql = "SELECT Nome FROM Regiao WHERE Nome = (%s)"
          c.execute(sql, (regiao,))
          row = c.fetchone()
          if(row != None and row[0] == regiao):
            sql = "SELECT Codigo FROM Regiao WHERE Nome = (%s)"
            c.execute(sql, (regiao,))
            codigo_regiao = c.fetchone()
            sql = "insert into Hospital (Nome,Natureza,Endereço,Orçamento,Regiao_Codigo) values(%s,%s,%s,%s,%s);"
            c.execute(sql, (nome_hospital,natureza,endereco,orcamento,codigo_regiao[0],))
          else:
            print("Regiao inexistente")
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Algo nao esta correto.")

      if(escolha == "1" or escolha == "Boletim_de_COVID"):
        c = conn.cursor(buffered=True)
        try:
          infectados = int(input("Qual numero de infectados?"))
          obitos = int(input("Qual numero de obitos?"))
          recuperados = int(input("Qual numero de recuperados?"))
          testes = int(input("Qual numero de testes?"))
          date = input("Qual dia da publicacao?formato (YYYY-MM-DD)")
          gravidade = input("Qual status de gravidade?")
          taxa = float(input("Qual a taxa de transmissao?"))
          sql = "SELECT Nome FROM Regiao"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          regiao = input("Qual o nome da regiao?")
          sql = "SELECT Nome FROM Regiao WHERE Nome = (%s)"
          c.execute(sql, (regiao,))
          row = c.fetchone()
          if (row != None and row[0] == regiao):
            sql = "SELECT Codigo FROM Regiao WHERE Nome = (%s)"
            c.execute(sql, (regiao,))
            codigo_regiao = c.fetchone()
            sql = "insert into Boletim_de_COVID (Numero_de_Infectados, Numero_de_Obitos, Numero_de_Recuperados, Numero_de_Testes, Data_de_Publicacao, Status_de_Gravidade, Taxa_de_Transmissao_COVID) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            c.execute(sql, (infectados, obitos, recuperados, testes, date, gravidade, taxa, codigo_regiao,))
          else:
            print("Regiao Inexistente")
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Algo nao esta correto.")
      if (escolha == "4" or escolha == "Funcionarios"):
        c = conn.cursor(buffered=True)
        try:
          cpf = int(input("Qual CPF?"))
          nome = input("Qual o nome do funcionario?")
          profissao = input("Qual a  profissao?")
          nascimento = input("Data de Nascimento?formato (YYYY-MM-DD)")
          salario = float(input("Qual o Salario?"))
          endereco = input("Qual o endereco?")
          email = input("Qual o email?")
          sql = "SELECT Nome FROM Hospital"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          hospital = input("Qual nome do Hospital?")
          sql = "SELECT Nome FROM Hospital WHERE Nome = (%s)"
          c.execute(sql, (hospital,))
          row = c.fetchone()
          if (row != None and row[0] == hospital):
            sql = "SELECT Codigo FROM Hospital WHERE Nome = (%s)"
            c.execute(sql, (hospital,))
            codigo_hospital = c.fetchone()
            sql = "insert into Funcionarios (CPF,Nome,Profissao,Data_de_Nascimento,Salario,Endereço,Email,Hospital_Codigo) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            c.execute(sql, (cpf ,nome, profissao, nascimento, salario, endereco, email, codigo_hospital[0],))
          else:
            print("Hospital Inexistente")
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Algo nao esta correto.")
      if(escolha == "14" or escolha=="Telefone_Funcionario"):
        c = conn.cursor(buffered=True)
        sql = "SELECT Nome FROM Funcionarios"
        c.execute(sql)
        i = 1
        for x in c:
          print(i, ":", x[0])
          i = i + 1
        escolha_nome = input("Quer adicionar telefone em qual destes funcionarios?")
        try:
          sql = "SELECT CPF FROM Funcionarios WHERE Nome = (%s)"
          c.execute(sql,(escolha_nome,))
          cpf_escolhido = c.fetchone()
          escolha_telefone = int(input("Qual telefone?"))
          sql = "insert into Telefone_Funcionario (Telefone,Funcionarios_CPF) values(%s,%s);"
          c.execute(sql,(escolha_telefone,cpf_escolhido[0],))
        except Exception as e:
          print(e)
          print("Nome ou Telefone escritos errados")
        conn.commit()
        c.close()
      if (escolha == "12" or escolha == "Recurso"):
        c = conn.cursor(buffered=True)
        try:
          finalidade = input("Qual a finalidade?")
          origem = input("Qual a origem?")
          sql = "SELECT Nome FROM Hospital"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          hospital = input("Qual nome do Hospital?")
          sql = "SELECT Nome FROM Hospital WHERE Nome = (%s)"
          c.execute(sql, (hospital,))
          row = c.fetchone()
          if (row != None and row[0] == hospital):
            sql = "SELECT Codigo FROM Hospital WHERE Nome = (%s)"
            c.execute(sql, (hospital,))
            codigo_hospital = c.fetchone()
            sql = "insert into Recurso (Finalidade,Origem,Hospital_Codigo) values(%s,%s,%s);"
            c.execute(sql, (finalidade, origem, codigo_hospital[0],))
          else:
            print("Hospital Inexistente")
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "3" or escolha == "Equipamentos"):
        c = conn.cursor(buffered=True)
        try:
          nome = input("Qual o nome?")
          ala = input("Qual a ala?")
          quantidade = int(input("Qual a quantidade?"))
          sql = "insert into Equipamentos (Nome,Ala,Quantidade) values(%s,%s,%s);"
          c.execute(sql, (nome, ala, quantidade,))
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "6" or escolha == "Hospital_Equipamentos"):
        c = conn.cursor(buffered=True)
        try:
          sql = "SELECT Nome FROM Hospital"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          hospital = input("Qual nome do Hospital?")
          sql = "SELECT Nome FROM Hospital WHERE Nome = (%s)"
          c.execute(sql, (hospital,))
          row = c.fetchone()
          if (row != None and row[0] == hospital):
            sql = "SELECT Codigo FROM Hospital WHERE Nome = (%s)"
            c.execute(sql, (hospital,))
            codigo_hospital = c.fetchone()
            sql = "SELECT Nome FROM Equipamentos"
            c.execute(sql)
            i = 1
            for x in c:
              print(i, ":", x[0])
              i = i + 1
            equipamento = input("Qual nome do Equipamento?")
            sql = "SELECT Nome FROM Equipamentos WHERE Nome = (%s)"
            c.execute(sql, (equipamento,))
            row = c.fetchone()
            if (row != None and row[0] == equipamento):
              sql = "SELECT Codigo FROM Equipamentos WHERE Nome = (%s)"
              c.execute(sql, (equipamento,))
              codigo_equipamento = c.fetchone()
              sql = "insert into Hospital_Equipamentos (Hospital_Codigo,Equipamentos_Codigo) values(%s,%s);"
              c.execute(sql, (codigo_hospital[0], codigo_equipamento[0],))
            else:
              print("Equipamento Inexistente")
          else:
            print("Hospital Inexistente")
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "9" or escolha == "Pacientes"):
        c = conn.cursor(buffered=True)
        try:
          cpf = int(input("Qual o CPF do paciente?"))
          nome = input("Qual o nome do paciente?")
          endereco = input("Qual o endereco?")
          email = input("Qual o email?")
          nascimento = input("Data de Nascimento?formato (YYYY-MM-DD)")
          sql = "insert into Pacientes (CPF,Nome,Endereço,Email,Data_de_Nascimento) values(%s,%s,%s,%s,%s);"
          c.execute(sql, (cpf, nome, endereco, email, nascimento,))
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Algo nao esta correto.")
      if (escolha == "7" or escolha == "Hospital_Pacientes"):
        c = conn.cursor(buffered=True)
        try:
          sql = "SELECT Nome FROM Hospital"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          hospital = input("Qual nome do Hospital?")
          sql = "SELECT Nome FROM Hospital WHERE Nome = (%s)"
          c.execute(sql, (hospital,))
          row = c.fetchone()
          if (row != None and row[0] == hospital):
            sql = "SELECT Codigo FROM Hospital WHERE Nome = (%s)"
            c.execute(sql, (hospital,))
            codigo_hospital = c.fetchone()
            sql = "SELECT Nome FROM Pacientes"
            c.execute(sql)
            i = 1
            for x in c:
              print(i, ":", x[0])
              i = i + 1
            paciente = input("Qual nome do Paciente?")
            sql = "SELECT Nome FROM Pacientes WHERE Nome = (%s)"
            c.execute(sql, (paciente,))
            row = c.fetchone()
            if (row != None and row[0] == paciente):
              sql = "SELECT CPF FROM Pacientes WHERE Nome = (%s)"
              c.execute(sql, (paciente,))
              cpf_paciente = c.fetchone()
              sql = "insert into Hospital_Pacientes (Hospital_Codigo,Pacientes_CPF) values(%s,%s);"
              c.execute(sql, (codigo_hospital[0], cpf_paciente[0],))
            else:
              print("Paciente Inexistente")
          else:
            print("Hospital Inexistente")
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "16" or escolha == "Testes"):
        c = conn.cursor(buffered=True)
        try:
          tipo = input("Qual o tipo do teste?")
          result = input("Qual o resultado?")
          origem = input("Qual a Origem?")
          sql = "SELECT Nome FROM Pacientes"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          paciente = input("Qual nome do Paciente?")
          sql = "SELECT Nome FROM Pacientes WHERE Nome = (%s)"
          c.execute(sql, (paciente,))
          row = c.fetchone()
          if (row != None and row[0] == paciente):
            sql = "SELECT CPF FROM Pacientes WHERE Nome = (%s)"
            c.execute(sql, (paciente,))
            cpf_paciente = c.fetchone()
            sql = "insert into Testes (Tipo_de_Teste,Resultado,Origem,Pacientes_CPF) values(%s,%s,%s,%s);"
            c.execute(sql, (tipo, result, origem, cpf_paciente[0],))
          else:
            print("Paciente Inexistente")
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Algo nao esta correto.")
      if (escolha == "2" or escolha == "Enfermidades"):
        c = conn.cursor(buffered=True)
        try:
          nome = input("Qual o nome da enfermidade?")
          gravidade = input("Qual a gravidade?")
          natureza = input("Qual a natureza da enfermidade?")
          sql = "insert into Enfermidades (Nome,Gravidade,Natureza) values(%s,%s,%s);"
          c.execute(sql, (nome, gravidade, natureza,))
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "10" or escolha == "Pacientes_Enfermidades"):
        c = conn.cursor(buffered=True)
        try:
          sql = "SELECT Nome FROM Pacientes"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          paciente = input("Qual nome do paciente?")
          sql = "SELECT Nome FROM Pacientes WHERE Nome = (%s)"
          c.execute(sql, (paciente,))
          row = c.fetchone()
          if (row != None and row[0] == paciente):
            sql = "SELECT CPF FROM Pacientes WHERE Nome = (%s)"
            c.execute(sql, (paciente,))
            cpf_paciente = c.fetchone()
            sql = "SELECT Nome FROM Enfermidades"
            c.execute(sql)
            i = 1
            for x in c:
              print(i, ":", x[0])
              i = i + 1
            enfermidade = input("Qual nome da enfermidade?")
            sql = "SELECT Nome FROM Enfermidades WHERE Nome = (%s)"
            c.execute(sql, (enfermidade,))
            row = c.fetchone()
            if (row != None and row[0] == enfermidade):
              sql = "insert into Pacientes_Enfermidades (Pacientes_CPF,Enfermidade_Nome) values(%s,%s);"
              c.execute(sql, (cpf_paciente[0], enfermidade,))
            else:
              print("Enfermidade Inexistente")
          else:
            print("Paciente Inexistente")
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "15" or escolha == "Telefone_Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT Nome FROM Pacientes"
        c.execute(sql)
        i = 1
        for x in c:
          print(i, ":", x[0])
          i = i + 1
        c.close()
        escolha_nome = input("Quer adicionar telefone em qual destes funcionarios?")
        try:
          c = conn.cursor()
          sql = "SELECT CPF FROM Pacientes WHERE Nome = (%s)"
          c.execute(sql, (escolha_nome,))
          cpf_escolhido = c.fetchone()
          escolha_telefone = int(input("Qual telefone?"))
          sql = "insert into Telefone_Pacientes (Telefone,Pacientes_CPF) values(%s,%s);"
          c.execute(sql, (escolha_telefone,cpf_escolhido[0],))
          conn.commit()
          c.close()
        except Exception as e:
          print(e)
          print("Nome ou Telefone escritos errados")
      if (escolha == "8" or escolha == "Medicamentos"):
        c = conn.cursor(buffered=True)
        try:
          preco = input("Qual o Preco?")
          sql = "insert into Medicamentos (Preço) values(%s);"
          c.execute(sql, (preco,))
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
      if (escolha == "11" or escolha == "Pacientes_Medicamentos"):
        c = conn.cursor(buffered=True)
        try:
          sql = "SELECT Nome FROM Pacientes"
          c.execute(sql)
          i = 1
          for x in c:
            print(i, ":", x[0])
            i = i + 1
          paciente = input("Qual nome do paciente?")
          sql = "SELECT Nome FROM Pacientes WHERE Nome = (%s)"
          c.execute(sql, (paciente,))
          row = c.fetchone()
          if (row != None and row[0] == paciente):
            sql = "SELECT CPF FROM Pacientes WHERE Nome = (%s)"
            c.execute(sql, (paciente,))
            cpf_paciente = c.fetchone()
            sql = "SELECT * FROM Medicamentos"
            c.execute(sql)
            for x in c:
              print(x[0])
            medicamento = int(input("Qual codigo do medicamento?"))
            sql = "SELECT Codigo FROM Medicamentos WHERE Codigo = (%s)"
            c.execute(sql, (medicamento,))
            row = c.fetchone()
            if (row != None and row[0] == medicamento):
              sql = "insert into Pacientes_Medicamentos (Pacientes_CPF,Medicamentos_Codigo) values(%s,%s);"
              c.execute(sql, (cpf_paciente[0], medicamento,))
            else:
              print("Medicamento Inexistente")
          else:
            print("Paciente Inexistente")
          conn.commit()
          c.close()
        except:
          print("Algo nao esta correto.")
    if (entrada == '2'):
      c = conn.cursor()
      sql = "SHOW TABLES"
      c.execute(sql)
      i = 1
      for x in c:
        print(i, ":", x[0])
        i = i + 1
      c.close()
      escolha = input("Quer apagar em qual tabela? Escreva Nome ou Numero")
      if (escolha == "13" or escolha == "Regiao"):
        c = conn.cursor(buffered=True)
        c2 = conn.cursor(buffered=True)
        c3 = conn.cursor(buffered=True)
        sql = "SELECT * FROM Regiao WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Regiao"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual Codigo da Regiao para apagar?"))
          sql = "SELECT Codigo FROM Regiao WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            certeza = input("Tem certeza que quer apagar? Se sim digite Sim se nao digite Nao (Se Apagar todos os relacionamentos serao apagados.)")
            if(certeza == "Sim" or certeza == "sim"):
              sql = "DELETE FROM Boletim_de_COVID WHERE Regiao_Codigo = (%s)"
              c.execute(sql, (apagar,))
              sql = "SELECT Codigo FROM Hospital WHERE Regiao_Codigo = (%s)"
              c.execute(sql, (apagar,))
              for hospital in c:
                sql = "SELECT CPF FROM Funcionarios WHERE  Hospital_Codigo = (%s)"
                c2.execute(sql, (hospital[0],))
                for funcionario in c2:
                  sql = "DELETE FROM Telefone_Funcionario WHERE Funcionarios_CPF = (%s)"
                  c3.execute(sql, (funcionario[0],))
                  sql = "DELETE FROM Funcionarios WHERE CPF = (%s)"
                  c3.execute(sql, (funcionario[0],))
                sql = "DELETE FROM Hospital_Equipamentos WHERE Hospital_Codigo = (%s)"
                c2.execute(sql, (hospital[0],))
                sql = "DELETE FROM Hospital_Pacientes WHERE Hospital_Codigo = (%s)"
                c2.execute(sql, (hospital[0],))
                sql = "DELETE FROM Recurso WHERE Hospital_Codigo = (%s)"
                c2.execute(sql, (hospital[0],))
              sql = "DELETE FROM Hospital WHERE Regiao_Codigo = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Regiao WHERE Codigo = (%s)"
              c.execute(sql, (apagar,))
            else:
              print("Operacao Cancelada")
          else:
            print("Regiao Inexistente")
        except Exception as e:
          print("Erro ao Apagar",e)
        conn.commit()
        c.close()
      if (escolha == "5" or escolha == "Hospital"):
        c = conn.cursor(buffered=True)
        c2 = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual Codigo do Hospital para apagar?"))
          sql = "SELECT Codigo FROM Hospital WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            certeza = input("Tem certeza que quer apagar? Se sim digite Sim se nao digite Nao (Se Apagar todos os relacionamentos serao apagados.)")
            if (certeza == "Sim" or certeza == "sim"):
              sql = "DELETE FROM Hospital_Equipamentos WHERE Hospital_Codigo = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Hospital_Pacientes WHERE Hospital_Codigo = (%s)"
              c.execute(sql, (apagar,))
              sql = "SELECT CPF FROM Funcionarios WHERE  Hospital_Codigo = (%s)"
              c.execute(sql, (apagar,))
              for funcionario in c:
                sql = "DELETE FROM Telefone_Funcionario WHERE Funcionarios_CPF = (%s)"
                c2.execute(sql, (funcionario[0],))
                sql = "DELETE FROM Funcionarios WHERE CPF = (%s)"
                c2.execute(sql, (funcionario[0],))
              sql = "DELETE FROM Recurso WHERE Hospital_Codigo = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Hospital WHERE Codigo = (%s)"
              c.execute(sql, (apagar,))
            else:
              print("Operacao Cancelada")
          else:
            print("Hospital Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "1" or escolha == "Boletim_de_COVID"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Boletim_de_COVID WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Boletim_de_COVID"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual codigo do bolteim de COVID para apagar?"))
          sql = "SELECT Codigo FROM Boletim_de_COVID WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Boletim_de_COVID WHERE Codigo = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Boletim Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "4" or escolha == "Funcionarios"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Funcionarios WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Funcionarios"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual CPF do Funcionario para apagar?"))
          sql = "SELECT CPF FROM Funcionarios WHERE CPF = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Telefone_Funcionario WHERE Funcionarios_CPF = (%s)"
            c.execute(sql, (apagar,))
            sql = "DELETE FROM Funcionarios WHERE CPF = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Funcionario Inexistente")
        except Exception as e:
          print("Erro ao Apagar",e)
        conn.commit()
        c.close()
      if (escolha == "14" or escolha == "Telefone_Funcionario"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Funcionario WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Telefone_Funcionario"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual telefone para apagar?"))
          sql = "SELECT Telefone FROM Telefone_Funcionario WHERE Telefone = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Telefone_Funcionario WHERE Telefone = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Telefone Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "12" or escolha == "Recurso"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Recurso WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Recurso"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual codigo do recurso para apagar?"))
          sql = "SELECT Codigo FROM Recurso WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Recurso WHERE Codigo = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Recurso Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "3" or escolha == "Equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Equipamentos"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual codigo do equipamento para apagar?"))
          sql = "SELECT Codigo FROM Equipamentos WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Hospital_Equipamentos WHERE Equipamentos_Codigo = (%s)"
            c.execute(sql, (apagar,))
            sql = "DELETE FROM Equipamentos WHERE Codigo = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Equipamento Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "6" or escolha == "Hospital_Equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital_Equipamentos"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar1 = int(input("Qual codigo do Hospital apagar?"))
          sql = "SELECT Hospital_Codigo FROM Hospital_Equipamentos WHERE Hospital_Codigo = (%s)"
          c.execute(sql, (apagar1,))
          row = c.fetchone()
          if (row != None and row[0] == apagar1):
            apagar2 = int(input("Qual Codigo do Equipamento ara apagar?"))
            sql = "SELECT Equipamentos_Codigo FROM Hospital_Equipamentos WHERE Equipamentos_Codigo = (%s)"
            c.execute(sql, (apagar2,))
            row = c.fetchone()
            if (row != None and row[0] == apagar2):
              sql = "DELETE FROM Hospital_Equipamentos WHERE Hospital_Codigo = (%s) and Equipamentos_Codigo = (%s)"
              c.execute(sql, (apagar1,apagar2,))
            else:
               print("Equipamento_Codigo Inexistente")
          else:
            print("Hospital_Codigo Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "9" or escolha == "Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual CPF do Paciente para apagar?"))
          sql = "SELECT CPF FROM Pacientes WHERE CPF = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            certeza = input("Tem certeza que quer apagar? Se sim digite Sim se nao digite Nao (Se Apagar todos os relacionamentos serao apagados.)")
            if (certeza == "Sim" or certeza == "sim"):
              sql = "DELETE FROM Hospital_Pacientes WHERE Pacientes_CPF = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Testes WHERE Pacientes_CPF = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Pacientes_Enfermidades WHERE Pacientes_CPF = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Pacientes_Medicamentos WHERE Pacientes_CPF = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Telefone_Pacientes WHERE Pacientes_CPF = (%s)"
              c.execute(sql, (apagar,))
              sql = "DELETE FROM Pacientes WHERE CPF = (%s)"
              c.execute(sql, (apagar,))
              print("Apagado!")
            else:
              print("Operacao Cancelada")
          else:
            print("Paciente Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "7" or escolha == "Hospital_Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital_Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar1 = int(input("Qual codigo do Hospital para apagar?"))
          sql = "SELECT Hospital_Codigo FROM Hospital_Pacientes WHERE Hospital_Codigo = (%s)"
          c.execute(sql, (apagar1,))
          row = c.fetchone()
          if (row != None and row[0] == apagar1):
            apagar2 = int(input("Qual CPF do Paciente para apagar?"))
            sql = "SELECT Pacientes_CPF FROM Hospital_Pacientes WHERE Pacientes_CPF = (%s)"
            c.execute(sql, (apagar2,))
            row = c.fetchone()
            if (row != None and row[0] == apagar2):
              sql = "DELETE FROM Hospital_Pacientes WHERE Hospital_Codigo = (%s) and Pacientes_CPF = (%s)"
              c.execute(sql, (apagar1, apagar2,))
            else:
              print("Paciente Inexistente")
          else:
            print("Hospital Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "16" or escolha == "Testes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Testes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Testes"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual Codigo do Teste para apagar?"))
          sql = "SELECT Codigo FROM Testes WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Testes WHERE Codigo = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Teste Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "2" or escolha == "Enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Enfermidades"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = input("Qual Nome da Enfermidade para apagar?")
          sql = "SELECT Nome FROM Enfermidades WHERE Nome = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Pacientes_Enfermidades WHERE Enfermidade_Nome = (%s)"
            c.execute(sql, (apagar,))
            sql = "DELETE FROM Enfermidades WHERE Nome = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Enfermidade Inexistente")
        except Exception as e:
          print(e)
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "10" or escolha == "Pacientes_Enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes_Enfermidades"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar1 = int(input("Qual CPF do paciente para apagar?"))
          sql = "SELECT Pacientes_CPF FROM Pacientes_Enfermidades WHERE Pacientes_CPF = (%s)"
          c.execute(sql, (apagar1,))
          row = c.fetchone()
          if (row != None and row[0] == apagar1):
            apagar2 = input("Qual nome da enfermidade para apagar?")
            sql = "SELECT Enfermidade_Nome FROM Pacientes_Enfermidades WHERE Enfermidade_Nome = (%s)"
            c.execute(sql, (apagar2,))
            row = c.fetchone()
            if (row != None and row[0] == apagar2):
              sql = "DELETE FROM Pacientes_Enfermidades WHERE Pacientes_CPF = (%s) and Enfermidade_Nome = (%s)"
              c.execute(sql, (apagar1, apagar2,))
            else:
              print("Enfermidade Inexistente")
          else:
            print("Pacinte Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "15" or escolha == "Telefone_Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Telefone_Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual Telefone para apagar?"))
          sql = "SELECT Telefone FROM Telefone_Pacientes WHERE Telefone = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Telefone_Pacientes WHERE Telefone = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Telefone Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "8" or escolha == "Medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Medicamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Medicamentos"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar = int(input("Qual codigo do medicamento para apagar?"))
          sql = "SELECT Codigo FROM Medicamentos WHERE Codigo = (%s)"
          c.execute(sql, (apagar,))
          row = c.fetchone()
          if (row != None and row[0] == apagar):
            sql = "DELETE FROM Pacientes_Medicamentos WHERE Medicamentos_Codigo = (%s)"
            c.execute(sql, (apagar,))
            sql = "DELETE FROM Medicamentos WHERE Codigo = (%s)"
            c.execute(sql, (apagar,))
          else:
            print("Medicamento Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
      if (escolha == "11" or escolha == "Pacientes_Medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Medicamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes_Medicamentos"
        c.execute(sql)
        for x in c:
          print(x)
        try:
          apagar1 = int(input("Qual CPF do Paciente para apagar?"))
          sql = "SELECT Pacientes_CPF FROM Pacientes_Medicamentos WHERE Pacientes_CPF = (%s)"
          c.execute(sql, (apagar1,))
          row = c.fetchone()
          if (row != None and row[0] == apagar1):
            apagar2 = int(input("Qual Codigo do medicamento ara apagar?"))
            sql = "SELECT Medicamentos_Codigo FROM Pacientes_Medicamentos WHERE Medicamentos_Codigo = (%s)"
            c.execute(sql, (apagar2,))
            row = c.fetchone()
            if (row != None and row[0] == apagar2):
              sql = "DELETE FROM Pacientes_Medicamentos WHERE Pacientes_CPF = (%s) and Medicamentos_Codigo = (%s)"
              c.execute(sql, (apagar1, apagar2,))
            else:
              print("Medicamento Inexistente")
          else:
            print("Paciente Inexistente")
        except:
          print("Erro ao Apagar")
        conn.commit()
        c.close()
    if (entrada == '3'):
      c = conn.cursor()
      sql = "SHOW TABLES"
      c.execute(sql)
      tipo = 0
      i = 1
      for x in c:
        print(i, ":", x[0])
        i = i + 1
      c.close()
      escolha = input("Quer modificar qual tabela? Escreva Nome ou Numero")
      if (escolha == "1" or escolha == "boletim_de_covid"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Boletim_de_COVID WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if(coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Boletim_de_COVID"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo do Boletim que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if(tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Numero_de_Infectados'):
              sql = "UPDATE Boletim_de_COVID SET Numero_de_Infectados = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Numero_de_Obitos'):
              sql = "UPDATE Boletim_de_COVID SET Numero_de_Obitos = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Numero_de_Recuperados'):
              sql = "UPDATE Boletim_de_COVID SET Numero_de_Recuperados = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Numero_de_Testes'):
              sql = "UPDATE Boletim_de_COVID SET Numero_de_Testes = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Regiao_Codigo'):
              sql = "UPDATE Boletim_de_COVID SET Regiao_Codigo = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif(tipo == 4):
            valornovo = float(valornovo)
            if (coluna == 'Taxa_de_Transmissao_COVID'):
              sql = "UPDATE Boletim_de_COVID SET Taxa_de_Transmissao_COVID = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif(tipo == 253):
            if (coluna == 'Status_de_Gravidade'):
              sql = "UPDATE Boletim_de_COVID SET Status_de_Gravidade = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif(tipo == 10):
            if (coluna == 'Data_de_Publicacao'):
              sql = "UPDATE Boletim_de_COVID SET Data_de_Publicacao = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO",e)
      if (escolha == "2" or escolha == "enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Enfermidades"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Nome da Enfermidade que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 253):
            if (coluna == 'Gravidade'):
              sql = "UPDATE Enfermidades SET Gravidade = (%s) Where Nome = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Natureza'):
              sql = "UPDATE Enfermidades SET Natureza = (%s) Where Nome = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO",e)
      if (escolha == "3" or escolha == "equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Equipamentos"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo do Equipamento que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            if (coluna == 'Quantidade'):
              sql = "UPDATE Equipamentos SET Quantidade = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Nome'):
              sql = "UPDATE Equipamentos SET Nome = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Ala'):
              sql = "UPDATE Equipamentos SET Ala = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
        except Exception as e:
          print("ERRO", e)
      if (escolha == "4" or escolha == "funcionarios"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Funcionarios WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Funcionarios"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual CPF do funcionario que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Hospital_Codigo'):
              sql = "UPDATE Funcionarios SET Hospital_Codigo = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 4):
            valornovo = float(valornovo)
            if (coluna == 'Salario'):
              sql = "UPDATE Funcionarios SET Salario = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Nome'):
              sql = "UPDATE Funcionarios SET Nome = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Profissao'):
              sql = "UPDATE Funcionarios SET Profissao = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Endereco'):
              sql = "UPDATE Funcionarios SET Endereco = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Email'):
              sql = "UPDATE Funcionarios SET Email = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 10):
            if (coluna == 'Data_de_Nascimento'):
              sql = "UPDATE Funcionarios SET Data_de_Nascimento = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "5" or escolha == "hospital"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Hospital"
          c.execute(sql)
          for x in c:
            print(x)
          print(coluna)
          valor = input("Qual Codigo do Hospital que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Regiao_Codigo'):
              sql = "UPDATE Hospital SET Regiao_Codigo = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 4):
            valornovo = float(valornovo)
            if (coluna == 'Orçamento'):
              sql = "UPDATE Hospital SET Orçamento = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Nome'):
              sql = "UPDATE Hospital SET Nome = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Natureza'):
              sql = "UPDATE Hospital SET Natureza = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Endereço'):
              sql = "UPDATE Hospital SET Endereço = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "6" or escolha == "hospital_equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Hospital_Equipamentos"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo antigo que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Hospital_Codigo'):
              sql = "UPDATE Hospital_Equipamentos SET Hospital_Codigo = (%s) Where Hospital_Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Equipamentos_Codigo'):
              sql = "UPDATE Hospital_Equipamentos SET Equipamentos_Codigo = (%s) Where Equipamentos_Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "7" or escolha == "hospital_pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Hospital_Pacientes"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo ou CPF antigo que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Hospital_Codigo'):
              sql = "UPDATE Hospital_Pacientes SET Hospital_Codigo = (%s) Where Hospital_Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Pacientes_CPF'):
              sql = "UPDATE Hospital_Pacientes SET Pacientes_CPF = (%s) Where Pacientes_CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "8" or escolha == "medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Medicamento WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Medicamento"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo do Medicamento que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 4):
            valornovo = float(valornovo)
            if (coluna == 'Preco'):
              sql = "UPDATE Medicamento SET Preco = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "9" or escolha == "pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Pacientes"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual CPF do Paciente que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 10):
            if (coluna == 'Data_de_Nascimento'):
              sql = "UPDATE Pacientes SET Data_de_Nascimento = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Nome'):
              sql = "UPDATE Pacientes SET Nome = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Email'):
              sql = "UPDATE Pacientes SET Email = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Endereço'):
              sql = "UPDATE Pacientes SET Endereço = (%s) Where CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "10" or escolha == "pacientes_enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Pacientes_Enfermidades"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual CPF ou Nome antigo que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Pacientes_CPF'):
              sql = "UPDATE Pacientes_Enfermidades SET Pacientes_CPF = (%s) Where Pacientes_CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Enfermidades_Nome'):
              sql = "UPDATE Pacientes_Enfermidades SET Enfermidades_Nome = (%s) Where Enfermidades_Nome = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "11" or escolha == "pacientes_medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Medicamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Pacientes_Medicamentos"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual CPF ou Codigo antigo que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Pacientes_CPF'):
              sql = "UPDATE Pacientes_Medicamentos SET Pacientes_CPF = (%s) Where Pacientes_CPF = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Enfermidades_Nome'):
              sql = "UPDATE Pacientes_Medicamentos SET Medicamentos_Codigo = (%s) Where Medicamentos_Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "12" or escolha == "recurso"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Recurso WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Recurso"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo do Recurso que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Hospital_Codigo'):
              sql = "UPDATE Recurso SET Hospital_Codigo = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Finalidade'):
              sql = "UPDATE Recurso SET Finalidade = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Origem'):
              sql = "UPDATE Recurso SET Origem = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "13" or escolha == "regiao"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Regiao WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Regiao"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo da Regiao que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Numero_de_Habitantes'):
              sql = "UPDATE Regiao SET Numero_de_Habitantes = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Nome'):
              sql = "UPDATE Regiao SET Nome = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "14" or escolha == "telefone_funcionario"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Funcionario WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Telefone_Funcionario"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Telefone que quer mudar ?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Telefone'):
              sql = "UPDATE Telefone_Funcionario SET Telefone = (%s) Where Telefone = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Funcionarios_CPF'):
              sql = "UPDATE Telefone_Funcionario SET Funcionarios_CPF = (%s) Where Telefone = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "15" or escolha == "telefone_pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Telefone_Pacientes"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Telefone que quer mudar ?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Telefone'):
              sql = "UPDATE Telefone_Pacientes SET Telefone = (%s) Where Telefone = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Pacientes_CPF'):
              sql = "UPDATE Telefone_Pacientes SET Pacientes_CPF = (%s) Where Telefone = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
      if (escolha == "16" or escolha == "testes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Testes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        try:
          for d in c.description:
            print(i, ":", d[0])
            i = i + 1
          coluna = input("Qual coluna quer modificar?")
          for d in c.description:
            if (coluna == d[0]):
              tipo = d[1]
          print("Dados:")
          sql = "SELECT * FROM Testes"
          c.execute(sql)
          for x in c:
            print(x)
          valor = input("Qual Codigo do teste que quer mudar?")
          valornovo = input("Insira o novo dado.")
          if (tipo == 3):
            valornovo = int(valornovo)
            if (coluna == 'Pacientes_CPF'):
              sql = "UPDATE Testes SET Pacientes_CPF = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          elif (tipo == 253):
            if (coluna == 'Tipo_de_Teste'):
              sql = "UPDATE Testes SET Tipo_de_Teste = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Origem'):
              sql = "UPDATE Testes SET Origem = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
            if (coluna == 'Resultado'):
              sql = "UPDATE Testes SET Resultado = (%s) Where Codigo = (%s)"
              c.execute(sql, (valornovo, valor,))
          conn.commit()
          c.close()
        except Exception as e:
          print("ERRO", e)
    if (entrada == '4'):
      c = conn.cursor()
      sql = "SHOW TABLES"
      c.execute(sql)
      i = 1
      for x in c:
        print(i, ":", x[0])
        i = i + 1
      c.close()
      escolha = input("Quer ver qual tabela? Escreva Nome ou Numero")
      if (escolha == "13" or escolha == "Regiao"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Regiao WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Regiao"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "5" or escolha == "Hospital"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "1" or escolha == "Boletim_de_COVID"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Boletim_de_COVID WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Boletim_de_COVID"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "4" or escolha == "Funcionarios"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Funcionarios WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Funcionarios"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "14" or escolha == "Telefone_Funcionario"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Funcionario WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Telefone_Funcionario"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "12" or escolha == "Recurso"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Recurso WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Recurso"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "3" or escolha == "Equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Equipamentos"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "6" or escolha == "Hospital_Equipamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Equipamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital_Equipamentos"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "9" or escolha == "Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "7" or escolha == "Hospital_Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Hospital_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Hospital_Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "16" or escolha == "Testes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Testes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Testes"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "2" or escolha == "Enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Enfermidades"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "10" or escolha == "Pacientes_Enfermidades"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Enfermidades WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes_Enfermidades"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "15" or escolha == "Telefone_Pacientes"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Telefone_Pacientes WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        c = conn.cursor()
        sql = "SELECT * FROM Telefone_Pacientes"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "8" or escolha == "Medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Medicamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Medicamentos"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()
      if (escolha == "11" or escolha == "Pacientes_Medicamentos"):
        c = conn.cursor(buffered=True)
        sql = "SELECT * FROM Pacientes_Medicamentos WHERE 1=0"
        c.execute(sql)
        print("Colunas e sua Ordem:")
        i = 1
        for d in c.description:
          print(i, ":", d[0])
          i = i + 1
        print("Dados:")
        sql = "SELECT * FROM Pacientes_Medicamentos"
        c.execute(sql)
        for x in c:
          print(x)
        c.close()

    if (entrada == '5'):
      pass
menu()