import os,re

from ..styled_print import styled_print

# alias
join = os.path.join

class Search:

  def __init__(self, user_data):

    self.data = user_data
  
  # функция для поиска файлов в директории, возвращает массив файлов
  def get_files(self,root_directory,type_search,extensions):

    """
    Docstring для get_files
    
    :param root_directory: начальная директория, откуда начинается поиск
    :param type_search: тип поиска
    """

     # инициализируем списки для файлов и дерево
    files = []

    if type_search == 'deep':

     while True:
        
        # получаем содержимое директории
        list_all = os.listdir(root_directory)

        # инициализируем список папок
        dirs = []

        # проходимся по каждому элементу директории
        for index,element in enumerate(list_all):

            # определяем файл или папка
            if os.path.isfile(join(root_directory,element)):
                
                name, extension = os.path.splitext(join(root_directory,element))

                # если расширение файла есть в переданных
                if extension in extensions:
                   
                 files.append(join(root_directory,element))

            elif os.path.isdir(join(root_directory,element)):
                dirs.append(element)

        if len(dirs) == 0:
            break

        # если были папки в директории
        else:

            # проходимся по всем папкам
            for dir in dirs:
                # проходимся глубоким поиском принимая данную папку за корневую
                result = self.get_files(join(root_directory, dir),'deep',extensions=extensions)

                # добавляем результат в найденные ранее файлы
                files = files + result



        break
     
    elif type_search == 'shallow':
       
       files = os.listdir(root_directory)

    return files
  
  def scan_file(self,path_file, regex_list):
     
    #  инициализируем результат
     result = {}

    #  читаем файл
     with open(path_file,'r') as file:
        
        result.setdefault(path_file,[])
        
        # разбираем файл на строки
        for index,line  in enumerate(file):
           
          #  проходимся по каждому регулярному выражению
           for regex in regex_list:
            
            search_result = re.findall(regex,line)

            if search_result:
              
              result[path_file].append(
                 {
                    f'{index + 1}': line
                 }
              )
              
        
        file.close()
      
     return result
  
  # поиск по файловой системе
  def search_fs(self,directory, type_search, regex_list, output_place, extensions_list):

    styled_print.info('Поиск...')

    # получаем все файлы
    all_files = self.get_files(directory, type_search, extensions=extensions_list)

    all_results = {}

    for file in all_files:
       full_path = join(directory, file)

       all_results[full_path] = self.scan_file(full_path,regex_list)
       

    return all_results

  def run(self):

    user_data = self.data

    # инициализируем результат
    result = {}

    # ветвление по типу работы

    if user_data['mode_work'] == 'fs':

      result = self.search_fs(
         directory=user_data['area_work'],
         type_search=user_data['type_search'],
         regex_list=user_data['regex_list'],
         output_place=user_data['output_place'],
         extensions_list=user_data['extensions_list']
        )
           
    
    else:

      print('Веб-анализ')
    
    styled_print.success('Операция поиска успешно завершена')
    return result
