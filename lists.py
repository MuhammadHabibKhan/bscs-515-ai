# Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2. 

list = ['abc', 'xyz', 'aba', '1221']
count = 0

for x in list:
    string_length = len(x)
    
    if string_length > 2:
        if x[0] == x[string_length-1]:
            count = count + 1

print(count)