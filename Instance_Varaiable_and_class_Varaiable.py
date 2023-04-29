class Employee:
  companyName = "Apple" #-->Class Varaiable -->the varaible use any class method or object
  noOfEmployees = 0 #--> Class Varaiable
  def __init__(self, name,raise_amount):
    self.name = name #--> Instance Varaiable -->the Varaible that cn be associated with any instances
    self.raise_amount = raise_amount #--> Instance Varaiable
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Ahmed",0.3)
#emp1.raise_amount = 0.3 #Calling Instance Varaible
emp1.companyName = "Apple India" #Making Class Varaible to instance varaible -->that varaiable can be associated the istances of class at that time
Employee.showDetails(emp1)
Employee.companyName = "Google" #change the class varaible of compnayname from "Apple to Google"

emp2 = Employee("Ali",0.4)
emp2.companyName = "Nestle" #change the class varaible of compnayname from "Apple to Nestle"
emp2.showDetails()