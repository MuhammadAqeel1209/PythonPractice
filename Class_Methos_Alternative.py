class Employee:
  # def __init__(self, name, salary):
  #   self.name = name 
  #   self.salary = salary
  name = "Ali"
  salary = "12000"
    # using @classMethod Decorates to make class Method
  @classmethod #--> Class method effect on whole class
  def fromStr(cls, string): #-->cls -->Reprsent the class
    #return cls(string.split("-")[0], int(string.split("-")[1]))
    name,salary = string.split("-")
    return cls() #--> When Constructor is have no argument then cls function has no arguments
    
e1 = Employee()
# print(e1.name)
# print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string) #-->class method call by Class name 
print(e2.name)
print(e2.salary)
print(e1.name,e1.salary)

class Person:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod #--> Class method on complete class
    def from_string(cls, string): #cls -->Represented the class --> give all argument of class constructor
        name, age,salary = string.split(',')
        return cls(name, int(age),int(salary))

person = Person.from_string("John Doe, 30,12000")  #-->class method call by Class name 
print(person.name, person.age,person.salary)