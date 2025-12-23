from src.utils.mappers import map_term
from ..data.ready_regex import ready_regex
from ..data.extensions import extensions

from re import compile

def prompt(questionary, map_key, allowed, parameter):
    
    # получаем значение
    value = questionary.ask()
    # получаем программное имя
    value = map_term(value,map_key)

    # если нет в разрешенном наборе
    if value not in allowed:

        raise Exception(f'{parameter} {value} temporarily unavailable')

    return value

def option( parametr_name ,check_method,pointer: str ):
    
    print('Введите exit для остановки процесса')

    values = []

    counter = 1

    while True:
    
      value = input(f'{pointer} {parametr_name} {counter} - ')  

      if value.strip().lower() == 'exit':

        if len(values) > 0:
         break
        
        print('Вы должны ввести хотя бы одно значение')
        continue

      check = check_method(value)

      if check['result']:
        values.append(value)
        counter += 1
      
      else:

          print(check['error_message'])
          continue
    
    return values

def input_mode(text, validator):
   
   while True:
   
    value = input(text)

    check = validator(value)

    if check['result']:
      
      return value
    
    else:
       
       print(check['error_message'])
       continue


def show_list(list, header='List'):
    print(f'=== {header} ===')

    for name in list:
        
        print(f'- {name}')


