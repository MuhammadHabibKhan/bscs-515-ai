# 1. Create a loop that counts from 0 to 100
for x in range(101):
    print(x)

# 2. Make a multiplication table using a loop

def mul_table(y):
    for z in range(1,11):
        print("| " + str(y) + " x " + str(z) + " = " + str(y*z) + " |")

mul_table(10)

# 3. Output the numbers 1 to 10 backwards using a loop

for x in range(10,0,-1):
    print(x)

# 4. Create a loop that counts all even numbers to 10

count = 0
for x in range(11):
    if x%2 == 0:
        count += 1
        print(x)
print("Total even no.s: " + str(count))

# 5. Create a loop that sums the numbers from 100 to 200
sum = 0
for t in range(100, 201):
    sum += t
print("Sum: " + str(sum))


