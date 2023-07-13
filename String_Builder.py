from io import StringIO
"""
Difference Between Strings and Stringd Builder
Strings 
1) Collection of Characters
2) Imuutable
3) Allocate New Memory
4) Many in built

Strings Builder
1) Collection of strings
2) Mutable
3) Adding with existing strings
4) Limited Method

 Way to create the String Builders
 1) Join
 2) string concatenation
 3) append
 4) String IO Module
"""

# --> No 1
Fruit = ["Apple","Mango","Grapes"]
symbol = "<"
#print(symbol.join(Fruit)) # --> Creation Method no 1

# --> No 2
First = "Muhammad "
Middle = "Aqeel "
Last = "Shakeel "
#print(First+Middle+Last) # --> Creation Method no 2

# --> No 3
Name = "Muhammad "
Name += "Aqeel "
Name += "Shakeel "
#print(Name) # --> Creation Method no 3

# --> No 4
data = ["Muhammad ","Aqeel ","Shakeel "]
string = StringIO()
for i in data:
    string.write(i)
#print(string.getvalue())    
