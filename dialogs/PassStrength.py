from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, Dialog):

        def analyze_password():
            password = self.lineEdit.text()
            strength = 0
            if len(password) > 8:
                strength += 1
            for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
                if i in password:
                    strength += 1
                    break
            for i in "!@#$%^&*()_+-=<>":
                if i in password:
                    strength += 1
                    break
            for i in "0123456789":
                if i in password:
                    strength += 1
                    break
            for i in "qwertyuiopasdfghjklzxcvbnm":
                if i in password:
                    strength += 1
                    break

            if strength < 3:
                self.label_2.setText(str(strength) + " Very Weak Password")
            if strength == 3:
                self.label_2.setText(str(strength) + " Weak Password")
            if strength == 4:
                self.label_2.setText(str(strength) + " Medium Password")
            if strength == 5:
                self.label_2.setText(str(strength) + " Strong Password")



        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        Dialog.resize(423, 282)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(analyze_password)
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Strengh Checker"))
        self.label_3.setText(_translate("Dialog", "Insert Password"))
        self.pushButton.setText(_translate("Dialog", "Analyze"))
        self.label.setText(_translate("Dialog", "strength:"))
        self.label_2.setText(_translate("Dialog", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
