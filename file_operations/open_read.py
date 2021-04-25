file=open("text.txt",'r')
cont=file.read(4)
print(cont)
print(type(cont))
print("Length of file :",len(cont))

file.close()