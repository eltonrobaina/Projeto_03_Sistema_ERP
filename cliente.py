# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem

### Libs diversas ###
import mysql.connector
import pandas as pd

### Import forms sistema ###
from dadosCliente import Ui_formDadosCliente


### Import das Variaveis Controle ###
import variaveisControle

### Variáveis de conexão com o banco de dados ###
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database



class Ui_formCliente(object):
    def setupUi(self, formCliente):
        formCliente.setObjectName("formCliente")
        formCliente.resize(642, 545)
        self.bt_adicionar = QtWidgets.QPushButton(formCliente)
        self.bt_adicionar.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.bt_adicionar.setStyleSheet("image: url(:/icon_adicionar/icons/adicionar.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_adicionar.setText("")
        self.bt_adicionar.setObjectName("bt_adicionar")
        self.bt_alterar = QtWidgets.QPushButton(formCliente)
        self.bt_alterar.setGeometry(QtCore.QRect(110, 10, 101, 91))
        self.bt_alterar.setStyleSheet("image: url(:/icon_alterar/icons/alterar.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_alterar.setText("")
        self.bt_alterar.setObjectName("bt_alterar")
        self.bt_consultar = QtWidgets.QPushButton(formCliente)
        self.bt_consultar.setGeometry(QtCore.QRect(210, 10, 101, 91))
        self.bt_consultar.setStyleSheet("image: url(:/icon_consultar/icons/consultar.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_consultar.setText("")
        self.bt_consultar.setObjectName("bt_consultar")
        self.bt_excluir = QtWidgets.QPushButton(formCliente)
        self.bt_excluir.setGeometry(QtCore.QRect(310, 10, 101, 91))
        self.bt_excluir.setStyleSheet("image: url(:/icon_excluir/icons/excluir.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_excluir.setText("")
        self.bt_excluir.setObjectName("bt_excluir")
        self.bt_retornar = QtWidgets.QPushButton(formCliente)
        self.bt_retornar.setGeometry(QtCore.QRect(520, 10, 101, 91))
        self.bt_retornar.setStyleSheet("image: url(:/icon_retornar/icons/retornar.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_retornar.setText("")
        self.bt_retornar.setObjectName("bt_retornar")
        self.bt_pesquisar = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisar.setGeometry(QtCore.QRect(452, 120, 31, 25))
        self.bt_pesquisar.setStyleSheet("image: url(:/icon_pesquisar/icons/pesquisar.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_pesquisar.setText("")
        self.bt_pesquisar.setObjectName("bt_pesquisar")
        self.tb_cliente = QtWidgets.QTableWidget(formCliente)
        self.tb_cliente.setGeometry(QtCore.QRect(10, 180, 621, 341))
        self.tb_cliente.setObjectName("tb_cliente")
        self.tb_cliente.setColumnCount(4)
        self.tb_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(3, item)
        self.lb_nomeCliente = QtWidgets.QLabel(formCliente)
        self.lb_nomeCliente.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.lb_nomeCliente.setObjectName("lb_nomeCliente")
        self.txt_nomeCliente = QtWidgets.QLineEdit(formCliente)
        self.txt_nomeCliente.setGeometry(QtCore.QRect(120, 120, 321, 25))
        self.txt_nomeCliente.setObjectName("txt_nomeCliente")
        self.bt_pesquisarGeral = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisarGeral.setGeometry(QtCore.QRect(482, 120, 31, 25))
        self.bt_pesquisarGeral.setStyleSheet("image: url(:/icon_geral/icons/filtro.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.bt_pesquisarGeral.setText("")
        self.bt_pesquisarGeral.setObjectName("bt_pesquisarGeral")

        self.retranslateUi(formCliente)
        QtCore.QMetaObject.connectSlotsByName(formCliente)

    def retranslateUi(self, formCliente):
        _translate = QtCore.QCoreApplication.translate
        formCliente.setWindowTitle(_translate("formCliente", "Form"))
        self.bt_adicionar.setToolTip(_translate("formCliente", "<html><head/><body><p><img src=\":/icon_cliente/icons/cliente.png\"/></p></body></html>"))
        self.bt_alterar.setToolTip(_translate("formCliente", "<html><head/><body><p><img src=\":/icon_cliente/icons/cliente.png\"/></p></body></html>"))
        self.bt_consultar.setToolTip(_translate("formCliente", "<html><head/><body><p><img src=\":/icon_cliente/icons/cliente.png\"/></p></body></html>"))
        self.bt_excluir.setToolTip(_translate("formCliente", "<html><head/><body><p><img src=\":/icon_cliente/icons/cliente.png\"/></p></body></html>"))
        self.bt_retornar.setToolTip(_translate("formCliente", "<html><head/><body><p><img src=\":/icon_cliente/icons/cliente.png\"/></p></body></html>"))
        item = self.tb_cliente.horizontalHeaderItem(0)
        item.setText(_translate("formCliente", "ID"))
        item = self.tb_cliente.horizontalHeaderItem(1)
        item.setText(_translate("formCliente", "Nome"))
        item = self.tb_cliente.horizontalHeaderItem(2)
        item.setText(_translate("formCliente", "Telefone"))
        item = self.tb_cliente.horizontalHeaderItem(3)
        item.setText(_translate("formCliente", "Cidade"))
        self.lb_nomeCliente.setText(_translate("formCliente", "Nome cliente:"))

        ### BOTÕES SISTEMA ###
        self.bt_retornar.clicked.connect(lambda: self.sairTela(formCliente))
        self.bt_pesquisarGeral.clicked.connect(self.pesquisarGeral)
        self.bt_pesquisar.clicked.connect(self.pesquisarCliente)
        self.bt_adicionar.clicked.connect(self.cadastrarCliente)
        self.bt_consultar.clicked.connect(self.consultarCliente)
        self.bt_alterar.clicked.connect(self.alterarCliente)
        self.bt_excluir.clicked.connect(self.excluirCliente)
    

    ### FUNÇÕES SISTEMA ###
    ## Fechar telaCliente ##
    def sairTela(self, formCliente):
        formCliente.close()
    
    ## Consulta tabelaCliente por nome ##
    def pesquisarCliente(self):
        mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
        )

        mycursor = mydb.cursor()
        nomeConsulta = self.txt_nomeCliente.text()
        consultaSQL = "SELECT * FROM cliente WHERE nome LIKE '" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
        self.all_data = df

        # Carrega o arquivo na tabela tb_cliente #
        numRows = len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close()

    ## Pesquisar tabelaCliente Geral##
    def pesquisarGeral(self):
        mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
        )

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM cliente')
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
        self.all_data = df

        # Carrega o arquivo na tabela tb_cliente #
        numRows = len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close()

    ## Funcao cadastrarCliente ##
    def cadastrarCliente(self):
            variaveisControle.tipoTelaDadosCliente = 'incluir'
            print('formCliente: ', variaveisControle.tipoTelaDadosCliente)
            self.formDadosCliente = QtWidgets.QWidget()
            self.ui = Ui_formDadosCliente()
            self.ui.setupUi(self.formDadosCliente)
            self.formDadosCliente.show()

    ## Função consultarCliente ##
    def consultarCliente(self):
        # Tipo Tela dadosCliente #
        variaveisControle.tipoTelaDadosCliente = 'consultar'
        print('formCliente: ', variaveisControle.tipoTelaDadosCliente)
        # ID cliente para consulta #
        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line, 0)
        variaveisControle.idConsulta = item.text()
        print('idConsulta: ', variaveisControle.idConsulta)
        # Abertura da tela consultarCliente #
        self.formDadosCliente = QtWidgets.QWidget()
        self.ui = Ui_formDadosCliente()
        self.ui.setupUi(self.formDadosCliente)
        self.formDadosCliente.show()

    ## Função alterarCliente ##
    def alterarCliente(self):
        # Tipo Tela dadosCliente #
        variaveisControle.tipoTelaDadosCliente = 'alterar'
        print('formCliente: ', variaveisControle.tipoTelaDadosCliente)
        # ID cliente para consulta #
        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line, 0)
        variaveisControle.idConsulta = item.text()
        print('idConsulta: ', variaveisControle.idConsulta)
        # Abertura da tela consultarCliente #
        self.formDadosCliente = QtWidgets.QWidget()
        self.ui = Ui_formDadosCliente()
        self.ui.setupUi(self.formDadosCliente)
        self.formDadosCliente.show()

    ## Função excluirCliente ##
    def excluirCliente(self):
        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line, 0)
        idCliente = item.text()

        # Conexao com o banco de dados #
        mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM cliente WHERE idCliente = '" + idCliente + "'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, 'record(s) exclused')

        # Atualizar tabela com consulta completa #

        mycursor.execute('SELECT * FROM cliente')
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
        self.all_data = df

        # Carrega o arquivo na tabela tb_cliente #
        numRows = len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close()
        
### Imagens Sistema ###
import icon_adicionar
import icon_alterar
import icon_consultar
import icon_excluir
import icon_geral
import icon_pesquisar
import icon_retornar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formCliente = QtWidgets.QWidget()
    ui = Ui_formCliente()
    ui.setupUi(formCliente)
    formCliente.show()
    sys.exit(app.exec_())
