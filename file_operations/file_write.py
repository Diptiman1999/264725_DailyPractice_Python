file=open("newline.txt","w")
file.write("Is it working?\nIf yes then Ok\nOtherwise we need to check--")
file.close()

file=open("newline.txt",'r')
print(file.read())
file.close()
