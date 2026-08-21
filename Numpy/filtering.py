import numpy as np

ages = np.array([[17, 19, 16, 32, 21, 30, 56, 11], [39, 22, 14, 99, 20, 22, 34, 18]])
teenagers = ages[ages<18]
adults = ages[(ages>=18) & (ages<65)] # using '&' instead of 'and' because numpy uses C style arrays
even = ages[ages % 2 == 0]
odd = ages[ages % 2 != 0]
print(teenagers)
print(adults)

# above boolean functions would flaten the list, break the 2d into 0d array. To preserve the original shape:
adults2 = np.where(ages>= 18, ages, 0) # where(condition, argument(which is array), fill(replacing the filtered out values with))