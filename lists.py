names = ["deepu","manu","anu","sanket","deepu"]
# list accessing
print(names[0])
print(names[-2])

#replacing list item
names[1] = "jonu"
print(names)

#append list
names.append("radha")
print(names)

#copy of a list
names2 = names.copy()
print(names2)

#count frequency of an element in a list
print(names.count("deepu"))
print(names.count("raj"))
print(names.count("jonu"))

#adds specified list elements (or any iterable) to the end of the list
names.extend(("apple","banana"))
fruits = ["grapes","pear"]
names.extend(fruits)
print(names)

# returns position at the first occurence of an element
print(names.index("apple"))
print(names.index("deepu"))

#insert element at a specific position
names.insert(2,"isha")
print(names)

#remove element at the specified position
names.pop(2)
print(names)

#removes first occurence of the element
names.remove("deepu")
print(names)

#reverses the order of the elements
names.reverse()
print(names)

# sorts the elements of list
names.sort()
print(names)

# remove all elements from a list
names.clear()
print(names)