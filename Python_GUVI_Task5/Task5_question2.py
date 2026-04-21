from functools import reduce
def mul(x,y):
    return x*y

numbers = [5,2,6,5]
result = reduce(lambda x,y: x*y,numbers)
print("product: ",result)