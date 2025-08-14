import matplotlib.pyplot as plt

plt.scatter([1,2,3],[50,55,60],color="green",label="Class A")
plt.scatter([1,2,3],[40,45,50],color="blue",label="Class B")
plt.xlabel("hours_student")
plt.ylabel("Exam_scores")
plt.title("Comparison two classes")
plt.legend()
plt.grid(True)
plt.show()