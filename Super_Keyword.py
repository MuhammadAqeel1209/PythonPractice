"""  Detail About "Super Keyword" 👇👇👇👇
The super() keyword in Python is used to refer to the parent class.
It is especially useful when a class inherits from multiple parent classes
and you want to call a method from one of the parent classes in the child class.
Simple, Super Keyword use to call any parrent class method in child class
"""

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

#-----------------INHERITANCE-------------------------
class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language = language
    def PrintInfo(self):
        print(self.name , self.id,self.language )    

Ahmed = Employee("Ahmad", 102)
Aqeel = Programmer("Aqeel", 105, "Python")
Aqeel.PrintInfo()