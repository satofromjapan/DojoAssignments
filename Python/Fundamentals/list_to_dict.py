name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) >= len(arr2):
        key = arr1
        val = arr2
    else:
        key = arr2
        val = arr1
    for i in range(len(key)):
        new_dict[key[i]] = val[i]
    return new_dict

result = make_dict(name, favorite_animal)
print result
