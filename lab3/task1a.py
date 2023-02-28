# I. a Python program to square and cube every number in a given list of integers using Lambda. 

list_numbers = [1,2,3,4,5,6,7,8,9,10]

sq = lambda x: x*x
cube = lambda y: y*y*y

for n in list_numbers:
    print("Square of " + str(n) + " is: " + str(sq(n)))
    print("Cube of " + str(n) + " is: " + str(cube(n)))
    print()