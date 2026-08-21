import matplotlib.pyplot as plt 
import numpy as np
print(plt.matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026])
y = np.array([10, 20, 15, 25])
plt.plot(x, y) # argument x, for coordinates of x axis and argument y, for coordinates of y axis.
# if only one argument is provided, it will be assumed as an argument of y values, and x values will be automatically generated and plotted against y.
plt.show()