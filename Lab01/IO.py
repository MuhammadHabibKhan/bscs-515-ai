# program to swap numbers

def swap_numbers(a,b,c,d):
    print("Before Swap:")
    print("a = " + str(a) + " | b = " + str(b) + " | c = " + str(c) + " | d = " + str(d))

    a,d = d,a
    b,c = c,b

    print("After Swap:")
    print("a = " + str(a) + " | b = " + str(b) + " | c = " + str(c) + " | d = " + str(d))

swap_numbers(2,56,78,9)