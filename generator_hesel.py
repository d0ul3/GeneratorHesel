# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import crypt
import re
import time


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 245)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 200, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(40, 70, 81, 28))
        self.comboBox.setMaxVisibleItems(12)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Leden", "Únor", "Březen", "Duben", "Květen",
                                "Červen", "Červenec", "Srpen", "Září",
                                "Říjen", "Listopad", "Prosinec"])
        self.comboBox.setCurrentIndex(int(time.strftime("%m")) - 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 86, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton.setDefault(True)
        self.pushButton.setWhatsThis(
            "Vygeneruje 8 místné heslo na základě dvou zadaných slov a měsice")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 120, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse
                                        | QtCore.Qt.TextSelectableByKeyboard
                                        | QtCore.Qt.TextSelectableByMouse)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 50, 58, 14))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 50, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 70, 113, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pushButton_clicked(self):
        salt = str((self.comboBox.currentIndex() + 1)).zfill(2)
        self.generate(salt, self.lineEdit.text(), self.lineEdit_2.text())
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generátor hesel"))
        self.pushButton.setText(_translate("Dialog", "Generuj"))
        self.label_2.setText(_translate("Dialog", "Měsíc:"))
        self.label_3.setText(_translate("Dialog", "Heslo:"))
        self.label_4.setText(_translate("Dialog", "Heslo znovu:"))

    def generate(self, salt, password1, password2):
        if (password1 == password2):
            if (len(password1) > 3):
                password = (crypt.crypt(password1, salt))
                vystup = password[2:10].lower().capitalize()
                if (not (re.search('[A-Z]', vystup[0]))):
                    vystup = "A" + vystup[-7:]
                if (re.search('[0-9]', vystup[7])):
                    vystup = vystup[:7] + "z"
                if (not (re.search('[0-9]', vystup))):
                    vystup = vystup[:4] + "4" + vystup[-3:]
                self.label.setText(vystup)
            else:
                self.label.setText("Heslo musí mít min. 4 znaky")
        else:
            self.label.setText("Hesla se neshodují !!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

