# repetitions are not allowed. Sets are unordered. They are immutable too, i.e., you can't change value of an element. 
names = {"anu", "manu", "raj", "ashu"}
print(names)

# add() adds an element to the set. If item already exists, it doesn't add.
names.add("yash")
print(names)
names.add("raj")
print(names)

# copy() copies the set
set2 = names.copy()
print(set2)

# difference() method returns a set that contains the items that exist only in the first set, not in both sets.
names2 = {"raj","sanvi","bala","manu"}
names.difference(names2)
print(names)

# difference_update() method removes the items that exist in both sets.
names.difference_update(names2)
print(names)

# discard() r3moves specific item
names.discard("raj")
print(names)

# intersection() returns a set that contains similarity between two or more sets.
names = {"anu", "manu", "raj", "ashu"}
print(names.intersection(names2))

# intersection_update() removes items that that is not present in all sets.
names = {"anu", "manu", "raj", "ashu"}
names2 = {"raj","sanvi","bala","manu"}
names.intersection_update(names2)
print(names)

# isdisjoint() returns true if no intersection. false if there is intersection.
names = {"anu", "manu", "raj", "ashu"}
names2 = {"raj","sanvi","bala","manu"}
names3 = {"akhil"}
print(names.isdisjoint(names2))
print(names.isdisjoint(names3))

# issubset() returns true if all items in the set exists in the specified set, otherwise false.
x = {"a","b","c"}
y = {"a","b","c","d","e"}
z = {"a","c"}
print(x.issubset(y))
print(x.issubset(z))

# issuperset() returns true if the set is superset of specified set.
print(x.issuperset(y))
print(y.issuperset(z))

# pop() removes a random item from set
print(y.pop())

# remove() deletes a specified element
x.remove("a")
print(x)

# union() returns a set containing union of all sets
print(x.union(y))

# update() adds items from specified set to current set.
x.update(y)
print(x)

# clear() clears all elements from set
names.clear()
print(names)