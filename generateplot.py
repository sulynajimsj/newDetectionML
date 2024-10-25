import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('performance_results.csv')

# Generate the boxplot
plt.figure(figsize=(10, 6))
data.boxplot(column='latency', by='test_case')

# Customize the plot
plt.title('API Latency Boxplot')
plt.suptitle('')
plt.xlabel('Test Case')
plt.ylabel('Latency (seconds)')

# Set y-axis limits to focus on the main data range
plt.ylim(0, 0.5)  # Adjust this range based on your data

# Save and show the plot
plt.savefig('latency_boxplot.png')
plt.show()