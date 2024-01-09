#!/usr/bin/env python
# coding: utf-8

# # Importing Iibraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load the dataset

# In[2]:


data = pd.read_csv('world_nuclear_power_dataset.csv')


# # Display the first few rows of the dataset

# In[3]:


print(data.head())


# # Summary statistics

# In[4]:


print(data.describe())


# # Check for missing values

# In[5]:


print(data.isnull().sum())


# # Check data types

# In[6]:


print(data.dtypes)


# # Visualization 1: Distribution of Power Plant Capacity

# In[7]:


plt.figure(figsize=(10, 6))
sns.histplot(data['Capacity_MW'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Power Plant Capacity')
plt.xlabel('Capacity (MW)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# # Visualization 2: Power Plant Status Count

# In[8]:


plt.figure(figsize=(8, 6))
status_count = data['Status'].value_counts()
sns.barplot(x=status_count.index, y=status_count.values, palette='viridis')
plt.title('Power Plant Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# # DASHBOARD-WORLD NUCLEAR POWER

# In[14]:


# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.patch.set_facecolor('lightgrey')  # Set background color

# Visualization 1: Bar plot
sns.countplot(x='Status', data=data, ax=axs[0, 0], palette='muted')
axs[0, 0].set_title('Power Plant Status')

# Visualization 2: Pie plot with color strip legend
status_counts = data['Status'].value_counts()
axs[0, 1].pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('muted'))
axs[0, 1].legend(bbox_to_anchor=(1, 1), loc='upper left', labels=status_counts.index)
axs[0, 1].set_title('Status Distribution')

# Visualization 3: Histogram plot
sns.histplot(data['Capacity_MW'], bins=20, kde=True, ax=axs[1, 0], color='skyblue')
axs[1, 0].set_title('Distribution of Power Plant Capacity')
axs[1, 0].set_xlabel('Capacity (MW)')
axs[1, 0].set_ylabel('Frequency')

# Visualization 4: Line plot (example using random data)
import numpy as np
years = np.arange(2000, 2020)
random_values = np.random.randint(100, 1000, size=len(years))
axs[1, 1].plot(years, random_values, marker='o', linestyle='-', color='green')
axs[1, 1].set_title('Random Line Plot')
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Random Values')

# Adjust layout
plt.tight_layout()
# Save the dashboard as an image
plt.savefig('2324VS0013_sravan.png', dpi=300)  # Change the file format and DPI as needed


# Show the dashboard
plt.show()


# In[ ]:




