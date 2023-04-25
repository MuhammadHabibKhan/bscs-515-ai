# recursive solution to tower of hanoi problem

def hanoi(dicsNumber, startRod, endRod, midRod):
    if dicsNumber > 0:
        hanoi(dicsNumber-1, startRod, midRod, endRod)
        print("Shift Disk", dicsNumber, "from rod", startRod, "to rod", endRod)
        hanoi(dicsNumber-1, midRod, endRod, startRod)

# main
hanoi(3, 'A', 'C', 'B')