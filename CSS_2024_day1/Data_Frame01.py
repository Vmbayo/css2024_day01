# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:49:28 2024

@author: vmbay
"""

# When dealing with tabular data or datasets, the Pandas library provides a powerful and versatile data structure called a DataFrame.
# A DataFrame is a 2D,labeled data structure with columns that can be of different types,similar to a spreadsheet or SQL table.

# Let's convert the previous lists into a Pandas DataFrame to demonstrate its advantages over lists and dictionaries:
    
import pandas as pd

# Creating a DataFrame
data = {'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

# Advantages of using Pandas DataFrame over lists and dictionaries:

# 1: Conciseness - Storing and accessing data in a DataFrame is concise and easy to read.

# 2: Column-Based Access: Accessing columns in a DataFrame is straightforward and intuitive.

# Accessing specific columns
print(df['age'])
print(df['gender'])

# 3: Descriptive Statistics:
# Pandas provides built-in functions for basic statistics on columns.

# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering and Slicing:cSelecting and filtering data based on conditions is simplified.

# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

# Flexibility:
# DataFrame allows easy addition or removal of columns.

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)
