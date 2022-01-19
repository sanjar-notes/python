def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            print('{}: {}'.format('spam3', [x for x in locals()]))
            return z

        y = " more spam"
        y+=spam3()
        print('{}: {}'.format('spam2', [x for x in locals()]))
        return y
    x = "spam"
    x += spam2()
    print('{}: {}'.format('spam1', [x for x in locals()]))
    return x
# print(spam1())
# print('{}: {}'.format('spam1', [x for x in locals()]))

# In spam3, locals are: z
# In spam2, locals are: spam3 z y
# In spam1, locals are: spam3 z y x
#


def f():
    def g():
        nonlocal Name
        print(Name)
    Name = 'Tobias'
    g()
f()

