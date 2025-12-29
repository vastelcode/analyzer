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
        'mode_work': 'web',
        'area_work': 'https://www.avito.ru/velikiy_novgorod/remont_i_stroitelstvo/drova_-_kolotye_i_churkami_7830301578?context=H4sIAAAAAAAA_wEmANn_YToxOntzOjE6IngiO3M6MTY6IkhJQkV5MTRaQmt2b2hsdmwiO30kpFYKJgAAAA',
        'regex_list': ['Ford Explorer'],
        'extensions_list':['.py','.txt','.md'],
        'output_place': '/home/maksim/Тест/result.txt'
     }
    
    # поиск
      result_search = Search(user_data).run()

    
    # вывод результатов
      # output.run(result_search, user_data['output_place'])

    #  print(user_data)
     except KeyboardInterrupt:
        
        styled_print.error("Работа аварийно завершена !")


