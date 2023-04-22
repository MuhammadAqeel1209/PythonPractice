class Person: #--> Class
    name = "M.Aqeel"
    occupation = "Software Engineer"

    #Self is like this keyword in Python
    def info(self):#self-->reference of current instance in the class,used to access varaible that belongs to class
        print(f"{self.name} is a {self.occupation}") #-->Function
    
    # def __init__(self): #-->Default Constructor
    #     print("Hello I am Aqeel")  
    def __init__(self,name,occupation): #-->Parameter Constructor
           self.name = name
           self.occupation = occupation

    #--------------------------GETTER----------------------------
    @property
    def Name(self):
        return self.name 
    @property
    def Occ(self):
        return self.occupation      

    #--------------------------SETTER----------------------------
    @Name.setter
    def SetName(self,name):
        self.name = name
    @Occ.setter
    def SetOcc(self,Occ):
        self.occupation = Occ    


        
p1 = Person("Aqeel","HR") #-->Making Object and Calling Parameter Constructor
p2 = Person("Ali","Employee")
print(p1.Name) #--> Getter 
print(p2.Name) #--> Getter
print(p1.Occ)  #--> Getter
p1.SetName = "Ahmed" #-->Setter
p2.SetName = "Amna" # -->Setter
p1.SetOcc = "CR"
print(p1.Name)  #--> Getter
print(p2.Name)  #--> Getter
# p1.name = "Ali" #-->Direct Varaiable
# p1.occupation = "Doctor" #-->Direct Varaiable
# print(p1.name) #-->Direct Varaiable
# print(p1.occupation)  #-->Direct Varaiable
p1.info()  #-->Method Calling
p2.info() #--> Method Calling