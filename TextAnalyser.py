class TextAnalyser:
   def __init__(self, file_name=None):
      if not file_name: 
         raise Exception("Не указан файл для анализа!")
      self.file_name = file_name
      self.read_file()
      self.prepare_text()
      self.print_text()
   
   def read_file(self):
      try:
         with open(self.file_name, 'r', encoding="UTF-8") as file:
            self.file = file
            self.text = self.file.read()
      except FileNotFoundError:
         raise Exception(f"файл {self.file_name} не найден!")
   
   def print_text(self):
      print(self.text)
   
   def prepare_text(self):
      if not self.text:
         raise Exception(f"файл {self.file_name} пуст!")
      self.text = self.text.lower()


text = TextAnalyser('text.txt')
