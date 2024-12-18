from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip
import os

class Ui_Dialog(object):
    def __init__(self, Dialog):
        self.dict = {}
        def init_passwords():
            f = open('./passwords', 'r')
            f = f.readline().split('#')
            for i in f:
                if not i:
                    return
                i = i.split(':')
                self.dict[i[0]] = i[1]
                update_list()

        def add_dict():
            f = open('./passwords', 'a')
            f.write(self.lineEdit_2.text() + ":" + self.lineEdit.text() + "#")
            self.dict[self.lineEdit_2.text()] = self.lineEdit.text()
            msgBox = QtWidgets.QMessageBox()
            update_list()

        def update_list():
            self.listWidget.clear()
            for i in self.dict:
                self.listWidget.addItem(i+': ' + self.dict[i])

        def copy(item):
            pyperclip.copy(item.text().split(': ')[1])


        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        Dialog.resize(604, 442)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(70, 110, 151, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(149, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(add_dict)
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 271, 391))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(copy)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        try:
            if os.stat('./passwords').st_size > 0:
                init_passwords()
        except:
            open('./passwords', 'x')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Manager"))
        self.groupBox_2.setTitle(_translate("Dialog", "Add Password"))
        self.label.setText(_translate("Dialog", "Insert Password"))
        self.label_2.setText(_translate("Dialog", "Insert Website"))
        self.pushButton.setText(_translate("Dialog", "Add Password"))
        self.groupBox.setTitle(_translate("Dialog", "Password List"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
