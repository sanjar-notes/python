'''
Dictionaries and sets - Both are unordered and no duplication is allowed.
    1. Index is meaningless for both, but dictionaries have a index like thing called key.
    2. Dictionaries - collection of key value pairs
    3. Both set and keys can have different type of objects
        dti = {2: "sanjar", "ahmar": 23, "sanjar":[4,5]} is okay
        dti = {1, 2, 3, "sanjar"} is okay too.
        We can store other objects or even dictionaries.
    4. RESTRICTION: Key cannot be a mutable object(e.g list), like a list. We can use it as a value though.
    5. We can pass duplicate key value pairs in the definition - there are no errors.
    6. Dict and set both are completely random(only during creation) - even for the same input.
    7. Adding to the dict: p[key] = value, it is added if it does not exists. Just like C++.
    8. Adding to the set .add(value)
    9. del(dict) - We can delete the whole dictionary using del(dict_name).
    10. 'in' - keyword. py2 had a has_key() function

    Part 2 <------------------------->

    11. dict.clear() clears the whole, i.e removes all kv pairs of the dictionary.
    12. Acccess is just dict_name[key] or dict_name.get(key)
    13. .get(key) - If a key is absent, we get an error when we do dictname[key], better use .get(key) as it returns None.
    14. .keys() returns the view list of keys - it is a view object, i.e returns a reference, like a list.
    15. We can print the dict in order, by sorting the key list and access the dict using these keys.
        for key in sorted(fruits.keys()):
            print(fruits[key]) # O(n) rather than O(nlogn)
    16. .values() returns the list of all values
    17. .pop(key i.e index, defaultReturnValue) for deleting a key value pair, using name. Error if the key does not exist.
    18. .popitem() used to remove the last element from dict
    18. treat dict_name as a list of keys.

    Part 3 <------------------------->

    19. .keys() and .values() return view object references.
    20. .items() to return the list of key, value pairs, tupleated
    21. Going reverse, we can create a dict using a list of 2-tuples.

'''

fruits = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "round and crunchy fruit",
    "grapes": "Grapes are good for health",
    "oango": 2
}

x = "abcd"
y = x
y += 'b'
print(x, y)
