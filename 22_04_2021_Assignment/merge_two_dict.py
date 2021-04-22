# Write a program to merge two dictionaries in Python
d1={10:100,20:200,30:300}
d2={'a':"lion",'b':"tiger",'c':"fox"}

# Merging can be done in different ways
d1.update(d2) #This will merge d2 to d1. Here only d1 is changed whereas d2 remains as it is
print(d1)

# Or we can do it using | operator
d1={10:100,20:200,30:300}
d2={'a':"lion",'b':"tiger",'c':"fox"}
d3=d1|d2
print(d3)