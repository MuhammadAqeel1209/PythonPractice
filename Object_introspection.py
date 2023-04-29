x = [1,2,3] #//list
y = (1,3,4,5,) #//Tuple
z = {1,2,3,4,5} #//Sets

#Dir 👇 --> Return the list of attribure and method which avaiable for an onject
# print(dir(z))
# print(dir(y))
# print(dir(x)) 

#Dict 👇 -->returns the dictionary representation of an object attributes Display all the methos that used using self keyword
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Aqeel",15)
print(p1.__dict__)

#help 👇 --> used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person))