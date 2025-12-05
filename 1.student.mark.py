students = []
courses = []   
marks = {}
def students_number():
    while True:
        try:
            num = int(input("Enter the numbers of students: "))
            if num > 0:
                return num
            else:
                print("Please enter positive number.")
        except ValueError:
            print("Please enter valid number.")

def student_information():
    students = []
    student_id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter the date of birth(DD/MM/YYYY): ")

    students.append({'id': student_id, 'name': name, 'dob': dob})
    return students

def course_number():
    while True:
        try:
            num = int(input("Enter the numbers of courses: "))
            if num > 0:
                return num
            else:
                print("Please enter positive number.")
        except ValueError:
            print("Please enter valid number.")

def course_infomation():
    courses = []
    course_id = input("Enter course id: ")
    name = input("Enter course name: ")

    courses.append({'id': course_id, 'name': name})
    return courses

def select_course_marks(courses, students):
    print("\n Available courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course['name']} ({course['id']})")
    
    while True:
        try:
            choice = int(input("Select a course (Enter number): "))
            if 1 <= choice <= len(courses):
                selected_course = courses[choice - 1]
                break
            print("Invalid choice.")
        except ValueError:
            print("Enter a number.")
    
    course_id = selected_course['id']
    if course_id not in marks:
        marks[course_id] = {}
    print(f"\nEnter marks for course: {selected_course['name']}")
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student['name']} ({student['id']}): "))
                if 0 <= mark <= 20:
                    marks[course_id][student['id']] = mark
                    break
                print("Mark should be between 0 and 20")
            except ValueError:
                print("Please input valid number")

def list_student(students):
    for student in students:
        print(f"ID: {student['id']} | name: {student['name']} | dob: {student['dob']}")

def list_course(courses):
    for course in courses:
        print(f"ID: {course['id']} | name: {course['name']}")
 
def student_mark_given_course(students, courses):
    if not courses:
        print("No courses available.")
        return
    print("\nAvalible courses.")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course['name']} ({course['id']})")

    while True:
        try:
            choice = int(input("Select course to show marks (enter number): "))
            if 1 <= choice <= len(courses):
                selected_course = courses[choice - 1]
                break
            print("Invalid choice")
        except ValueError:
            print("Please enter a number.")
        
    course_id = selected_course['id']
    print(f"Mark: {selected_course['id']}")

    if course_id in marks:
        for student in students:
            student_id = student['id']
            mark = marks[course_id].get(student_id, "Not Entered")
            print(f"Student: {student['name']} ({student_id}) | Mark: {mark}")
    else:
        print("No marks entered for this course yet")

def main():
    global students, courses, marks

    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Enter marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")

        choice = input("Select an option (1-7): ")
        if choice == '1':
            n = students_number()
            for _ in range(n):
                new = student_information()
                students.extend(new)
        elif choice == '2':
            n = course_number()
            for _ in range(n):
                new = course_infomation()
                courses.extend(new)
        elif choice == '3':
            if not courses or not students:
                print("Please ensure students and courses are entered first.")
            else:
                select_course_marks(courses, students)
        elif choice == '4':
            if not students:
                print("No students available.")
            else:
                list_student(students)
        elif choice == '5':
            if not courses:
                print("No courses available.")
            else:
                list_course(courses)
        elif choice == '6':
            if not courses or not students:
                print("Please ensure students and courses are entered first.")
            else:
                student_mark_given_course(students, courses)
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()