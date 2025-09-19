class Student:
    def __init__(self):
        self.rollNumber = 0
        self.name = ""
        self.marks = 0.0

    def setData(self, r, n, m):
        self.rollNumber = r
        self.name = n
        self.marks = m

    def display(self):
        print("Roll number:", self.rollNumber)
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student()
s2 = Student()

s1.setData(1, "Ali", 85.5)
s2.setData(2, "Arslan", 95.5)

print("Student 1 information:")
s1.display()
print("---------------")
print("Student 2 information:")
s2.display()
