from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import MainWindow


class Ui_Login(object):
    def __init__(self, Login, exists):
        Login.setWindowIcon(QtGui.QIcon('icon.png'))
        Login.setObjectName("Login")
        #Login.setStyleSheet("background-color: lightgrey")
        self.wf = open('./pin', 'a')
        Login.resize(237, 210)
        self.gridLayout = QtWidgets.QGridLayout(Login)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Login)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label.setStyleSheet("font: 20pt \"MS Gothic\";\n""text-decoration: underline;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.placeholderText()
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Login)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        #self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_2.setObjectName("pushButton_2")
        #self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)


                

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Log in"))
        self.label.setText(_translate("Login", "Insert Pin"))


if __name__ == "__main__":
    def closewin(ui):
        Login.close()

    def set_pass(ui):
        ui.wf = open('./pin', 'w')
        ui.wf.write(ui.lineEdit.text())
        ui.wf.close()
        if len(ui.lineEdit.text()) > 0:
            ui.pushButton.clicked.connect(lambda: login(ui))
            ui.lineEdit.setPlaceholderText("password")
            ui.pushButton.setText("Log In")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Password set, you may log in now')
            msgBox.setWindowTitle(" ")
            msgBox.setWindowIcon(QtGui.QIcon('icon.png'))
            msgBox.exec()

    def login(ui):
        #print('bbb', uif.readline(), type(uif.readline()))
        ui.f = open('./pin', 'r')
        if ui.lineEdit.text() == ui.f.readline():
            ui.new_window = QtWidgets.QMainWindow()
            MainWindow.Ui_MainWindow(ui.new_window) 
            ui.new_window.show()
            closewin(ui)
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Wrong Password, try again')
            msgBox.setWindowTitle("Error")
            msgBox.setWindowIcon(QtGui.QIcon('icon.png'))
            msgBox.exec()

        
    exists = False
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login(Login, exists)
    if os.stat('./pin').st_size > 0:
        exists = True
        ui.lineEdit.setPlaceholderText("password")
        ui.pushButton.setText('Log in')
        ui.pushButton.clicked.connect(lambda: login(ui))
    else:
        ui.lineEdit.setPlaceholderText("Set password")
        ui.pushButton.setText('Set password')
        ui.pushButton.clicked.connect(lambda: set_pass(ui))
    #ui.setupUi(Login, exists)
    Login.show()
    sys.exit(app.exec_())
