print("***********for loop********")
students = ["max", "stark", "john", "will"]

print("**** iterating the list *******")
for x in students:
  print(x)
 
print("*******+ iterating an element in list ******+++++") 
for x in students[3]:
  print(x)
  
print("********* example of break *********")
for x in students:
  print(x)
  if x == "john":
    break

print("*******++++ example of continue *********")   
for x in students:
  if x == "john":
    continue
  print(x)

print("******** illustrating range *********")
for x in range(1, 12, 2):
  print(x)

print("*****+ illustrating else in for loop **********+") # the else block won't be executed if for loop is ended by break statement 
for x in range(6):
  print(x)
else:
  print("end")
  
print("******* nested loop *******")
x = [1,2,3]
y = [1,2,3]
for u in x:
  for v in y:
    print(u,v)
 
