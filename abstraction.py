# hiding unnecessary details from users through class and method
class Student:
    def __init__(self,name,age,grade,percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.percentage = percentage
    def student_details(self):  #method - abstraction
        print(f"{self.name}'s age is {self.age} and is in class {self.grade} , with {self.percentage+2}%") # now self.percentage+2 is used for hide percentage agr me 2 percentage hr student ko extra dena chahta hu
    
#object - instance of class
student1 = Student('Mahad',20,'C',83)
student2 = Student('Ali',20,'A',93)
student3 = Student('Arslan ',20,'B',91)

print(student1.percentage)
student1.student_details()
student2.student_details()
student3.student_details()