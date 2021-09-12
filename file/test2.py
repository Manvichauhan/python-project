def func(n):
    if(n > 100):
     return n-5
    return func(func(n+11));
print(func(45))