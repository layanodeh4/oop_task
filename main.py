class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
        

    def describe(self):
        print(f"person id: {self.person_id}, name: {self.name}")


class Student(Person):
    def __init__(self, person_id, name, major):
        super().__init__(person_id, name)
        self.major = major
        

    def describe(self):
        print(f"student id: {self.person_id}, name: {self.name}, major: {self.major}")

    def __str__(self):
        return f"student id: {self.person_id}, name: {self.name}, major: {self.major}"


# Student IS-A Person, so inheritance makes sense because a student
# has all the basic information of a person plus student-specific data.        

class Course:
    def __init__(self, code, name, seats):
        self.code = code
        self.name = name
        self.seats = seats

    def __str__(self):
        return f"code: {self.code}, course name: {self.name}, seats: {self.seats}"


class Enrollment:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

    @property
    def grade(self):
        return self.__grade 

    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.__grade = value

#composition is appropriate because an enrollment connects existing Student and Course objects.


class Registry:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course, grade):
        enrollment = Enrollment(student, course, grade)
        self.enrollments.append(enrollment)  
        return enrollment

    def show_students(self):
        print("\nStudents")
        for s in self.students:
            print(s)

    def show_courses(self):
        print("\nCourses")
        for c in self.courses:
            print(c)

    def show_enrollments(self):
        print("\nEnrollments")
        for e in self.enrollments:
            print(f"{e.student.name} -> {e.course.name} -> Grade: {e.grade}")



person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

person.describe()
student.describe()

print(student)

s1 = Student(102, "ahmad", "AI")
s2 = Student(103, "leen", "computer science")
s3 = Student(104, "omar", "AI")

c1 = Course("py110", "python", 4)
c2 = Course("ml111", "oop", 5)

registry = Registry()

registry.add_student(s1)
registry.add_student(s2)
registry.add_student(s3)

registry.add_course(c1)
registry.add_course(c2)

registry.enroll_student(s1, c1, 77)
registry.enroll_student(s2, c2, 89)
registry.enroll_student(s3, c1, 83)

registry.show_students()
registry.show_courses()
registry.show_enrollments()



try:
    user_input = input("Enter grade: ")
    grade = int(user_input)

    enrollment = registry.enroll_student(s1, c1, grade)

    print("Enrollment created successfully.")
    print(f"Grade: {enrollment.grade}")

except ValueError as error:
    print(f"Error: {error}")
