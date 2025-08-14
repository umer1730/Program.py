#plt.scatter(x,y,color="colorname",marker="marker style",label="label name")
# scatter plotter is most important in Ml
#simple
import matplotlib.pyplot as plt
hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,60,65,70,75,80,85]
plt.scatter(hours_studies,exam_scores,color="green",marker="o",label="Student data")
plt.xlabel("hours_student")
plt.ylabel("Exam_scores")
plt.title("Relationship between study time and exam score")
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,60,65,70,75,80,85]
colors=["r","y","g","b","r","y","r","g"]
plt.scatter(hours_studies,exam_scores,c=colors,marker="^",label="Student data")
plt.xlabel("hours_student",fontsize=15)
plt.ylabel("Exam_scores",fontsize=15)
plt.title("Relationship between study time and exam score",fontsize=15)
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,65,70,60,75,80,85]
colors=["r","y","g","b","r","y","r","g"]
sizes=[15,200,6,300,12,100,18,50]
plt.scatter(hours_studies,exam_scores,c=colors,marker="*",label="Student data",s=sizes,alpha=0.4,edgecolor="g",linewidth=2)   # aplha is given dull value if ou remove alpha then remove dullness
plt.xlabel("hours_student",fontsize=15)
plt.ylabel("Exam_scores",fontsize=15)
plt.title("Relationship between study time and exam score",fontsize=15)
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,65,70,60,75,80,85]
colors=["r","y","g","b","r","y","r","g"]
sizes=[15,200,6,300,12,100,18,50]
plt.scatter(hours_studies,exam_scores,c=colors,marker="o",label="Student data",s=sizes,cmap="viridis")   # aplha is given dull value if ou remove alpha then remove dullness
plt.colorbar()
plt.xlabel("hours_student",fontsize=15)
plt.ylabel("Exam_scores",fontsize=15)
plt.title("Relationship between study time and exam score",fontsize=15)
plt.legend()
plt.grid()
plt.show()