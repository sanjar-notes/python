'''
Tuple - An ordered set of data
1. They are immutable, not changeable*.
2. Parenthesis are not necessary, it is there only for avoiding syntactic ambiguity(i.e x=1,2 is the same as x=(1,2s))
3.  t = 'a', 'b', 'c' 3-ary tuple
        print(t)
    We need to make the things good.
4. We can access them like lists using []. But don't try to change em
5. We can mix different data types.
6. We can update tuples by just reassigning them to the tuple with data changed
7. We have equality associativity from Right to Left
8. Tuples are immutable in order to avoid errors(be robust) - philosophy.
9. Tuples are useful for records, not for actively changing data.
10. We can extract values of the tuple(This is called tuple unpacking)
        a. a, b, c = tuple_name # Number of values SHOULD be the same as len(tuple)
        b. We can assign the same values to multiple things
        c. Don't use together on the same line
            e.g a = b, c = 1, 3
            a = (1, 3)
            b = 1
            c = 3
            Not intuitive
11. Tuples can contain anything inside, tuples lists etc, Changing these 'inside' lists is allowed.
    a = (1, [1, 2])
    a[1].append(3) # -> (1 , [1,2,3])
    this is allowed - the tuple stores the data structures's reference only.
    It is useful in many ways.
12. It is useful to make a tuple so that relationships between variables is intuitive.
13. We can print any tuple, so they can be passed as it is to .format()
-------------------------
Binary Number Systems:
    We can specify the number system and the decimal at last(but not together)
    1. Use x for hex, o for oct and b for binary - small letters strictly
    2. For representing in decimal 0b101001, 0xAF24, 0o137
    3. For converting from decimal to other systems do int(str(hex(i))), or bin(i) or oct(i) - All are strings.
'''

