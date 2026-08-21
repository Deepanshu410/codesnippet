import matplotlib.pyplot as plt
import numpy as np

# Figure = The entire canvas
# Ax = A single plot (subplot) on the figure

# print(plt.subplots(2, 2)) # plt.subplots(rows, columns) returns a tuple containing a figure and axes object(s);
# this returns a tuple containing two entities; a figure object which is our canva, and an 2d array of axes objects which are our subplots. Axes is technically a Numpy array.

# UNPACKING THE TUPLE: 
x = np.array([1,2,3,4,5])
figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x*2, color="red") # .plot(x, y)
# axes[0,0].bar(x, x*2, color="lightred") # .plot(x, y) # can also use .bar
axes[0,0].set_title("x*2") 

axes[0,1].plot(x, x**2, color="skyblue") 
axes[0,1].set_title("x**2") 

axes[1,0].plot(x, x**3, color="green") 
axes[1,0].set_title("x**3") 

axes[1,1].plot(x, x**4, color="pink") 
axes[1,1].set_title("x**4") 

plt.tight_layout()
plt.show()