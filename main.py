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
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade 

    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.__grade = value

#composition is appropriate because an enrollment connects existing Student and Course objects.

person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

person.describe()
student.describe()

print(student)

course1 = Course("CS101", "Introduction to Programming", 2)
course2 = Course("DB101", "Introduction to Databases", 3)

print(course1)
print(course2)

enrollment = Enrollment(student, course1, 85)

print(enrollment.grade)

enrollment.grade = 89

print(enrollment.student.name)
print(enrollment.course.code)
print(enrollment.grade)

