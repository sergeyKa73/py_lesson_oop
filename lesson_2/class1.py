from class3 import Verification

class V2(Verification):

     def __init__(self, login, password, age):
         super().__init__(login, password) # наследование метод  super
         self.__save()
         self.age = age

     def __save(self):
          with open('users') as r:
               for i in r:
                    if f'{self.login, self.password}'+'\n' == i:
                         raise ValueError ('такой login есть!')
          
          Verification.save(self) # простое наследование
     
     def show(self):
          return self.login, self.password



x = V2('Tom', '978453216', 18)
