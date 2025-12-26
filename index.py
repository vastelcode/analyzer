# точка входа в приложение

# импорты
from src.core import Core
from src.config import config_app

# создаём приложение
app = Core(config_app)

# запускаем
app.run()