import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'CursoPyQt2022#',
    database = 'python'
)

mycursor = mydb.cursor()

### DELETE TABELA ###
print('Delete Cliente')
sql = "DELETE FROM cliente WHERE idCliente = '5'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')

