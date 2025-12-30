from ..modules.input import Input
from ..modules.search import Search
from ..modules.styled_print import styled_print
from ..modules.output import output

from ..data.ready_regex import ready_regex

class Core:

  def __init__(self, config):
      
      self.config = config

      self.input_manager = Input()

  def run(self):
     
   try:
    
    interface = self.input_manager.choice_interface()

    user_data = {}

    #   user_data = {
    #     'type_search': 'deep',
    #     'mode_work': 'fs',
    #     'area_work': '/home/maksim/Тест',
    #     'regex_list': ['int'],
    #     'extensions_list':['.py'],
    #     'output_place': '/home/maksim/Тест/result.txt',
    #     'folders_exceptions': ['/home/maksim/Тест/dir']
    #  }

    if interface == 'cli':
    #  получаем данные пользователя
      user_data = self.input_manager.run()
    # поиск
    result_search = Search(user_data).run()

    # вывод результатов
    output.run(result_search, user_data['output_place'])


   except KeyboardInterrupt:
        
        styled_print.error("Работа аварийно завершена !")


