class Student:
      # constructor
      def __init__(self, name, age):
            self.name  = name
            self.age = age
      
      def display(self):
            print(f"my name is {self.name}")
            
"""      
s1 = Student()
s1.name = "sai"
s1.age = 45
print(s1.name)

s2 = Student()
s2.name = "raj"
s2.age = 78
"""

s1 = Student("sai", 45)
s1.display()

s2 = Student("krishvi",89)
s2.display()