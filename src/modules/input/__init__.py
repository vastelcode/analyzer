from ...utils.helpers import prompt, option, show_list, input_mode
from ...utils.mappers import map_regex
from ...data.questionary import prompts
from ...data.extensions import extensions
from ...data.ready_regex import ready_regex

from ..validation import validator


# choice_mode_interface = prompt(**prompts['mode_interface'])

class Input:

  # запуск пользователься ввода
  def run(self):

    try:

      # выбор типа работы
      mode_work = prompt(**prompts['mode_work'])

      # ввод области работы и расширений

      result = {
         'area': None,
         'extensions': []
      }

      if mode_work == 'fs':
          
          result['area'] = input_mode('Определите область работы - ', validator.validate_dir)

          # сразу здесь получаем расширения файлов

          result['extensions'] = self.get_list(extensions,'Расширения', validator.validate_extension, 'Расширение')
      
      else:
         
         result['area'] = input_mode('Определите область работы - ', validator.validate_url)

         result['extensions'] = []
      
      area_work = result['area']
      extensions_list = result['extensions']

      # выбор типа поиска
      type_search = prompt(**prompts['type_search'])

      # получаем список регулярных выражений
      regex_list = map_regex(self.get_list(ready_regex,'Регулярные выражения', validator.validate_regex, 'Регулярное выражение'))

      return {
         'mode_work': mode_work,
         'area_work': area_work,
         'type_search': type_search,
         'extensions_list': extensions_list,
         'regex_list': regex_list
      }



    except Exception as exc:
        
        print(f'Analyzer Input Error: {exc}')
  
  def get_list(self,set_values, header, validator, header_option):
     
    print(f'? {"\033[1;96m"}{header}{'\033[0m'}')

    # спрашиваем нужно ли выводить список

    change_show = input('Выводить список (y)? ')

    if change_show.strip().lower() == 'y':
         show_list(list=set_values)
         

    # запрашиваем список регулярных выражений
    result_list = option(header_option, check_method=validator, pointer=' ? ')

    return result_list

