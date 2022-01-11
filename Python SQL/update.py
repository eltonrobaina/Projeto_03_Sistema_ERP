import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'CursoPyQt2022#',
    database = 'python'
)

mycursor = mydb.cursor()

### Variaveis ###

cidade = 'Rio de Janeiro'
idCliente = '2'


### UPDATE TABELA ###
print('UPDATE CLIENTE')
sql = "UPDATE cliente SET Cidade = %s WHERE idCliente = %s"
val = (cidade, idCliente)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, 'record(s) update')