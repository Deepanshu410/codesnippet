import matplotlib.pyplot as plt
import numpy as np

# grid() = helps make plots easier to read by adding grid lines to the plot

x = np.array([2023, 2024, 2025, 2026])
y = np.array([10, 20, 15, 25])
# plt.grid() # add grid lines to the plot, vertical and horizontal.
# plt.grid(axis='x') # add grid lines to the x-axis only
plt.grid(axis='y', linewidth=2, color='grey', linestyle='dashed') # add grid lines to the y-axis only

plt.plot(x, y)
plt.show()
