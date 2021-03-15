def f__f():
    print(str(__file__.split('/')[-1][:-3]) + ' running as ', end='')
    if __name__ == "__main__":
        print('script')
    else:
        print('module')


f__f()
