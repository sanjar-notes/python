import shelve

# make a normal dict to a persistent dictionary
books = {
    "recipes": {
        "blt": ["bacon", "lettuce", "tomato", "bread"],
        "beans_on_toast": ["beans", "breads"],
        "scrambled_eggs": ["eggs", "butter", "milk"],
        "soup": ["tin of soup"],
        "pasta": ["pasta", "cheese"]
    },
    "maintainance": {
        "struck": ["oil"],
        "loose": ["gaffer tape"]
    }
}
# print(books['recipes']['blt'])
with shelve.open('books') as db:
    lis = list(db.keys())
    print(lis)

'''
NI - keys(VO), values(VO), items(VO), editing values(RBV)
I - access of values, replacing values
'''
