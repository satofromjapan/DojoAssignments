#
# print out:
# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python
#

bio = {"name": "Masato", "age": "31", "country": "United States", "fav_lang": "Python"}

def bio_creator(bio):
    print "My name is", bio["name"]
    print "My age is", bio["age"]
    print "My country of birth is", bio["country"]
    print "My favorite language is", bio["fav_lang"]

bio_creator(bio)

# print bio

# print bio["name"]
# print bio["age"]
# print bio["country"]
# print bio["fav_lang"]
