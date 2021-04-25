def func(x):
    return x**2

# Using pure function
print(list(map(func,[1,2,3,4,5,6,7,8,9,10])))

# using Lambda function also
print(list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10])))
