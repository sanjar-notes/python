'''
while loop is like for except that we need to control the iterator
0. They are used when we don't know how many times we need to iterate
1. We have to initialize the iterator
2. We have to update, until the condition becomes false
3. There are times when the while loop has condition of True but has a break inside
4. Else can be used here too
'''

import random
highest = 10
for i in range(10):
    print(random.randint(0, highest))
