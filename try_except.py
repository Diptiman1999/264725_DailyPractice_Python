try:
    num1=int(input())
    print(num1/0)
except ZeroDivisionError:
    print("Divisible by 0")
finally:
    print("Oh God! Atleast the code executed")
