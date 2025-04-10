#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import matplotlib.pyplot as plt
from statistics import mean

csv_file = 'vv.csv'
column_name = 'proper time (micro)'
values = []


# Step 1: Read the column values
with open(csv_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Convert to float (or int, depending on the data)
            value = float(row[column_name])
            values.append(value)
        except ValueError:
            continue  # Skip rows with invalid/missing data

# Step 2: Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(values, bins=50, edgecolor='black')  # Adjust `bins` as needed
plt.xlabel('proper_time(micro)')
plt.ylabel('Count')
plt.title('Histogram of proper_time(micro)')
plt.grid(True)
plt.tight_layout()
plt.show()


mean_value = mean(values)
print(f"Mean of '{column_name}' = {mean_value:.2f}")


# In[9]:


import numpy as np
import scipy.optimize as opt

# Define the exponential function for fitting
def exponential_fit(x, a, b):
    return a * np.exp(b * x)

# Step 3: Perform exponential fit
# Use histogram data to fit the exponential function
count, bins, _ = plt.hist(values, bins=50, edgecolor='black', alpha=0.6)  # Plot histogram and get bin data
plt.clf()  # Clear the previous plot to avoid overlap

# Calculate bin centers
bin_centers = 0.5 * (bins[1:] + bins[:-1])

# Fit the exponential curve to the histogram
params, covariance = opt.curve_fit(exponential_fit, bin_centers, count, p0=(max(count), -0.1))

# Get the fit parameters
a, b = params

# Step 4: Plot the histogram with exponential fit curve
plt.figure(figsize=(10, 6))
plt.hist(values, bins=50, edgecolor='black', alpha=0.6, label='Data')
plt.plot(bin_centers, exponential_fit(bin_centers, *params), 'r-', label=f'Exp fit: a={a:.2f}, b={b:.2f}')
plt.xlabel('proper_time(micro)')
plt.ylabel('Count')
plt.title('Histogram of proper_time(micro) with Exponential Fit')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print fit parameters
print(f"Exponential Fit Parameters: a={a:.2f}, b={b:.2f}")


# In[10]:


# After fitting the data
a, b = params

# Construct the exponential equation
equation = f"y = {a:.2f} * exp({b:.2f} * x)"

# Print the equation
print(f"The exponential fit equation is: {equation}")


# In[11]:


# Calculate the mean from the exponential fit
mean_propertime = -1 / b

# Print the mean
print(f"Mean of 'proper_time' from the exponential fit: {mean_propertime:.2f} microseconds")


# In[ ]:




