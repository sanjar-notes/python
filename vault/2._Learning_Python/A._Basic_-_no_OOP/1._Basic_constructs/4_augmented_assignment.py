'''
-------------------------------------------------------------------------------------------------------------------------
Assignment:
1. For string, int, bool, float - by value
2. ANything else - assigns reference

Note: use keyword 'is' to check reference, == does bit by bit comparison

-------------------------------------------------------------------------------------------------------------------------
Augmented Assignment:
    1. +, *, =, %, //, **
    2. In C/C++ and Java, both assignments are same. But python creates a buffer variable if we use long hand assignment.
    Augmented is in-place and hence fast
    3. Can be used universally, i.e used for strings too.
    4. Other operators are &=, ^=,|=, <<=, >>= these are Bitwise Ops

-------------------------------------------------------------------------------------------------------------------------

Join Method:
    In Python, when we conactenate strings, Python makes a new to_copy variable and concatenates it, then releases the old one.
    1. This is very inefficient
    2. We also have a problem with the ending ", ".
    3. sepe.join(iterable containing strings) helps here.
        Syntax: concatenated_string_name = ", ".join(list of strings to be concatenated)
        i. We can also pass a single string(rather than a list)
        ii. We can concatenate an existing string by doing string_name+=sepe.join(list string)
        iii. beware of the fact that sepe is not applied between old, first of the list. As it is present after n-1 things, starting from list[0]
            do old += sepe + sepe.join(list)
'''
