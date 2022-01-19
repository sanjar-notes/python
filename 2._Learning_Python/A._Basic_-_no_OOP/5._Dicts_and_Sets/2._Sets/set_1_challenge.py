# WAP that takes some text and returns a list of all characters
# in the text which are not vowels, sorted in alphabetical order.

# You can either enter the text from the keyboard or
# initialize a string variable with the string

# soln get the set and subtract the set from the vowels set
# text = set(input().lower())
for i in set(input().upper()) - frozenset('AEIOU'):
    print(i)
