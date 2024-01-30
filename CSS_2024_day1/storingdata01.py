# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:51:49 2024

@author: vmbay
"""

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 = 25
B11 = 39

print(B1)
print(B2)
print(B3)
print(B4)
print(B5)
print(B6)
print(B7)
print(B8)
print(B9)
print(B10)
print(B11)

# Using List

age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])
print(age[11])

# Basic Sats
age = [30,40,30,49,22,35,22,46,29,25,39]
print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

# Storing Text
C2 = M
C3 = M
C4 = F
# But wait! Its giving us an error name 'M' is not defined Why is that? 
# Any letters, words, group of words fall under the category of a string data type.
# Therefore we need to add " to the beginning and end

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

# We can do many things with lists:
# Data Storage With Lists

# print all the items in the list using [:]
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

# we can add items to the end of the list using append()
my_list.append("pi")
print(my_list)

# add items at specific positions using insert()
my_list.insert(1,"pi2")
print(my_list)

# remove an item from the list using the remove() function
my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")

# check how many variables are in the list using the len()
print(my_list)
print(len(my_list))

# print a range of values using [start:end] – just like in excel!
# View a certain range of items:
print(my_list)
print(my_list[0:3])
