#FUNCTION IN PYTHON
def CalculategeoMetricMean(a,b):
    geoMetricMean = (a * b)/ (a + b)
    print(geoMetricMean)

def GreaterNumber(a,b):
    if(a>b):
        print(F"{a} is greater then {b}")
    else:
        print(F"{b} is greater then {a}") 

def SmallerNumber(a,b):
    pass #-->I write pass when we want to give defination after some time        

a = 8
b = 9
GreaterNumber(a, b)
CalculategeoMetricMean(a, b)

c = 8
d = 7

GreaterNumber(c, d)
CalculategeoMetricMean(c,d)


"""
TYPES OF FUNCTION
1)USER DEFINED FUNCTION --> CREATED BY USER WHEN HE NEEDS
2) BUILT IN FUNCTION --> type(),range(),dict(),list(),tuple(),set() etc
"""
#https://www.w3schools.com/python/python_ref_functions.asp 👈 -->This is link in which all Built In Function avaiable
# geoMetricMean2 = (c * d)/ (c + d)
# print(geoMetricMean2)
