import os
compulsorySubject=["Bangla (First Paper)","Bangla (Second Paper)", "English (First Paper)", "English (Second Paper)","Mathematics", "Information and Communication Technology (ICT)", "Religion Studies"]
scienceSubject = ["Physics", "Chemistry", "Biology","Higher Mathematics"]
commerceSubject = ["Business Entrepreneurship", "Accounting", "Finance and Banking"]
commerceOptional = ["Agricultural Studies" , "Higher Mathematics" , "Economics" ,"Geography" , "Home Science"]
artsSubject = ["Bangladesh and Global Studies","Geography and Environment", "Civics and Citizenship", "Agricultural Studies" ]
GPA = {
    5.0: "A+",
    4.0: "A",
    3.5: "A-",
    3.0: "B",
    2.0: "C",
    1.0: "D",
    0.0: "F"

}

# This function calculate indivisual subject grade 
def gradeCalculator(num):
    if num >= 80 and num <= 100:
        return 5.0
    elif num >= 70 and num < 80:
        return 4.0
    elif num >= 60 and num < 70:
        return 3.50
    elif num >= 50 and num < 60:
        return 3.0
    elif num >= 40 and num < 50:
        return 2.0
    elif num >= 33 and num < 40:
        return 1.0
    elif num >= 0  and num < 33:
        return 0.0

# This function calculate  final GPA
def finalGrade(grades, benefit, optionalSub):
    avgBangla = (marks["Bangla (First Paper)"] + marks["Bangla (Second Paper)"]) / 2.0
    avgEnglish = (marks["English (First Paper)"] + marks["English (Second Paper)"]) / 2.0
    grades['Bangla'] = gradeCalculator(avgBangla)
    grades['English'] = gradeCalculator(avgEnglish)
    totalGrade = 0
    combineSubject = ["Bangla (First Paper)","Bangla (Second Paper)", "English (First Paper)", "English (Second Paper)"]
    for subjectName, grade in grades.items():
        if subjectName in combineSubject:
            continue
        else:
            if grade == 0.0:
                return 0.0
            else:
                totalGrade += grade
    totalGrade = totalGrade - grades[optionalSub] + benefit
    return totalGrade / 8

# This function clear the terminal for better view 
def clear_terminal():
    os.system('cls')
    print("-"*10,"Welcome to Student Grade Calculator","-"*10)

# This function takes valid subject mark 
def get_valid_mark(subject):
  while True:
    print(f"Enter the mark of {subject}: ",end="")
    mark = input()
    try:
        mark = float(mark)
        if mark < 0.0 or mark > 100.0:
          print("Mark must be between 0 - 100")
        else:
          return mark
    except ValueError:
        print("Invalid input. Enter value between 0 - 100")

# This function takes marks of all subject and assign grade 
def get_marks(compulsory, core):
    for subject in compulsory:
        mark = get_valid_mark(subject)
        marks[subject] = mark
        grades[subject] = gradeCalculator(mark)
    for subject in core:
        mark = get_valid_mark(subject)
        marks[subject] = mark
        grades[subject] = gradeCalculator(mark)

# This function print the indivisual grade with final gpa 
def printResult(grades, finalGrade, group):
  commonSubject = ["Bangla", "English", "Mathematics", "Information and Communication Technology (ICT)", "Religion Studies"]
  partSubject = ["Bangla (First Paper)","Bangla (Second Paper)", "English (First Paper)", "English (Second Paper)"]
  print("{} {}".format("Subject Name".ljust(50),"Grade"))
  print("-"*60)
  for subject in commonSubject:
    print(f"{subject.ljust(50)} {GPA[grades[subject]]}")

  for key, value in grades.items():
    if key in commonSubject or key in partSubject:
      continue
    else:
      print(f"{key.ljust(50)} {GPA[value]}")
  print(f"Final grade: {finalGrade:.2f}".rjust(25))


# This is the main program section 
flag = 1
while(flag):
    marks = {}
    grades = {}
    clear_terminal()
    print("Enter the group name: ")
    print("1. Science")
    print("2. Commerce")
    print("3. Arts")
    background = int(input())
    clear_terminal()
    if background == 1:
        get_marks(compulsorySubject,scienceSubject)
        clear_terminal()
        print("1. Biology")
        print("2. Higher Mathematics")
        optional = int(input("which one is optional subject?: "))
        clear_terminal()
        if optional == 1:
            benefit = grades["Biology"] - 2.0 if grades["Biology"] > 2.0 else 0.0
            optionalSub = "Biology"
        if optional == 2:
            benefit = grades["Higher Mathematics"] - 2.0 if grades["Higher Mathematics"] > 2.0 else 0.0
            optionalSub = "Higher Mathematics"
    if background == 2:
        get_marks(compulsorySubject,commerceSubject)
        clear_terminal() 
        print("1. Agricultural Studies")
        print("2. Higher Mathematics")       
        print("3. Economics")       
        print("4. Geography")       
        print("5. Home Science")  
        optional = int(input("Choose optional subject: "))
        print(f"Enter the mark of {commerceOptional[optional-1]}: ")
        mark = get_valid_mark(commerceOptional[optional-1]) 
        clear_terminal() 
        marks[commerceOptional[optional-1]] = mark   
        grades[commerceOptional[optional-1]] = gradeCalculator(mark)
        benefit = grades[commerceOptional[optional-1]] - 2.0 if grades[commerceOptional[optional-1]] > 2.0 else 0.0
        optionalSub = commerceOptional[optional-1]
    if background == 3:
        get_marks(compulsorySubject,artsSubject)
        clear_terminal()
        print("1. Bangladesh and Global Studies")
        print("2. Geography and Environment")       
        print("3. Civics and Citizenship")       
        print("4. Agricultural Studies")
        optional = int(input("Choose optional subject: "))
        clear_terminal()
        benefit = grades[artsSubject[optional-1]] - 2.0 if grades[artsSubject[optional-1]] > 2.0 else 0.0
        optionalSub = artsSubject[optional-1]

    result = finalGrade(grades, benefit, optionalSub)
    printResult(grades, result, background)

    print("Do you wish to continue:")
    print("1. Yes")
    print("2. No")
    res = int(input())
    flag = 1 if res == 1 else 0
