from ..modules.input import Input

class Core:

  def __init__(self, config):
      
      self.config = config

      self.input_manager = Input()
  
  def run(self):
     
    #  получаем данные пользователя
     user_data = self.input_manager.run()
    
    # поиск

     print(user_data)


