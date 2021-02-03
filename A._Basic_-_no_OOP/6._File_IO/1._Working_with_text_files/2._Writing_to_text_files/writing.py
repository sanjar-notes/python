with open('in', 'a') as f:
    tb = 2
    for i in range(1, 13):
        print('{0:>2} times {1} is {2}'.format(i, tb, i * tb), file=f)
    print('-' * 40, file=f)
