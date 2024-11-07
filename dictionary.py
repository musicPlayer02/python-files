mobile = {"brand":"apple","model":15,"price":60}

print(mobile["model"])
mobile["model"] = 16
mobile["wifi"] = "on"

# items() method returns a view object. It contains key-value pairs as tuples in a list.
print(mobile.items())

# keys() method returns a view object. it contains keys as a list.
print(mobile.keys())

# values() method returns a view object. It contains values as a list.
print(mobile.values())

# pop() removes specified element from dictionary
mobile.pop("wifi")
print(mobile)

# popitem() removes last item from dictionary
mobile.popitem()
print(mobile)

# copy() returns a copy of dict
mobile2 = mobile.copy()
print(mobile2)

# get() returns value of an item with a specified key
print(mobile.get("brand"))

# setdefault() returns of the item with specified key. If the key doesn't exist, inserts the key with specified value.
x = mobile.setdefault("price")
print(x)
print(mobile)
mobile.setdefault("price", 95) # 95 will only be updated if price was already not in the dict
mobile.setdefault("wifi","on")
print(mobile)

# update() inserts specified item to dict. It can be another dict or any iterable object with key value pairs.
mobile.update({"color": "black"})
print(mobile)
mobile.update({"dims": (78,74,4)})
print(mobile)

# fromkeys() method returns a dict with the specified keys and specified values
x = {"key1","key2"}
y = 0
w = 10
z = {1,2}
this_dict = dict.fromkeys(x,y)
print(this_dict)
print(dict.fromkeys(x,z))

# clear() removes all elements from a dictionary
mobile.clear()
print(mobile)