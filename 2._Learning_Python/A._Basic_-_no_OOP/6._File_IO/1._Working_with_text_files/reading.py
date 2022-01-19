with open('in.txt', 'r') as f:
    print(f.read(), end='')
    f = open('in.txt', 'r')
    print(''.join(f.readlines()))
    f.close()
