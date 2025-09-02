#  allows methods in diff clases to have same name but diff behaviour depending on object

class Student:
    def __init__(self,name,age,grade,percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.percentage = percentage

    def student_details(self):  #method - abstraction
        print(f"{self.name} age is {self.age} and is in class {self.grade} , with {self.percentage}%") 
#object - instance of class
student1 = Student('Mahad',20,'C',83)
student2 = Student('Ali',20,'A',93)
student3 = Student('Arslan ',20,'B',91)

# this is child class.........
class GraduateStudent(Student): 
    def __init__(self,name,age,grade,percentage,stream): 
        super().__init__(name,age,grade,percentage) 
        self.stream = stream 
    def student_details(self): # you can change name
        print(f"{self.name} is in class {self.grade}, with {self.percentage} and from stream {self.stream}")

Grad_Student1 = GraduateStudent('Ahmer',18,'B',87,'PCM')
# print(Grad_Student1.stream) # can write

# print(student1.percentage)  # can write
student1.student_details()
Grad_Student1.student_details()