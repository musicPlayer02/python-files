heights = input("enter heights of students seperated by a space: ").split()
total_height = 0
count = 0
for i in heights:
  count += 1
  total_height += float(i)
average = total_height/count
print(average)

# or
heights = input("enter heights of students seperated by a space: ").split()
for i in range(0,len(heights)):
  heights[i] = int(heights[i])
print(sum(heights)/len(heights))
print(f"maximum height is {max(heights)}")