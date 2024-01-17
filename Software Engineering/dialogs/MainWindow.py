from PyQt5 import QtCore, QtGui, QtWidgets
import PassOrg, PassGen, PassStrength, configPage

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.resize(450, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def open_pass_manager():
            self.Dialog = QtWidgets.QWidget()
            PassOrg.Ui_Dialog(self.Dialog)
            self.Dialog.show()

        def open_pass_generator():
            self.Dialog = QtWidgets.QWidget()
            PassGen.Ui_Dialog(self.Dialog)
            self.Dialog.show()

        def open_strength_checker():
            self.Dialog = QtWidgets.QWidget()
            PassStrength.Ui_Dialog(self.Dialog)
            self.Dialog.show()

        def open_configurations():
            self.Dialog = QtWidgets.QWidget()
            configPage.Ui_Dialog(self.Dialog)
            self.Dialog.show()

        self.pushButton.clicked.connect(open_pass_manager)
        self.pushButton_2.clicked.connect(open_pass_generator)
        self.pushButton_3.clicked.connect(open_strength_checker)
        self.pushButton_4.clicked.connect(open_configurations)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PogLock"))
        self.pushButton.setText(_translate("MainWindow", "Password Manager"))
        self.pushButton_2.setText(_translate("MainWindow", "Password Generator"))
        self.pushButton_3.setText(_translate("MainWindow", "Strength Checker"))
        self.pushButton_4.setText(_translate("MainWindow", "Configurations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
