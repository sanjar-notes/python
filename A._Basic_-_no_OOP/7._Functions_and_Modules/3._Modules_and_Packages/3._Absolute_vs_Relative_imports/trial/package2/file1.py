def f__f():
    print(str(__file__.split('/')[-1][:-3]) + ' running as ', end='')
    if __name__ == "__main__":
        print('script')
    else:
        print('module')
f__f()

# import all modules in the current directory - i.e sibling modules

# from . import *
# import sys, os
# sys.path.append(os.pardir)
# import package2.file2
def f():
    x = 3
    def g():
        y = 4
        print(locals())
    print(locals())
    g()
f()
