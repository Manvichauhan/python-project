n = int(input("enter the number of stairs:"))
def sum(x):
    if x <= 1: 
        return x
    return sum(x - 1) + sum(x - 2)

def count(n):
    return sum(n + 1)
print("number of ways:", count(n))