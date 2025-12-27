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

    #  получаем данные пользователя
      # user_data = self.input_manager.run()
    
      user_data = {
        'type_search': 'deep',
        'mode_work': 'fs',
        'area_work': '/home/maksim/Тест',
        'regex_list': ['def',ready_regex['date']],
        'extensions_list':['.py','.txt','.md'],
        'output_place': 'console'
     }
    
    # поиск
      result_search = Search(user_data).run()

    
    # вывод результатов
      output.run(result_search)

    #  print(user_data)
     except KeyboardInterrupt:
        
        styled_print.error("Работа аварийно завершена !")


