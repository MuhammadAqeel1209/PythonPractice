import numpy as np

myArray = np.array([3,6,32,1])  # --> 👉 Making Array
#print(myArray.ndim)            # --> 👉 Tell The Dimension
#Syantx 👉 name.repeat(no of time)
# print(myArray.repeat(3))      # --> 👉 Repeat elements of an array.
# print(myArray.mean())         # --> 👉 Returns the average of the array elements along given axis.
# print(myArray.max())          # --> 👉 Return the maximum along a given axis.
# print(myArray.min())          # --> 👉 Return the minimum along a given axis.
# save = myArray.copy()         # --> 👉 Return a copy of the array.
# print(save)                   # --> 👉 Print the copy array
# print(myArray.argmax())       # --> 👉 Tell Index of  Maximum Number 
# print(myArray.argmin())       # --> 👉 Tell Index of  Minimum Number
# print(myArray.argsort())      # --> 👉 Sort the array and Give the array index in sorting form
myArr = np.array([[3,6,32,7]])
# print(myArray)
# print(myArray[3])             # --> 👉 Print the value at that index 
# print(myArr[0,3])             # --> 👉 Print the value at that index 
#print(myArr.shape)             # --> 👉 Tell How Many Row and Col
#print(myArray.shape)           # --> 👉 Tell How Many Row and Col
# print(myArr.dtype)            # --> 👉 Find The Data Type
# myArr[0,1] = 45               # --> 👉 Change The Element
# print(myArr)

a = np.array([1+2j, 3+4j, 5+6j])# --> 👉 Complex Number Array
# print(a.real)                 # --> 👉 The Real Part Of The Array.
# print(a.imag)                 # --> 👉 The Imaginary Part Of The Arra..
# print(a.conj())               # --> 👉 Complex-Conjugate All Elements.
# print(a.conjugate())          # --> 👉 Complex-Conjugate All Elements.

                                # --> 👇 Making Two Dimensonal Array    
listArray = np.array([[1,2,3],[5,8,5],[0,3,2]])
# print(listArray)
# print(listArray.shape)        # --> 👉 Tell How Many Row and Col
#print(listArray.size)          # --> 👉 Count The Element Of Array
# print(listArray.dtype)        # --> 👉 Find The Data Type
# print(listArray[2,0])         # --> 👉 Print the value at that index

x = np.array([1, 2, 2.5])
#print(x.astype(int))           # --> 👉 Type Casting.
zero = np.zeros((2,5))          # --> 👉 Making NULL Array
#print(zero)
#print(zero.dtype)              # --> 👉 Find The Data Type

rng = np.arange(15)             # --> 👉 Making The Start From 0 to Value that we give in example we give 15 
#print(rng)

#name = np.linspace(Start,End,Space) 👈 Synatx
space = np.linspace(1,5,12)     # --> 👉 Used to create an evenly spaced sequence in a specified interval.
#print(space)
#name = np.empty(Row,Col)👈 Synatx
emp = np.empty((1,3))           # --> 👉 to return new array of a given shape and type. It has random values and uninitialized entries.
#print(emp)

ide = np.identity(5)            # --> 👉 Making Identity matrix
#print(ide)

arx = np.array([[1,2,3],
            [4,5,6],
            [7,1,0]])

arx2 = np.array([[1,2,3],
            [4,5,6],
            [7,1,0]])

#Syantx 👉 name.repeat(no of time)
# print(arx2.repeat(2))       # --> 👉 Repeat elements of an array.
# print(arx + arx2)           # --> 👉 Sum of Array element by element(elemnt from one matrix + element from second matrix)
# print(arx * arx2)           # --> 👉 Multiply of Array element by element(elemnt from one matrix * element from second matrix)

# print(np.sqrt(arx * arx2))  # --> 👉 Square Root of all element

 # --> 👇 sum() --> 👉 Sum the all element , max() --> 👉 Maximum Number, min() --> 👉 Minimum Number
#print(arx.sum(),"\n",arx.max(),"\n",arx.min())

#print(np.where(arx >5 ))     # --> 👉 Find Number that greater than number that we give and return the index of that number
#print(np.count_nonzero(arx2))# --> 👉 Count Non Zero Number

#print(arx.diagonal())        # --> 👉 Return specified diagonals.

# print(arx)
# print(arx.argmax())         # --> 👉 Give the index of maximum number in two dimension in form of 0,1,2,etc
# print(arx.argmin())         # --> 👉 Give the index of minimum number in two dimension in form of 0,1,2,etc
#axis = 0 --> Col and axis = 1 --> Row
#print(arx.argmax(axis=0))    # --> 👉 Give the index of maximum number in two dimension from col in form of matrix index[0,2,3] etc
# print(arx.argmax(axis=1))   # --> 👉 Give the index of maximum number in two dimension from row in form of  matrix index[0,2,3] etc
# print(arx.argmin(axis=0))   # --> 👉 Give the index of minimum number in two dimension from col in form of matrix index[0,2,3] etc
# print(arx.argmin(axis=1))   # --> 👉 Give the index of maximum number in two dimension from row in form of matrix index[0,2,3] etc
#print(arx.argsort(axis=0))   # --> 👉 Sort the array col wise because axis = 0 and Give the array index in sorting form 
#print(arx.argsort(axis=1))   # --> 👉 Sort the array row wise because axis = 1 and Give the array index in sorting form 
#print(arx.nbytes)            # --> 👉 Tell How many number of bytes cosume




# for num in arx.flat:        # --> 👉 A 1-D iterator over the array.
#     print(num)

#print(arx.sum(axis=0))       # --> 👉 Sum of element of matrix of col 
#print(arx.sum(axis=1))       # --> 👉 Sum of element of matrix of row 

# print(arx.ndim)             # --> 👉 Tell The Dimension
# print(arx.T)                # --> 👉 Transpose of matrix 

