# (ii) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']
l = [colors for colors in list if list.index(colors) not in [0,4,5]]
print(l[:3])