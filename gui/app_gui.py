from PyQt6.Qtsrc import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import randint

window_titles = [
    'Сообщение 1',
    'Сообщение 56',
    'Сообщение 78',
    'Сообщение 10',
    'Сообщение 38',
    'Сообщение 23',
]


class MainWindow(QMainWindow):

    def __init__(self):  # Исправлено: __init__ вместо init
        super().__init__()  # Исправлено: super().__init__()

        self.setWindowTitle('Моё приложение')
        self.setMinimumSize(500, 300)

        self.button = QPushButton('Изменить заголовок')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.handle_click)

        # Подключаем сигнал изменения заголовка
        self.windowTitleChanged.connect(self.change_title)

        self.setCentralWidget(self.button)

    def handle_click(self):
        # Выбираем случайный заголовок
        content = window_titles[randint(0, len(window_titles) - 1)]
        # Устанавливаем новый заголовок окна
        self.setWindowTitle(content)  # Исправлено: setWindowTitle вместо windowTitleChanged

    def change_title(self, title):
        print(f'Заголовок был сменён. Новый заголовок - {title}')


import sys

app = QApplication(sys.argv)
window = MainWindow()

def start_gui():

    print('Запущен графический интерфейс...')
    window.show()
    app.exec()