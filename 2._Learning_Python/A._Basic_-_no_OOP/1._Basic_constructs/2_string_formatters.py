'''
String formatting
    1. Using str(), to convert a data type using + and strings, we should use str()
    2. We can avoid +, by simply using print(var1, var2, sep = "")
    3. We can write a paragraph(string) and describe it in different lines by using triple quotes, instead of single quotes
        Note: Don't have 4 quotes in a row. i.e """abc"d" """
        Use point 3 to avoid /'s as """ or single doesn't have any problems with using " inside as many times as we wish.
    4. We can get input like cin, actually better using input.split(), this returns a list of strings of the inputs, Enter <- is the end.
        e.g input().split(), 1 2 3, returns ['1', '2', '3']
'''
'''
String Replacement Fields
    0. Use {} for % and write the args in .format() - number of args greater than or equal to {()}
    1.use {k} for a replacefield where k represents the position of the variable in the format()

        >>> print("I am a {0}".format("Boy", "Girl"))
        I am a Boy

        if we don't use k, python assumes k from 0 to last - It works with classes too, i.e {.field} is OK.
    2. We can have multiple and duplicate replacement fields, they may be out of order as well.
    3. For floating point numbers
        e.g print("{0:a.b}".format(22/7))
        a = total length(both fract as well as non fract) including the '.' (optional)
        b = fract length (after the .)
    4. For allocating space for print, do {k:length} or {:length} - Note that except for decimals, nothing will be truncated if k is small.
    5. For left and right justification, write {i:<length} for left aligned. They are left aligned by default. Or use > length.
    6. For printing something in the empty space, use {i:<0len}, this will print 000000String. Using left/right justification symbol is very important here.
    7. For printing a number in binary, hex or hexadecimal, we just write {0:b} or {0:o} or {0:x}
    8. We can use formatters inside one another too
    9. We can use [] or . notation inside a {}
        e.g '{[2]}'.format([1,2,3]) # -> '3'
        e.g '{.name}.format(object) # -> 'object.name_value'
    Basically, we can write {index: filler(opt) alignment(opt) length number_system(opt) .after_decimal_length f(opt)} :FJLNF
        MAID length has two on both sides - everything is optional
        Left - filler and justification
        Right - length and (number_system or decimal_f)(e.g .2f does not count .)
    e.g print("{0:>06b}".format(9)) is 001001
    e.g print("{0:>06.2f}".format(22 / 7)) is 0003.1
        Don't use binary and decimal at the same time
    The length will always be equal to the most significant digit
    *) number and decimal cannot be used together
'''
'''
    Formatting Operator(obsolete) %
    1.
    age = 10
    print("I am a %i "%(age))

    THIS HAS NO FLEXIBILITY AS COMPARED TO PYTHON3 - only one Left to right
    It is actually used to handle formatting and not replacement

    Correct use of formatting operator

    1. print("Age %3d", age) - allocates space for characters if they don't have it.
        a. If age is less than 3 digits, we have spaces before the number, as if they were 0's.
        b. If the age is 3 digits or more, we have the age fully printed, no spaces or anything.

        This used for table formatting.
    2. For precision of floats write print("%a.bf", volume), here a is the letters in the whole part, b is the number of digits in the fractional part
'''

print('{0:.2f}'.format(123.234))
