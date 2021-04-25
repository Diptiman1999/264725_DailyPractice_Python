class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
s=Spam()
s.print_egg()
print(s._Spam__egg)#7

# If it was simple egg then it could be accessible but if it is_egg it can be accessible inside the same module not any
# other module that is accessing it. If it is __egg then it will not be accessible from anywhere directly.
# For that you need to create a function like get attribute or can use it using ._Classname__variablename