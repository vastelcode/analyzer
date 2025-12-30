from ...utils.helpers import prompt, option, show_list, input_mode, added_point, middleware_folders
from ...utils.mappers import map_regex
from ...data.questionary import prompts
from ...data.extensions import extensions
from ...data.ready_regex import ready_regex

from ..styled_print import styled_print
from ..validation import validator


# choice_mode_interface = prompt(**prompts['mode_interface'])

class Input:

  # выбор варианта взаимодействия
  def choice_interface(self):
     
     result = prompt(**prompts['mode_interface'])

     return result

  # запуск пользователься ввода
  def run(self):

    styled_print.info('Ввод данных...')

    try:

      # выбор области работы
      area_work = input_mode('Определите область работы - ', validator.validate_dir)

      # выбор расширений
      extensions_list = added_point(self.get_list(
         header='Расширения',
         set_values=extensions,
         validator=validator.validate_extension,
         min_value=0
      ))


      # выбор типа поиска
      type_search = prompt(**prompts['type_search'])

      folders_exceptions = []

      # если глубокий поиск, то запрашиваем папки-исключения
      if type_search == 'deep':
         
         folders_exceptions = self.get_list(
         header='Папки-исключения',
         validator=validator.validate_folders,
         middleware_list=[middleware_folders,area_work],
         min_value=-1
      )
      
         


      # получаем список регулярных выражений
      regex_list = map_regex(self.get_list(
         header='Регулярные выражения',
         set_values=list(ready_regex.keys()),
         validator=validator.validate_regex,
         min_value=0
      ))

      # получаем место вывода результата

      output_place = input_mode('Определите место вывода результата (console) - ', validator.validate_file)

      styled_print.success('Операция ввода успешно завершена !')

      return {
         'mode_work': 'fs',
         'area_work': area_work,
         'type_search': type_search,
         'extensions_list': extensions_list,
         'folders_exceptions': folders_exceptions,
         'regex_list': regex_list,
         'output_place': output_place
      }



    except Exception as exc:
        
        styled_print.error(f'Analyzer Input Error: {exc}')
  
  def get_list(self, header, validator,min_value, set_values=None, middleware_list=None):
     
    print(f'? {"\033[1;96m"}{header}{'\033[0m'}')

    if set_values:
      # спрашиваем нужно ли выводить список

      change_show = input(styled_print.italic('Выводить список (y) ? ',is_print=False))

      if change_show.strip().lower() == 'y':
         show_list(list=set_values)
         

    # запрашиваем список регулярных выражений
    result_list = option( check_method=validator, min_length=min_value, middleware_list=middleware_list)

    return result_list

