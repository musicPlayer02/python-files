# Tuples are immutable. Means they cant be modified once created. While lists and dicts can be modified.
names = ("raj", "bindu", "shivani", "matt", "bindu","pat")
print(names[2])

# count() returns number of times an item occurs in tuple
print(names.count("bindu"))

# index() returns first occurence
print(names.index("bindu"))
