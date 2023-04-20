"""#Decorates is a function that is used to modify the function and return it
def Greet(fx):#-->Decorates Function
    def mfx(): #-->Modify The Function
        print("Assalam u alaikum Sir!!")
        fx() #--> Simple Function
        print("Thank For Using")
    return mfx #--> Return The Modify The Function

#---------------------------------------1ST METHOD--------------------------------------

#1st Calling The Decorates
@Greet #--> Simple Method For Calling Decorates 

#2nd Make the function who want to modify
def Hello():
    print("I am Aqeel")

Hello() #Call The Funaction hat You Make

#---------------------------------------2ND METHOD--------------------------------------
#Name(Pass The Function)(Modify Function Which use in Decorates like mfx)  
# Only Calling The Function  
#Greet(Hello)() #Another Method For Calling Decorates """


#----------------------------------DECORATES WITH ARGUMENTS----------------------------------
def Greet(fx):#-->Decorates Function
    def mfx(*args, **kwargs): #-->Modify The Function
        #*args --> Taking arguments 
        #**kwargs --> Taking arguments of Dictionary in key pair value
        print("Assalam u alaikum Sir!!")
        fx(*args, **kwargs) #--> Simple Function
        print("Thank For Using")
    return mfx #--> Return The Modify The Function

@Greet
def add(a,b):
    print(a + b)
#Greet(add)(1,2)        
add(1,2) 

   

