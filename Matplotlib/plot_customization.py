import matplotlib.pyplot as plt 
import numpy as np
print(plt.matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026])
y = np.array([10, 20, 15, 25])
y2 = np.array([15, 28, 25, 45])
# line_style = {'marker': 'o', 'markerfacecolor': 'yellow', 'markeredgecolor': 'black', 'linestyle': '-.', 'linewidth': 2, 'markersize': 10} either this or below one, both are same. 
line_style = dict(marker='o', markerfacecolor='yellow', markeredgecolor='black', linestyle='-.', linewidth=2, markersize=10)
# markersize can also be used a short form 'ms', and markerfacecolor can also be used a short form 'mfc'. markeredgecolor can also be used a short form 'mec'. 
plt.plot(x, y,color='red', **line_style) # using unpacking operator to pass the line style as a dictionary.
plt.plot(x, y2, color='blue', **line_style) 
plt.show()