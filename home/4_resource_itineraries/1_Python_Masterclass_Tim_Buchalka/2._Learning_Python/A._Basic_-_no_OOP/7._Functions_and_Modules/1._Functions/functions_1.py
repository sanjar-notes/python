def f_args(a, b, c=2):   # or as f_kwargs
    print(a, b)

# f_args(1, 2)     # OK: order is important if not providing keywords
# f_args(1)        # Error: number of args = number of params
# f_args(1,2,3)    # Error: number of args = number of params
# f_args(b=3, a=2) # OK: as they are kwargs

# def f_args(a=2, b, c) is an error: Keyword argument at the end.

# ----------------------------------------

def f_star_args(*args):
    for i in args:
        print(i, end=' ')

# f_star_args(1)          # OK
# f_star_args([1,2,3])    # OK, but: Not treated AS the args list, treated as an individual arg
# ----------------------------------------

def f_star_kwargs(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])

# f_star_kwargs(a=1, b=2, c=3)  # Ok: Catches the name of keywords awa values
# f_star_kwargs(1)  # Error: Does not take positional arguments
# ----------------------------------------

def f_args_star_args(**kwargs):
    # print(a)
    print(kwargs)

# f_args_star_args(b=2, a=1)  # order unimportant
# f_args_star_args(a=1, a=2)  # error

