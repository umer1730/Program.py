# allows one class {new}(child) to reuse the prop and methods of another class {old}(parent).
''' agr apne koi class pehle se bna kr rakhi ha ab future me ap nai class bnate ho but ap chahte ho uske method use kr sko
to ab me dobara q method bnao jb method apne already purani class me likha hua ha time bacha ne ke liye inheritance method use kia jata ha'''
# this is parent class...........
class Student:
    def __init__(self,name,age,grade,percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.percentage = percentage
    def student_details(self):  #method
        print(f"{self.name} age is {self.age} and is in class {self.grade} , with {self.percentage}%") 
    
#object - instance of class
student1 = Student('Mahad',20,'C',83)
student2 = Student('Ali',20,'A',93)
student3 = Student('Arslan ',20,'B',91)

# print(student1.percentage)
# student1.student_details()
# student2.student_details()
# student3.student_details()

# this is child class.........
class GraduateStudent(Student): 
    # we can also add and remove parameters like age & stream
    def __init__(self,name,age,grade,percentage,stream): # old parameters from parent class and new parameters in child class
        super().__init__(name,age,grade,percentage) #call parent class init
        self.stream = stream # new attribute in child class

    def student_details(self):
        return super().student_details()    # method inherit from parent class 

Grad_Student1 = GraduateStudent('Ahmer',18,'B',87,'PCM')
print(Grad_Student1.stream)

# we can also print
print(student1.percentage)

Grad_Student1.student_details()
