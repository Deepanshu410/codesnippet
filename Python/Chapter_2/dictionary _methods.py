
#dictionary methods
a = {
    "name": "Dj",
    "from": "India",
    "marks": [93,23,34]
}
print(a)
# a = a.items() # --> the whole dict values
# print(a)

# python will only print the first value of a variable  only one value method can be used at a time
# but to run multiple methods we do, print(vairable.method()) which is done from update method
# a = a.keys()   # --> the value of a variable in the dict
# print(a)

# updatea = {
#     "from": "Mars"
# }
# a.update(updatea)
# print(a)

# print(a.get("name"))

# print(a.values()) # return with dict_values
# print(list(a.values())) # return with only the values of the dict

# print(a.clear())
# print(a.copy())
# print(a.fromkeys(a))  # --> only keys(variable) of the dict

# print(a.pop("marks")) # --> remove that particular variable only, excluding his key
# print(a)

# print(a.popitem())   #--> removes last last whole item
# print(a)

print(a.setdefault("name", "NAME"))
print(a)