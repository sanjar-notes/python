'''
1. Naming same as C++, i.e first letter is _ or letter, rest anything from a-zA-Z0-0_
2. A nice way to refer to memory locations and store data.
3. Operators +, -, *, /, //(returns quotient), % returns remainder, ** is the exponent
4. BODMAS is followed for precedence
5. Associativity of +, -, *, / is LR, for = it is R
6. Use parenthesis freely
'''
'''
Strings Basics:
    1. An immutable character array(coz lists are mutable)
    2. Access a single letter parrot[i],
        a. Here we can access i th from left, by giving i>=0
        b. By giving negative i, we can access characters from R->L e.g parrot[-1]
    3. Splice
        a. parrot[a:b]// starting from a to b (excluding), a and b could be negative
        (If omitted a is 0 and b = end of string)
    4. Remember we cannot go around the string or R->L, coz that is not a string.
    5. We can also give ith from here, i.e parrot[a:b:ith] - prints from a to b, printing every ith character from a. Jump = ith -1
    e.g x = "1, 2, 3, 4", print(x[0::3]) = 1234
    6. + operator concatenates strings
    7. * operators concatenates string i times, where i is an integer
    8. We can do print(str1, str2, int 1, int 2) - i.e it's a variadic function
    9. Operator precedence still applies, i.e print("p"*5+4) results in an error

    10. Searching for substring: 'in' operator
        "day" in "Monday, return true.
'''
