""" Ig you need to create a global variable, but you are stuck in the local scope, 
you can use the global keyword. It will make the variable global."""

def myfunc():
  global x
  x=300
  
myfunc()
print(x)  


""" Also, use the global keyword ifyou want to make a change to a global variable inside a function."""

x = 300 
def myfunc():
  global x
  x = 200
myfunc()
print(x)