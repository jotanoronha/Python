print("\n------------- \n SUN SCHOOL \n-------------")


count = 1
amout_students = int(input("How many students does the school have? "))
best_grade = 0
best_student = ""


while count <= amout_students:
    print(f"STUDENT {count}")
    student_name = (input("What is the student's name? "))
    students_grade = float(input("How was the student's grade? "))
    count = count + 1


    if  students_grade > best_grade:
        best_grade = students_grade
        best_student = student_name

print(f"The best student's was: {best_student} \n Grade: {best_grade}")


