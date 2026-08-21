import matplotlib.pyplot as plt 
import numpy as np
print(plt.matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026])
y = np.array([10, 20, 15, 25])
y2 = np.array([15, 28, 25, 45])

# labels: 
plt.title('Class Size', fontsize=16, fontweight='bold',family='Arial', color='Green')
plt.xlabel('Year', fontsize=12, fontweight='bold' ,fontfamily='Arial', color='green')
plt.ylabel('Number of Students', fontsize=12, fontweight='bold', family='Arial', color='green')
plt.tick_params(axis='both', labelsize=10, labelcolor='grey', labelrotation=45)
#
plt.plot(x, y) 
plt.plot(x, y2) 

plt.xticks(x) # x-axis ticks

plt.show()