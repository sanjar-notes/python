def main():
    try:
        n = int(input('Enter a number: '))
    except ValueError:
        print('Insert proper value')
        main()

    def fact(n):
        if n == 0:
            return 1
        return n * fact(n - 1)
    print('{} != {}'.format(n,fact(n)))
