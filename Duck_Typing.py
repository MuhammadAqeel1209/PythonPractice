# class Duck:
#     def Walk(self):
#         print("thapak thapak")

# class Horse:
#     def Walk(self):
#         print("tabdak tabdak")

# class Cat:
#     def Talk(self):
#         print("meow meow")

# def MyFun(obj):
#     # --> Condition to check Method Avaiable or not 👇👇👇
#     # --> hasattr() --> Syntax --> hasattr(object,attribute) --> Object --> Class Object --> attruibute --> Method in the class
#     if hasattr(obj,"Walk"):
#         obj.Walk()
# D = Duck()
# H = Horse()
# C = Cat()

# MyFun(D)
# MyFun(H)
# MyFun(C)

class Duck:
    def Sound(self):
        print("quack quack")

class Dog:
    def Sound(self):
        print("woof woof")

class Cat:
    def __init__(self):
        self.sound = "meow meow"

def All_Sound(obj):
    # --> Condition to check Method Avaiable or not 👇👇👇
    # --> hasattr() --> Syntax --> hasattr(object,attribute) --> Object --> Class Object --> attruibute --> Method in the class
    if hasattr(obj,"Sound"):
        obj.Sound()
duck = Duck()
dog = Dog()
cat = Cat()

All_Sound(duck)
All_Sound(dog)
All_Sound(cat)