import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'CursoPyQt2022#',
    database = 'python'
)

mycursor = mydb.cursor()

### CONSULTA TABELA ###
print('Consulta tabela cliente')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()
#print(myresult)
for line in myresult:
    print('line: ', line)