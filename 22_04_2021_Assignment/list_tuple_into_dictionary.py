# Write a Python program to convert a list of tuples into a dictionary
t=[("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]

# First My way
d1={}
for a,b in t:
    d1[a]=b
print(d1)

# predefined dict() method in dictionaries
d2={}
d2=dict(t)
print(d2)

# predefined setdefault(key,value) in dictionaries
d3={}
for a,b in t:
    d3.setdefault(a,b)
print(d3)