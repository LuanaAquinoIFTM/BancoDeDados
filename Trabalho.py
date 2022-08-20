#Atividade prática 02 - Data: 24/08/2022 - Valor: 10 pontos
#Fazer um sistema de consultas ao banco de dados Northwind.
#Ao entrar no sistema, aparece um menu numerado com todas as tabelas do banco.
#Ao escolher uma tabela, aparece outro menu numerado com todos os campos (colunas) 
# da tabela escolhida.Ao escolher o campo (coluna), o usuário deve digitar algum
#  conteúdo para ser pesquisado nesse campo, nessa tabela.O sistema deve exibir na 
# tela o resultado da consulta.

import mysql.connector

mydb = mysql.connector.connect(
    host = "relational.fit.cvut.cz",
    user = "guest",
    password = "relational",
    database = "northwind"

)
print("-------------------------TABELAS-------------------------")
print("| 1 - Customers (Clientes)                              |")
print("| 2 - Employees (Empregados)                            |")
print("| 3 - Orders (Compras)                                  |")
print("| 4 - Suppliers (Fornecerdores)                         |")
print("| 5 - Products (Produtos)                               |")
print("| 6 - Shippers (Carregadores)                           |")
print("| 7 - Categories (Categorias)                           |")
print("| 8 - CustomerCustomerDemo (ClienteClienteDemo)         |")
print("| 9 - CustomerDemographics (DadosDemográficosDoCliente) |")
print("| 10 - Order Details (Detalhes do Pedido)               |")
print("| 11 - EmployeeTerritories (TerritóriosDoFuncionário)   |")
print("| 12 - Region (Região)                                  |")
print("| 13 - Territories (Territórios)                        |")
print("---------------------------------------------------------")
print("Escolha uma tabela a ser consultada:")


opcao = input()
if (opcao == '1'):
    tabela = "Customers"
    print("1 - CustomerID")
    print("2 - CompanyName")
    print("3 - ContactName")
    print("4 - ContactTitle")
    print("5 - Address")
    print("6 - City")
    print("7 - Region")
    print("8 - PostalCode")
    print("9 - Country")
    print("10 - Phone")
    print("11 - Fax")
    print("Escolha um campo a ser consultada:")
    campo = input()
    if(campo == "1"):
        coluna = "CustomerID"
        print("Digite um ID a ser pesquisado:")
        id = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{id}%"')
        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "2"):
        coluna = "CompanyName"
        print("Digite uma companhia para ser pesquisada")
        companhia = input()
    
        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{companhia}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "3"):
        coluna = "ContactName" 
        print("Digite um nome a ser pesquisado")
        nome = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{nome}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "4"):
        coluna = "ContactTitle" 
        print("Digite um título de contato a ser pesquisado")
        t_cont = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{t_cont}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "5"):
        coluna = "Address" 
        print("Digite um endereço a ser pesquisado")
        ender = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{ender}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "6"):
        coluna = "City" 
        print("Digite uma cidade a ser pesquisada")
        cid = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{cid}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "7"):
        coluna = "Region" 
        print("Digite uma região a ser pesquisada")
        regiao = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{regiao}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "8"):
        coluna = "PostalCode" 
        print("Digite um código postal a ser pesquisado")
        cod_postal = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{cod_postal}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "9"):
        coluna = "Country" 
        print("Digite um país a ser pesquisado")
        pais = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{pais}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "10"):
        coluna = "Phone" 
        print("Digite um telefone a ser pesquisado")
        phone = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{phone}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)

    if(campo == "11"):
        coluna = "Fax" 
        print("Digite um fax a ser pesquisado")
        fax = input()

        mycursor = mydb.cursor()

        mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{fax}%"')

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)


if (opcao == '2'):
    tabela = "Employees"
    coluna = "FirstName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if (opcao == '3'):
    tabela = "Orders"
    coluna = "OrderID"
    print("Digite o id da compra ser pesquisado:")
    nome = input()

if (opcao == '4'):
    tabela = "Suppliers"  
    coluna = "ContactName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if (opcao == '5'):
    tabela = "Products"
    coluna = "ProductName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if (opcao == '6'):
    tabela = "Shippers"
    coluna = "CompanyName"
    print("Digite um nome a ser pesquisado:")
    nome = input()