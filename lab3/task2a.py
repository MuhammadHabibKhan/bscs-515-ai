""" I. You have collected information about cities in your province. You decide to store each city
name, population, and mayor in a file. Write a python program to accept the data for a number of cities 
from the keyboard and store the data in a file in the order in which they are entered
"""
def info():
    name = input("Enter City name: ")
    pop = input("Enter Population: ")
    mayor = input("Enter Mayor's name: ")

    return [name, pop, mayor]

def append_info():
    totalCities = input("Enter total number of cities: ")
    with open("city_info.txt", "w") as file:
        for x in range(int(totalCities)):
            info_list = info()
            for x in range(3):
                file.write(info_list[x])
                if x != 2:
                    file.write(" ")
            file.write("\n")

append_info()