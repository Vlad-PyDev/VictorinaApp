from PyQt5 import QtCore, QtWidgets


class Ui_QuizGameMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("QuizGameMainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(20, 20, 560, 60))
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setObjectName("questionLabel")

        self.option1 = QtWidgets.QRadioButton(self.centralwidget)
        self.option1.setGeometry(QtCore.QRect(20, 100, 560, 30))
        self.option1.setObjectName("option1")

        self.option2 = QtWidgets.QRadioButton(self.centralwidget)
        self.option2.setGeometry(QtCore.QRect(20, 140, 560, 30))
        self.option2.setObjectName("option2")

        self.option3 = QtWidgets.QRadioButton(self.centralwidget)
        self.option3.setGeometry(QtCore.QRect(20, 180, 560, 30))
        self.option3.setObjectName("option3")

        self.option4 = QtWidgets.QRadioButton(self.centralwidget)
        self.option4.setGeometry(QtCore.QRect(20, 220, 560, 30))
        self.option4.setObjectName("option4")

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(250, 280, 100, 40))
        self.nextButton.setObjectName("nextButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Викторина"))
        self.questionLabel.setText(_translate("MainWindow", "Вопрос будет здесь"))
        self.option1.setText(_translate("MainWindow", "Вариант 1"))
        self.option2.setText(_translate("MainWindow", "Вариант 2"))
        self.option3.setText(_translate("MainWindow", "Вариант 3"))
        self.option4.setText(_translate("MainWindow", "Вариант 4"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))
