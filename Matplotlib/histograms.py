import matplotlib.pyplot as plt
import numpy as np

# histogram = a visual representation of the distribution of quantitative data. They group value into bins (intervals) and count how many values fall into each bin. Great for statistics and probablity.

scores = np.random.normal(loc=80, scale=10, size=100) # normal for normal distribution, 80 is mean, 10 is standard deviation, 100 is number of data points
scores = np.clip(scores, 0, 100) # clip to limit values between 0 and 100
plt.hist(scores, bins=20, color='silver', alpha=0.7, edgecolor='black') # hist for histogram, bins for number of bins, color for color of bars, alpha for transparency
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.title('Exam Scores Distribution')
plt.show()