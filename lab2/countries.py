# 1. Make a program that lists the countries in the set below using a while loop.

clist = ["Canada","USA","Mexico"]

list_len = len(clist)
x = list_len

while x > 0:
    print(clist[x-1])
    x = x-1