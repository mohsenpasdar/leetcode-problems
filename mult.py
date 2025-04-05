counter = 0
def mult(a, b):
    x = a
    if x == 1:
        return b
    
    if x % 2 == 0:
        res = mult(x // 2 , b)
        return res + res
    else:
        res = mult(x // 2, b)
        return res + res + b
    
print(mult(1515454, 25533))