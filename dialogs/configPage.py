from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_Dialog(object):
    def __init__(self, Dialog):
        def import_data():
            x = subprocess.check_output('pwd', shell = True)
            subprocess.run('cp c:/Users/' + x.decode('utf-8').split('/')[4] + "/desktop/passwords ./.")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Imported passwords from desktop')
            msgBox.setWindowTitle(" ")
            msgBox.setWindowIcon(QtGui.QIcon('icon.png'))
            msgBox.exec()

        def export_data():
            x = subprocess.check_output('pwd', shell = True)
            x = x.decode('utf-8').split('/')
            subprocess.run('cp ../passwords c:/Users/' + x[4] + "/desktop")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Exported passwords to the desktop')
            msgBox.setWindowTitle(" ")
            msgBox.setWindowIcon(QtGui.QIcon('icon.png'))
            msgBox.exec()

        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        Dialog.resize(317, 153)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(import_data)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(export_data)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configurations"))
        self.pushButton.setText(_translate("Dialog", "Import Data"))
        self.pushButton_2.setText(_translate("Dialog", "Export Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
