import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_QuizGameMainWindow


class QuizGameMainWindow(QMainWindow, Ui_QuizGameMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #d4fc79, stop:1 #96e6a1);
            }
            QLabel, QRadioButton, QPushButton {
                font-size: 16px;
            }
        """)
        self.questions = [
            {
                "question": "Какой самый большой океан в мире?",
                "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"],
                "answer": 2
            },
            {
                "question": "Кто написал 'Войну и мир'?",
                "options": ["Пушкин", "Толстой", "Достоевский", "Чехов"],
                "answer": 1
            },
            {
                "question": "Столица Франции?",
                "options": ["Берлин", "Париж", "Мадрид", "Лондон"],
                "answer": 1
            }
        ]
        self.current_question_index = 0
        self.nextButton.clicked.connect(self.next_question)
        self.load_question()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_question(self):
        if self.current_question_index >= len(self.questions):
            QMessageBox.information(self, "Конец викторины", "Викторина завершена!")
            self.close()
            return
        q = self.questions[self.current_question_index]
        self.questionLabel.setText(q["question"])
        self.option1.setText(q["options"][0])
        self.option2.setText(q["options"][1])
        self.option3.setText(q["options"][2])
        self.option4.setText(q["options"][3])
        self.option1.setChecked(False)
        self.option2.setChecked(False)
        self.option3.setChecked(False)
        self.option4.setChecked(False)

    def next_question(self):
        q = self.questions[self.current_question_index]
        selected = None
        if self.option1.isChecked():
            selected = 0
        elif self.option2.isChecked():
            selected = 1
        elif self.option3.isChecked():
            selected = 2
        elif self.option4.isChecked():
            selected = 3
        if selected is None:
            QMessageBox.warning(self, "Ошибка", "Выберите вариант ответа!")
            return
        if selected == q["answer"]:
            QMessageBox.information(self, "Результат", "Правильно!")
        else:
            correct_option = q["options"][q["answer"]]
            QMessageBox.information(self, "Результат", f"Неправильно! Правильный ответ: {correct_option}")
        self.current_question_index += 1
        self.load_question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizGameMainWindow()
    window.show()
    sys.exit(app.exec_())
