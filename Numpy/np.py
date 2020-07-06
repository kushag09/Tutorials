import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

'''
print(a) = [1 2 3]
print(b) = [[1. 2. 3.]
            [4. 5. 6.]]
'''
print(a.ndim, b.ndim) # ndim tells the dimension of the array created (Answer is 1, 2)
print(a.shape, b.shape) # shape tells the number of rows and columns in form (rows, columns) (Answer is (3,) (2, 3))
# a.shape shows 3 as it is one dimensional so shows columns, b.shape shows (2, 3)

# To get the data type, we simply write a.dtype
print(a.dtype, b.dtype) # Answer is int32 and float64

#To change the data type we write
a.astype('int32')

x = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(x)
'''Gives
[[ 1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16]]
'''
# To get a specific element by indexing, we can use following code
print(x[1,7]) # It is in the form [row, column]
''' Gives 16 '''

# Getting a specific row
print(x[0, :]) # Basic list slicing method is used
'''Gives [1 2 3 4 5 6 7 8]'''

# Getting a specific column
print(x[:, 4]) # Basic list slicing method is used
'''Gives [5 13]'''

# Getting all even numbers of a specific row
print(x[0, 1:8:2]) # Column part in the form of startindex:endindex:stepsize
''' Gives [2 4 6 8] '''

# Changing element by its index
x[0,2] = 67 #Changes the first row and third column of the array to 67
print(x)
''' Gives
[[ 1  2 67  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16]]
'''

#It can be used to change the whole row/column as well
x[0, :] = 6 #It changes the whole first row to 6
print(x)
''' Gives
[[ 6  6  6  6  6  6  6  6]
 [ 9 10 11 12 13 14 15 16]]
'''

x[:, 4] = 88 #It changes the fifth column in both rows to 88
print(x)
'''Gives
[[ 6  6  6  6 88  6  6  6]
 [ 9 10 11 12 88 14 15 16]]
'''

# 3D arrays
y = np.array([[[1,2,3,4], [5,6,7,8]], [[9,10,11,12],[13,14,15,16]]])
print(y)
''' Results in:
[[[ 1  2  3  4]
  [ 5  6  7  8]]

 [[ 9 10 11 12]
  [13 14 15 16]]]
  '''
#Getting/Changing specific element is similar in 3D arrays as 2D array
#Suppose, you want to get 7 from the array
print(y[0,1,2]) #7 is present in the first block, in the second row and the third column
# it is in the form y[block, row, column]
'''Gives 7'''


#If you want to initialise an array with all the numbers being same
z = np.full((2,2), 25) #The arguments are np.full(DIMENSION OF ARRAY, NUMBER TO BE SAME)
print(z)
'''Gives
[[25 25]
 [25 25]]
'''


#If you want random decimal numbers between 0 and 1
xyz = np.random.rand(2,2) #Argument taken was DIMENSION of array to be represented
print(xyz)
'''Gives
[[0.73705504 0.24135013]
 [0.45578366 0.26414143]]
'''
#To get random integer values
integer_rand = np.random.randint(3, 10, size=(2,2)) #Shows random numbers between 3 to 10 and in form of numpy array
print(integer_rand)
''' Gives
[[8 3]
 [7 8]]

 NOTE: IT IS ALWAYS RANDOM SO IT ANSWER MAY NOT BE THE SAME ALWAYS
 '''

#If you want to repeat an array multiple times
tst_arr = np.array([[1,2,3]])
rep = np.repeat(tst_arr, 3, axis=0) #Arguments are in the form np.repeat(ARRAY, NO. OF TIMES TO REPEAT, AXIS = HORIZONTAL(0)/VERTICAL(1))
print(rep)
'''Gives
[[1 2 3]
 [1 2 3]
 [1 2 3]]
'''

#Lets make a design
design = np.ones((5,5))  #np.ones is same as np.full((5,5), 1)

design_ini = np.zeros((3,3)) #np.zeros is same as np.full((3,3), 0)
design_ini[1,1] = 9 #Changing the middle value

design[1:4, 1:4] = design_ini
print(design)
''' Result:
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
'''

#Numpy can also be used to do maths
#Lets see an example

tester = np.array([1,2,3,4,5])
print(tester+2) #This adds 2 to each element of the array
'''Giving answer of [3 4 5 6 7]'''

# You can also add 2 arrays with each other
test1 = np.array([6,2,4,6,3])
print(tester + test1) # It adds 1st element of tester to 1st element of test1 and so on...
'''Giving answer of [7 4 7 10 8]'''

#And like this, you can do other calculations as well like multiplication, division, subtraction, indices, trigonometry etc.

#You can also find max value min value or sum of values of array

tests = np.array([[4,6,2],[1,7,3]])
print(np.min(tests)) # Finds smallest value in the array (Answer is 1)
print(np.max(tests)) # Finds largest value in the array (Answer is 7)
print(np.sum(tests)) # Sums all the values in the array itself (Answer is 23)

#We can also stack arrays
test21 = np.array([1,2,3,4,5])
test22 = np.array([6,3,1,5,6]) #Only the fact that the shape of arrays should be same while vertically stacking
print(np.vstack([test21, test22]))
''' Returns:
[[1 2 3 4 5]
 [6 3 1 5 6]]
'''

#Horizontal stacking
test23 = np.ones((2,6))
test24 = np.zeros((2,4))
print(np.hstack([test23, test24]))
''' Returns:
[[1. 1. 1. 1. 1. 1. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1. 1. 0. 0. 0. 0.]]
'''
#You can also apply conditions on numpy arrays
print(test21 > 3) #Applies condition on each element and represent it in array with True/False
''' Returns: [False False False True True] '''

#If you want values that are greater than 3 then -
print(test21[test21>3])
''' Returns: [4 5]'''
