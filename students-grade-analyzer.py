def display_student_summary(student_name, student_grade):
   for i in range(len(student_name)):
    print("student name is: ",student_name[i]+ " his grade is:",student_grade[i])
def get_avg_grade(student_grade):
   sum_of_grades=0
   for grades in student_grade:
      sum_of_grades+=grades
   return sum_of_grades / len(student_grade)

def get_heighest_grade(s_name,s_grade, hieghest_grade_index=0, i=0):
  
    if i==len(s_name):
       return s_name[hieghest_grade_index] ,s_grade[hieghest_grade_index]
    if s_grade[i]> s_grade[hieghest_grade_index]:
      hieghest_grade_index=i
    return(get_heighest_grade(s_name,s_grade,hieghest_grade_index,i+1))
def count_passed (student_grade,i=0,count=0):
   if i==len(student_grade):
      return count
   if student_grade[i]>= 60:
      count +=1
   return count_passed(student_grade,i+1,count)

   
student_name=[]
student_grade=[]
number_of_students=input("Enter number of the  students in the class: ")
while not number_of_students.isdigit():
 number_of_students=input("please enter a valid number for students in the class(>0): ")
for i in range (int(number_of_students)):
  s_name=input(f"enter name for student number {i+1}:").capitalize()
  s_grade=input(f"enter the grade for student {s_name}: ")
  while not s_grade.isdigit() or not (0 <= int(s_grade) <= 100):
        s_grade = input(f"Please enter a valid grade (0–100) for {s_name}: ")
  student_name.append(s_name)
  student_grade.append(int(s_grade)) 
  
display_student_summary(student_name, student_grade)
avg=get_avg_grade(student_grade)
print("The average of the class is: ",get_avg_grade(student_grade))
hieghest_student, hieghest_grade=get_heighest_grade(student_name,student_grade)
print("The student:",hieghest_student +" has the hieghest grade which is:",hieghest_grade)
passed_students=count_passed(student_grade)
print("the number of students passed is: ",passed_students)

