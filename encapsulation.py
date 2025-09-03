# restrict access to certain attributs or methods to protect data and enforce controlled access
# kisi bhi methd ko agr ap private rakhna chahte ho
class Student:
    def __init__(self,name,age,grade,percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.__percentage = percentage  # double underscore limits access methods

    def get_percentage(self):  # ab access krskte ha
        return self.__percentage # double quote ko as a private use kia jata ha 

    def student_details(self):  #method 
        print(f"{self.name} age is {self.age} and is in class {self.grade} , with {self.percentage}%") 
    
#object - instance of class
student1 = Student('Mahad',20,'C',83)
student2 = Student('Ali',20,'A',93)
student3 = Student('Arslan ',20,'B',91)

print(student1.get_percentage())
# student1.student_details()
# student2.student_details()
# student3.student_details()