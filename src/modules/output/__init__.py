from ..styled_print import styled_print

class Output:

  def run(self,result):
      # выводим результаты поиска
      for value in result.values():
         
        #  value в данном случае объект вида {file_name: [{'line index': line}]}

        for file_name, lines in value.items():
           
           if len(value[file_name]) == 0:
              continue
           
           styled_print.highlight(f'Файл {file_name}')

           for line in lines:
              
              for line_index, line_value in line.items():
                 
                 styled_print.list_item(f'{line_index}: {line_value} ')

output = Output()