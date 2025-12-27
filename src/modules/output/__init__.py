from ..styled_print import styled_print

class Output:

  def enumeration_result(self,result, function, function_s = False):
    styled_print.info('Вывод...')

    if not bool(function_s):
       function_s = function

    for value in result.values():
         
        #  value в данном случае объект вида {file_name: [{'line index': line}]}

        for file_name, lines in value.items():
           
           if len(value[file_name]) == 0:
              continue
           
           function(f'Файл {file_name} \n')

           for line in lines:
              
              for line_index, line_value in line.items():
                 
                 function_s(f'{line_index}. {line_value} ')

  def run(self,result,output_place):
        
        if output_place == 'console':
           
           self.enumeration_result(result,styled_print.highlight,styled_print.list_item)
        
        # иначе пишем в файл
        else:
           
          with open(output_place, 'a') as file:
             
             self.enumeration_result(result,file.write)

             file.close()
        
        styled_print.success('Операция вывода успешно завершена !')

            

           

output = Output()