'''
Python is indented and does not use delimiters like ;
Blocks statements have the same indentation, continually.

-----------------------------------------------------

if elif else;

elif and else are optional

e.g

if condition1:
    pass
elif condition2:
    pass
else
    pass

-----------------------------------------------------

Logical Operators
1. and (logical AND i.e conjunction)
2. or (logical OR or disjunction)
3. not (logical NOT or inverse) - can be used as not of whole or not in
4. Chaining of logical operators is allowed - joined by AND :)
5. True and False are bool constants, None is convertible to 0
6. 0, 0.0, 0j, "", (), {}, [], None are equivalent to False, anything else is True
7. ShortCircuiting exists for AND and OR

-------------------------------------------------------

in keyword(operator): Check for membership
'''
'''
Loops:
A. For loop
    the for loop is does the job of for and for each as in C/C++, uses range(integer a, integer b, intger step) used to iterate over objects number range
    same as i = a; i < b; i++

    a = 0, step = 1 is the default value

    * Can be used to iterate over a container

    2. continue, goes to th next iteration without executing anything after continue
    3. break, terminates the innermost rule in which it is present.
    4. else used in for - executes only if loop does not break - i.e executes for normal loop only
    e.g
        for i in range(10):
                a = i
        else
            print("Loop Ran Okay")
        ELSE is very useful - I'm going to use it
B. while - standard
C. do while - standard
D. Python3 has no switch statements
-----------------------------------------------------
'''
