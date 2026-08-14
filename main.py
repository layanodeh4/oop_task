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


person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

person.describe()
student.describe()

print(student)

course1 = Course("CS101", "Introduction to Programming", 2)
course2 = Course("DB101", "Introduction to Databases", 3)

print(course1)
print(course2)