'''
These are very important
We know about the 'string'. Add these

1. sep.join(iterable of strings) -> a string : joins the list/set/dict into a string seperated by sep, solves terminating comma-like problems.
2. string_name.split(sep) -> a list = splits a given string which has a seperator - useful for TSV, CSV
3. string.strip() -> a string - removes the ending characters maximally w.r.t to the given string, until a unknown character is encountered

-------------


The remaining are:
1. Lists
2. Ranges
3. Tuples

These are linear

There are three more binary sequence types - sets, dictionaries and multimaps

-------------
Lists -  They are a sequence of things(homo and hetero both are allowed)
List functions:

list() - constructor
m.count(key)
m.min()
m.max()
m.sort()
m.index(key) - returns the first occurrence in the list
m.append(new_element)
m = m1+m2, concatenation is allowed

m.sort() just like C++, returns None -  works on the object on which it is called.
m.sort(reverse = True)
sorted(m) returns the object.

lists with different order are different == is overloaded and can compare the two.

----------------

We have iterators for all the sequence types:
1. For DS's, shallow copy is done when we do assignment - Pointing to the same list
2. For deep copy do y = list(x)
3. For param initialization - we do y = [v1, v2, v3...]
4. list() constructor:
   a. list() returns []
   b. for strings, set, tuples and range: Creates a list of elements.
        list("Here") = ['H', 'e', 'r', 'e'] - iterates over the characters
   c. For dictionary
        1. If not specified ~ same as list(dictio.keys())
        2. For values: list(dictio.values())
        3. For key-value tuples: list(ditcio.values())
----------------

Iterators:
1. iter(data_structure) returns the iterator(front to back)
2. next(iterator_variable) does dereferencing and increases the iterator by one, i.e *(p++)
3. after the last elements iterator, we get an error

string = "123456789"

for char in string:
    print(char, end='')

for char in iter(string):
    print(char)

---

listt = ["sanjar", "maryam", 1, 2, 5, "ahmar", 7]

my_iterator = iter(listt)

# for i in range(len(listt)):
#     print(next(my_iterator))

# same as
for i in listt:
    print(i)

----------------------

Range:
1. It is a bulit in type in python3, so it may be stored in a variable.
2. range(n) is the same as range(0, n, 1)
3. In range(a, b, c), we see start is a, end is b and step forward is c
    a, b and c should be in harmony, i.e we can have a negative step only if a < b, this won't return an error though
        a. Use case:
            for i in range(100, 0, -1):
                print(i)
            # prints from 100 to 1(not including 0)
4. In range(2, 10, 1)
5. list, taking in range() creates a list of the integer from start to end
6. Range is independent of memory, i.e range(10) and range(1000000) use the same memory - beacuse it is only a representation(pretty POWERFUL)
7. xrange in py2 are the same range in py3
8. ranges can be used get a value without running a loop, because [] is overloaded, i.e range(1, 155, 2)[3] will return 7
9. range(0, 10)[i] returns the ith letter in range - very intuitive
    a. Used to get all the numbers divisible by x
    b. Used to count the number of
    c. len(range(a, b)) is defined - returns 0 for invalid a, b
    d. Used in loops which increase by more than one, standard for loop
        for i in range(0, 100, 5):
            print(i)
10. Sliced ranges are allowed too - range(0, 100)[::2]
    print(len(range(0, 100)[::2])) SAME AS print(len(range(0, 100, 2)))
11. Range never create a list in memory
12. We can go backwards too, range(b, a, -c) where b > a and c > 0
13. Negative slice is extremely useful as it starts to travel backwards
        backstring = "edoC 3 nohtyP evol I"
            print(backstring[::-1])
        Usable with ranges too
        Very powerful language - don't go the C++ way here.
Index:
1. Same as C++
2.
'''
