# class is a blue print or template
class Student:
    def __init__(self,name,age,grade,roll_no,team):  #__init__ method we call it - constructor, use for initialize the value
        self.name=name  # attribute (properties)
        self.age=age
        self.grade= grade
        self.roll_no=roll_no
        self.team = team

    def display(self):  # method
        print(f"Name: {self.name} \nAge: {self.age} \nGrade: {self.grade} \nRoll no: {self.roll_no} \nTeam: {self.team}")
# we can add another variable in this like team
team1 = 'A'  
team2 = 'B'
# object - instance of class

student_1 = Student("Ali",20,'A',1,team1)
print(student_1.name, student_1.age,student_1.grade,student_1.roll_no)
student_1.display()

print("----2-----")

student_2 = Student("Arslan",20,'B',4,team2)
print(student_2.name, student_2.age,student_2.grade,student_2.roll_no)
student_2.display()
