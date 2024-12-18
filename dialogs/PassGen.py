from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Dialog(object):
    def __init__(self, Dialog):

        def generate_password():
            numbers = '0123456789'
            special = '!@#$%^&*()_+-=<>'
            alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
            password = ''

            for i in range(int(self.comboBox.currentText())):
                if self.checkBox_2.isChecked():
                    password = password + numbers[random.randint(0, 9)]
                elif self.checkBox.isChecked():
                    a = special + alphabet + numbers
                    password = password + a[random.randint(0, len(a) - 1)]
                else:
                    b = alphabet + numbers
                    password = password + b[random.randint(0, len(b) - 1)]
            self.lineEdit.setText(password)

        def disable_special():
            if not self.pinmode:
                self.checkBox.setEnabled(False)
                self.pinmode = True
            else:
                self.checkBox.setEnabled(True)
                self.pinmode = False


        self.pinmode = False
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 248)
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(disable_special)
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(generate_password)
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Generator"))
        self.checkBox_2.setText(_translate("Dialog", "Pin Mode"))
        self.checkBox.setText(_translate("Dialog", "Special Characters?"))
        self.label.setText(_translate("Dialog", "Amount of characters"))
        self.comboBox.setItemText(0, _translate("Dialog", "4"))
        self.comboBox.setItemText(1, _translate("Dialog", "5"))
        self.comboBox.setItemText(2, _translate("Dialog", "6"))
        self.comboBox.setItemText(3, _translate("Dialog", "7"))
        self.comboBox.setItemText(4, _translate("Dialog", "8"))
        self.comboBox.setItemText(5, _translate("Dialog", "9"))
        self.comboBox.setItemText(6, _translate("Dialog", "10"))
        self.comboBox.setItemText(7, _translate("Dialog", "11"))
        self.comboBox.setItemText(8, _translate("Dialog", "12"))
        self.comboBox.setItemText(9, _translate("Dialog", "13"))
        self.comboBox.setItemText(10, _translate("Dialog", "14"))
        self.comboBox.setItemText(11, _translate("Dialog", "15"))
        self.comboBox.setItemText(12, _translate("Dialog", "16"))
        self.comboBox.setItemText(13, _translate("Dialog", "17"))
        self.comboBox.setItemText(14, _translate("Dialog", "18"))
        self.comboBox.setItemText(15, _translate("Dialog", "19"))
        self.comboBox.setItemText(16, _translate("Dialog", "20"))
        self.pushButton.setText(_translate("Dialog", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
