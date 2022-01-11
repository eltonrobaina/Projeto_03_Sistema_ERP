import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'CursoPyQt2022#',
    database = 'python'
)

mycursor = mydb.cursor()

### Variaveis ###
cliente = 'Jessica'
telefone = '8794568'
cidade = 'Sao Paulo'


### DELETE TABELA ###
print('INSERT CLIENTE')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s, %s, %s)"
val = (cliente, telefone, cidade)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, 'record(s) insert')