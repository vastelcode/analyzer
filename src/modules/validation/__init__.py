from ...data.extensions import extensions
from ...data.ready_regex import ready_regex
from re import compile, error, match
import os, requests


class Validation():

  def validate_extension(self,ext):

    if f'.{ext}' in extensions:

      return {'result': True}
    
    return {'result': False, 'error_message': f'Расширение .{ext} недоступно. '}
  
  def validate_regex(self, regex):

    try:

      compile(regex)
      return {'result': True}
    
    except error:

      return {'result': False, 'error_message': f'Невалидное регулярное выражение {regex} '}
  
  def validate_dir(self,path):

    if os.path.isdir(path):

      return {'result': True}
    
    else:

      return {'result': False, 'error_message': f'{path} не является папкой'}
  
  def validate_url(self, url):

    # проверка соотвествия
    if match(ready_regex['url'], url):
      pass
    
    else:
     return {'result': False, 'error_message': f'{url} не соотвествует шаблону URL'}
    
    response = requests.get(url)

    if response.status_code != 200:

      return {'result': False, 'error_message':f'{url} выдаёт ошибку'}
    
    else:
      return {'result': True}
  
  def validate_file(self, path):

    if os.path.isfile(path) or path.strip().lower() == 'console' :

      return {'result': True}
    
    else:

      return {'result': False, 'error_message': f'{path} не является файлом'}
  
  def validate_folders(self,path):

    if path == '/':

      return {'result': False, 'error_message': f'Текущую директорию нельзя внести в исключения'}
    
    if not os.path.isdir(path):

      return {'result': False, 'error_message': f'Такой директории {path} не существует'}
    
    else:
      return {'result': True}





validator = Validation()    