class TextAnalyser:
   def __init__(self, file_name=None):
      if not file_name: 
         raise Exception("Не указан файл для анализа!")
      self.read_file(file_name)
      if not self.text:
         raise Exception(f"файл {file_name} пуст!")
      else:
         self.text_lower()
         self.print_text()
   
   def read_file(self, file_name):
      try:
         with open(file_name, 'r', encoding="UTF-8") as file:
            self.file = file
            self.text = self.file.read()
      except FileNotFoundError:
         raise Exception(f"файл {file_name} не найден!")
   
   def print_text(self):
      print(self.text)
   
   def text_lower(self):
      self.text = self.text.lower()


text = TextAnalyser('text.txt')
   