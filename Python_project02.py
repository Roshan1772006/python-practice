"""
add
update
delete
view
exit
"""

#initialising dictionary
student_grades = {}

#add a new student
def add_student(name,grade):
    student_grades[name] = grade
    #[sagar] = 100
    print(f"Added {name} eiht a {grade}")
    #added a student

#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updates {grade}")

    else:
        print(f"{name} is not found!")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

#view alll sstudent
def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("no student found/added")

def main():
    while True:
        print("\nstudent Grades Management System")
        print("1.Add student")
        print("2.Update student")
        print("3.Delete student")
        print("4.View student")
        print("5.Exit student")
        choice = int(input("Enter your choice ="))
        if choice == 1:
            name =input("Eter student name =")
            grade = int(input("Enter student garde:"))
            add_student(name,grade)

        elif choice==2:
            name=input("Enter student name =")
            grade=int(input("Enter student grade ="))
            update_student(name,grade)

        elif choice ==3:
            name=input("Enter student name = ")
            delete_student(name)

        elif choice==4:
            display_all_students()
            
        elif choice==5:
            print("Closing the program....")
            break

        else:
            print("Invalid value or data")

main()