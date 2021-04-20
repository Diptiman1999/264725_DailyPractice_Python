# def func(x):
#     try:
#         if x<0:
#             raise Exception("Less than 0")
#     except x:
#         print(x)
#
# func(-10)

def func(x):
    assert x>0,"less than 0"
    print(x)

func(-10)