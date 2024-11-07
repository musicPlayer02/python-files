class Person:
      def __init__(self,name, age):
            self.name= name
            self.age= age
            
      def display(self):
            print(f"name of the parent is {self.name}")
            
            
            
class Employee(Person):
       def __init__(self, name, age, id, salary):
             self.id = id
             self.salary = salary
             Person.__init__(self,name,age)
             
       def display_child(self):
             print(f"Id is {self.id}")
             print(f"salary is {self.salary}")
             
emp = Employee("sajni",24,101,25000)
emp.display()
emp.display_child()