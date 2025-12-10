class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
    def get_id(self):
        return self.__id   
    def get_name(self):
        return self.__name   
    def get_dob(self):
        return self.__dob   
    def student_info(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DOB: {self.__dob}")
    def dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'dob': self.__dob
        }
    
class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name
    def get_id(self):
        return self.__id    
    def get_name(self):
        return self.__name    
    def course_info(self):
        print(f"ID: {self.__id} | Course name: {self.__name}")
    def dict(self):
        return {
            'id': self.__id,
            'name': self.__name
        }
    
class Mark:
    def __init__(self):
        self.__mark = {}
    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.__mark:
            self.__mark[course_id] = {}
        self.__mark[course_id][student_id] = mark
    def get_mark(self, course_id):
        return self.__mark.get(course_id, {})    
    def mark_for_course(self, course_id):
        return course_id in self.__mark
    def get_student_mark(self, course_id, student_id):
        if course_id in self.__mark:
            return self.__mark[course_id].get(student_id)
        return None
    
class StuMana:
    def __init__(self):
        self.__students = []
    def input(self):
        while True:
            try:
                num = int(input("Enter the numbers of students: "))
                if num > 0:
                    break
                else:
                    print("Please enter positive number.")
            except ValueError:
                print("Please enter valid number.")
        for _ in range(num):
            student_id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter the date of birth(DD/MM/YYYY): ")
            self.__students.append(Student(student_id, name, dob))
    def list(self):
        if not self.__students:
            print("No student availible to list.")
            return       
        for student in self.__students:
            student.student_info()
    def get_students(self):
        return self.__students   
    def get_stu_id(self, student_id):
        for student in self.__students:
            if student.get_id() == student_id:
                return student
        return None
    def is_empty(self):
        return len(self.__students) == 0
    
class CourseMana:
    def __init__(self):
        self.__courses = []    
    def input(self):
        while True:
            try:
                num = int(input("Enter the numbers of courses: "))
                if num > 0:
                    break
                else:
                    print("Please enter positive number.")
            except ValueError:
                print("Please enter valid number.")        
        for _ in range(num):
            course_id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.__courses.append(Course(course_id, name))        
    def list(self):
        if not self.__courses:
            print("No course availible")
            return       
        for i, course in enumerate(self.__courses, 1):
            print(f"{i}.", end=" ")
            course.course_info()
    def get_courses(self):
        return self.__courses  
    def get_courseindex(self, index):
        if 0 <= index < len(self.__courses):
            return self.__courses[index]
        return None   
    def is_empty(self):
        return len(self.__courses) == 0
    
class MarkMana:
    def __init__(self, stu_mana, cour_mana):
        self.__mark_system = Mark()
        self.__student_mana = stu_mana
        self.__course_mana = cour_mana
    def input_mark(self):
        if self.__student_mana.is_empty() or self.__course_mana.is_empty():
            print("Enter students and courses first.")
            return
        self.__course_mana.list()
        while True:
            try:
                choice = int(input("Select course to show marks (enter number): "))
                if 1 <= choice <= len(self.__course_mana.get_courses()):
                    selected_course = self.__course_mana.get_courseindex(choice - 1)
                    break
                print("Invalid choice")
            except ValueError:
                print("Please enter a number.")
        course_id = selected_course.get_id()
        print(f"\nEnter marks for course: {selected_course.get_name()}")
        for student in self.__student_mana.get_students():
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.get_name()} ({student.get_id()}): "))
                    if 0 <= mark <= 20:
                        self.__mark_system.add_mark(course_id, student.get_id(), mark)
                        break
                    print("Mark should be between 0 and 20")
                except ValueError:
                    print("Please input valid number")
    def show_mark(self):
        if self.__course_mana.is_empty():
            print("No courses availible")
            return        
        self.__course_mana.list()
        while True:
            try:
                choice = int(input("Select course to show marks (enter number): "))
                selected_course = self.__course_mana.get_courseindex(choice - 1)
                if selected_course:
                    break
                print("Invalid choice")
            except ValueError:
                print("Please enter a number.")            
        course_id = selected_course.get_id()
        print(f"Mark: {selected_course.get_name()} ({course_id})")
        if self.__mark_system.mark_for_course(course_id):
            for student in self.__student_mana.get_students():
                student_id = student.get_id()
                mark = self.__mark_system.get_student_mark(course_id, student_id)
                if mark is not None:
                    print(f"Student: {student.get_name()} ({student_id}) | Mark: {mark}")
                else:
                    print(f"Student: {student.get_name()} ({student_id}) | Mark: Not entered")
        else:
            print("No marks entered for this course yet")

class System:
    def __init__(self):
        self.__stu_mana = StuMana()
        self.__cour_mana = CourseMana()
        self.__mark_mana = MarkMana(self.__stu_mana, self.__cour_mana)
    def run(self):
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
                self.__stu_mana.input()
            elif choice == '2':
                self.__cour_mana.input()
            elif choice == '3':
                self.__mark_mana.input_mark()
            elif choice == '4':
                self.__stu_mana.list()
            elif choice == '5':
                self.__cour_mana.list()
            elif choice == '6':
                self.__mark_mana.show_mark()
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

def main():
        system = System()
        system.run()
    
if __name__ == "__main__":
    main()