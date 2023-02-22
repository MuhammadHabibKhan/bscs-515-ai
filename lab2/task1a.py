def cubeSize(h, w, d):
    volume = h*w*d

    print("Volume of the given cube is: " + str(volume))
    
    if (volume >= 1 and volume <= 10):
        print("Extra Small")
    elif (volume >= 11 and volume <= 25):
        print("Small")
    elif (volume >= 26 and volume <= 75):
        print("Medium")
    elif (volume >= 76 and volume <= 100):
        print("Large")
    elif (volume >= 101 and volume <= 250):
        print("Extra Large")
    elif (volume > 250):
        print("Extra-Extra Large") 

cubeSize(2,5,6)   