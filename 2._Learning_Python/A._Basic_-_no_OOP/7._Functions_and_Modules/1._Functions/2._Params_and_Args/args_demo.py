# Declaration
x, y, z = 1, 2, 3
p, q, r = (1, 2, 3)


# In function definition
def f(*a):
    print(a[0])


f([1, 2, 3], [2])


# In function calls
def g(a, b):
    print(a + b)

g(*[1,2])

