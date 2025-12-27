from src.utils.mappers import map_term
from ..data.ready_regex import ready_regex
from ..data.extensions import extensions

from ..modules.styled_print import styled_print

from re import compile

def prompt(questionary, map_key, allowed, parameter):
    
    # получаем значение
    value = questionary.ask()
    # получаем программное имя
    value = map_term(value,map_key)

    # если нет в разрешенном наборе
    if value not in allowed:

       styled_print.error(f'{parameter} {value} temporarily unavailable')

    return value

def option( parametr_name ,check_method,pointer: str ):
    
    styled_print.info('Введите exit для остановки процесса')

    values = []

    counter = 1

    while True:
    
      value = input(styled_print.list_item(f' ',is_print=False))  

      if value.strip().lower() == 'exit':

        if len(values) > 0:
         break
        
        styled_print.warning('Вы должны ввести хотя бы одно значение')

        continue

      check = check_method(value)

      if check['result']:
        values.append(value)
        counter += 1
      
      else:

          styled_print.error(check['error_message'])
          continue
    
    return values

def input_mode(text, validator):
   
   while True:
   
    value = input(styled_print.styled_text('? ', is_print=False) + styled_print.highlight(text, is_print=False))

    check = validator(value)

    if check['result']:
      
      return value
    
    else:
       
       styled_print.error(check['error_message'])
       continue


def show_list(list, header='List'):
    
    styled_print.title(header)

    result = {
       'last_index': None
    }

    for index,name in enumerate(list):
        # если не последний индекс
        if index != len(list) - 1:
           
           if index != result['last_index']:
              # выводим сразу две штуки
              styled_print.list_item(f'{name}, {list[index + 1]}')
              result['last_index'] = index + 1
           
           else:
              
              continue
        else:
           styled_print.list_item(f'{name}')

# функция для добавления точки
def added_point(extensions):
   
   for index,extension in enumerate(extensions):
      
      extensions[index] = f'.{extension}'
  
   return extensions
      

