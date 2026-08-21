import matplotlib.pyplot as plt
import numpy as np

# scatter graphs = Use dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. Good for visualizing relationships between two numeric variables. Helps to identify correlations(+,-, None), trends, and outliers in data. Eg., Study hours vs test scores. 
x1 = np.array([1, 2, 3, 4, 5]) # hours studied
y1 = np.array([20, 40, 60, 80, 100]) # scores achieved
x2= np.array([1, 2, 3, 4, 5]) # hours studied
y2 = np.array([30, 50, 70, 95, 100]) # scores achieved
plt.scatter(x1, y1, color='blue', alpha=0.5, 
            s = 100, label='Group 1') # scatter plot with blue dots, alpha for transparency, s for size of dots, label for legend
plt.scatter(x2, y2, color='red', alpha=0.5, 
            s = 100, label='Group 2') # scatter plot with red dots
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.title('Study Hours vs Test Scores')
plt.legend()
plt.show()