def fun_1(a, b):
    a = 5
    b = 6
    return a, b

def fun_2(x, z):
    n = fun_1(x)
    
    return n

s = None
d = None

c = fun_1(s, d)
print(type(c))
print(c[1])

# fun_2()