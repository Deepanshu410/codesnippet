import matplotlib.pyplot as plt
import numpy as np

# bar charts = used to compare categories of data by representing each category with a bar. The height of the bar corresponds to the value of the category.
categories = np.array(['Grains', 'Fruit', 'Vegetables', 'Protein', 'Dairy', 'Sweets'])
values = np.array([4, 3, 5, 2, 4, 1])

plt.bar(categories, values, color='lightcoral') # normal vertical bar chartt
# plt.barh(categories, values, color='skyblue') # horizontal bar chart
plt.xlabel('Food Groups')
plt.ylabel('Quantity')
plt.title('Bar Chart (Daily Consumption)')
plt.show()