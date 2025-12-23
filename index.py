# точка входа в приложение

# импорты
from src.core import Core
from src.config import config_app

app = Core(config_app)

app.run()