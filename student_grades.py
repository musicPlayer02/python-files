student_scores = {
  "mark": 81,
  "mansi": 78,
  "suresh": 99,
  "ganesh": 74,
  "mahesh":62,
}

""" scores 91-100 = A, 81-90 = B, 71-80 = C, less than equal to 70 = F"""

student_grades = {}

for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "A"
  elif student_scores[student] > 80:
    student_grades[student] = "B"
  elif student_scores[student] > 70:
    student_grades[student] = "C"
  else:
    student_grades[student] = "F"


print(student_scores)
print(student_grades)