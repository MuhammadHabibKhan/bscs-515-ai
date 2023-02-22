def workerEfficiency():
    time_taken = input("Enter time taken in hours: ")
    time_taken = int(time_taken)
    
    if (time_taken >= 2 and time_taken <= 3):
        print("You are a highly efficient worker!")
    elif (time_taken > 3 and time_taken <= 4):
        print("You need to improve your speed mate!")
    elif (time_taken > 4 and time_taken <= 5):
        print("We will give you training to improve your speed!")
    elif (time_taken > 5):
        print("Unfortunately, you have to leave the company")

workerEfficiency()