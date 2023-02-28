# II. a Python program to find if a given string starts with a given character using Lambda. 

s = input("Enter string: ")
st_match = lambda ip: print("Matched!") if s[0] == ip else print("Not matched")

st_match('H')