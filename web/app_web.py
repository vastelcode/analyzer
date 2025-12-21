from flask import Flask, render_template
import os, logging


# отключаем сообщения в консоли
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
# log.disabled = True

# определяем текущую директорию
current_dir = os.path.dirname(os.path.abspath(__file__))

# функция запуска приложения
def start_web():

    print('Запущено веб-приложение...')

    # Создаём экземпляр приложения Flask
    app = Flask(__name__, template_folder=current_dir)

    # главная страница
    @app.route('/')
    def index():
        """Отображает главную страницу с кнопкой."""
        return render_template('index.html')

    @app.route('/send_message', methods=['POST'])
    def send_message():
        """Обрабатывает POST‑запрос от кнопки и выводит сообщение в консоль."""
        print('Кнопка "Вывод" была нажата! Сообщение отправлено в консоль.')
        return {'status': 'success', 'message': 'Сообщение выведено в консоль'}

    if __name__ == 'web.app_web':

        print('Перейдите по ссылке - http://localhost:5000')

        # Запускаем приложение на локальном сервере
        app.run(host='localhost', port=5000, debug=False)

