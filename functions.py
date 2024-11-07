# arbitrary number of arguments
def my_func(**cars):
  print("my fav car is "  +cars["car2"])
my_func(car1 = "benz", car2 = "audi")

# default parameter
def my_func(name = "raj"):
  print("my name is "+ name)
my_func("preeti")
my_func()

