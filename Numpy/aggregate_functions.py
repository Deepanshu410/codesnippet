import numpy as np

array = np.array([[1,2,3,4,5], [6,7,8, 9,10]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # standard deviation
print(np.var(array)) # variant, the square of the std
print(np.min(array))
print(np.argmin(array)) # position of the minimum value
print(np.argmax(array)) # position of the maximum value
print(np.sum(array, axis=0)) #summing all the columns, if axis is zero apply this function to all the columns
print(np.sum(array, axis=1)) #summing all the rows, if axis is one apply this function to all the rows