#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
      self._value = value

    @property 
    def value(self):
       return self._value
    
    @value.setter 
    def value(self, value):
      if not isinstance(value, str):
        print("The value must be a string.")
      else:
        self._value = value  
    
    def is_sentence(self):
       if (self.value).endswith("."):
          return True
       else:
          return False
    
    def is_question(self):
       if (self.value).endswith("?"):
          return True
       else:
          return False
    
    def is_exclamation(self):
       if (self.value).endswith("!"):
          return True
       else:
          return False
       
    def count_sentences(self):
      new_value = re.split(r'[.!?]', self.value)
      new_value = [s.strip() for s in new_value if s.strip()]
      return len(new_value)

word1 = MyString("This is a string! It has three sentences. Right?")
print(word1.count_sentences())