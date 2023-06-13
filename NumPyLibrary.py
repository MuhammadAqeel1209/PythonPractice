import numpy as np

myArray = np.array([3,6,32,1])  # --> 👉 Making Array
array1 = np.arange(5)           # --> 👉 create an array with values from 0 to 4
#print("Using np.arange(5):", array1)

array2 = np.arange(1, 9, 2)     # --> 👉create an array with values from 1 to 8 with a step of 2
#print("Using np.arange(1, 9, 2):",array2)
#print(myArray.ndim)            # --> 👉 Tell The Dimension

array1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8], 
                [9, 10, 11, 12]],
                
                [[13, 14, 15, 16], 
                 [17, 18, 19, 20], 
                 [21, 22, 23, 24]],

                 [[12, 1, 2, 3], 
                 [8, 28, 39, 30], 
                 [4, 5, 6, 4]],]) # --> 👉 create a 3D array with 3 "slices", each of 3 rows and 4 columns
# np.save('file1.npy', array1)      # --> 👉 save the array to a file
# print(np.load('file1.npy'))       # --> 👉 load the saved NumPy array
# print(array1)
# print(array1.size)              # --> 👉 Size Of Array --> Count the element

zeroArray = np.zeros((2, 3, 4))   # --> 👉create 3D array with dimensions 2 slices x 3 rows x 4 column filled with zeros
# print("\n3-D Array: ")
# print(zeroArray)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# with np.nditer([arr1, arr2]) as it: # --> 👉 Iterate over the arrays using nditer
#     for x, y in it:
#         print(x, y)

arrayOnes = np.ones((3,3))      # --> 👉create an array filled with ones using np.ones()
# print(arrayOnes)

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

#Syantax 👉 name.repeat(no of time)
# print(arx2.repeat(2))       # --> 👉 Repeat elements of an array.
# print(arx + arx2)           # --> 👉 Sum of Array element by element(elemnt from one matrix + element from second matrix)
# print(arx * arx2)           # --> 👉 Multiply of Array element by element(elemnt from one matrix * element from second matrix)
# print(arx - arx2)           # --> 👉 Subtarct of Array element by element(elemnt from one matrix - element from second matrix)
# print(arx / arx2)           # --> 👉 Division of Array element by element(elemnt from one matrix / element from second matrix)

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

marks = np.array([76, 78, 81, 66, 85])

# mean_marks = np.mean(marks)     # --> 👉 compute the mean of marks
# print("Mean:",mean_marks)

# median_marks = np.median(marks) # --> 👉 compute the median of marks
# print("Median:",median_marks)

# min_marks = np.min(marks)       # --> 👉 find the minimum
# print("Minimum marks:", min_marks)

# max_marks = np.max(marks)       # --> 👉 find the maximum
# print("Maximum marks:", max_marks)

matrix1 = np.array([[1, 3, 5], 
             		[7, 9, 2],
                    [4, 6, 8]])


# result = np.linalg.inv(matrix1)   # --> 👉 find inverse of matrix1
# print(result)

matrix2 = np.array([[1, 2, 3], 
             		[4, 5, 1],
                    [2, 3, 4]])

# result = np.linalg.det(matrix2)    # --> 👉 find determinant of matrix1
# print(result)

array1 = np.array([1, 2, 3, 4, 5 ])
number = 10

# result = array1 + number            # --> 👉  number sums up with each array element
# print(result)
