lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [alice, lloyd, tyler]

# Add your function below!
def average(numbers):
  total = 0
  total = float(total + sum(numbers))/len(numbers)
  return total  

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])

  total = (homework*.1) + (quizzes*.3) + (tests*.6)
  return total

def get_letter_grade(score):

  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60: 
    return "D"
  else :
    return "F" 

def get_letter_grade_for_student(student):
  score = int(get_average(student))
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60: 
    return "D"
  else :
    return "F" 

def get_class_average(class_list):
  totalofaverages = 0
  result = 0
  for item in class_list:
    totalofaverages += get_average(item)
  result = (totalofaverages/len(class_list))
  return result

print ("Lloyd's letter grade is: %s" % get_letter_grade(get_average(lloyd)))
print ("Lloyd's average is: %s" % get_average(lloyd))
print ("The class average is: %s" %get_class_average(students))
print ("The class letter grade for the class average is: %s" %get_letter_grade(get_class_average(students)))