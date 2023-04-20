#DOC is a special type of strings and display the comment it is not comment 
#and write it after from function name
def square(n):
    """Take a number_______ and print the sqaure"""
    print(n**2)

square(5)   
print(square.__doc__)

def number(n):
    print(n)
    """Print number"""

print(number.__doc__)

#PEP 8 it is a document that guideline and best practice for python tutioral
import this #The Zen of Python, by Tim Peters 