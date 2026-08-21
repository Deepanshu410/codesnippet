import matplotlib.pyplot as plt
import numpy as np

# pie charts = Circular chart divided into slices to show percentages of the total. Good for visualizing distribution of categorical data.
categories = np.array(['Freshmen', 'Sophomore', 'Junior', 'Senior'])
values = np.array([300, 250, 200, 150])
color = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # Custom colors for the pie chart slices
explode = (0.1, 0, 0, 0) # explode the first slice
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=color, explode=[0, 0, 0, 0.1], shadow=True, startangle=90) # autopct='%1.1f%%', meaning auto percentage, adds percentage labels to each slice of the pie chart
plt.title('Pie Chart (Yearly Enrollment)')
plt.show()