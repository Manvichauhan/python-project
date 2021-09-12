num = int(input("Print sum of even numbers till : "))

total = 0

for i in range(1, num + 1):

    # Check for even or not.
    if((i % 2) == 0):
        total = total + i

print("\nSum of even numbers from 1 to", num, "is :", total)
