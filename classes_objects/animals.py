class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color = color

class Dog(Animal):
    def bark(self):
        print("Woff!!")
class Cat(Animal):
    def meow(self):
        print("Meow")

fido=Dog("Bruno","Black")
print("Color of Dog is ",fido.color)
fido.bark()

cat=Cat("Mnm","White")
print("Color of cat is ",cat.color)
cat.meow()