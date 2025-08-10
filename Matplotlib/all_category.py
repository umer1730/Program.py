import matplotlib.pyplot as plt
subject= ["Eng","Math","Phy","Che","Bio"]
marks=[85,90,70,86,82]
plt.xlabel("Subject",fontsize=10)  #if you want to size charcter
plt.ylabel("Marks",fontsize=10)
plt.title("Student marks avg",fontsize=10)
c=["y","b","m","g"]
plt.bar(subject,marks,color=c,width=0.4,label="Student avg",linewidth=5,linestyle=":",alpha=0.4)   #alpha is given dull value
plt.legend()
plt.show()

# for two colors
import matplotlib.pyplot as plt
subject= ["Eng","Math","Phy","Che","Bio"]
marks=[85,90,70,86,82]
marks1=[20,30,40,50,40]
plt.xlabel("Subject",fontsize=10)  #if you want to size charcter
plt.ylabel("Marks",fontsize=10)
plt.title("Student marks avg",fontsize=10)
c=["y","b","m","g"]
plt.bar(subject,marks,width=0.4,color="r",label="Student avg")   #alpha is given dull value
plt.bar(subject,marks1,width=0.4,color="y",label="Student avg1")
plt.legend()
plt.show()

# for create double graph
import matplotlib.pyplot as plt
import numpy as np
subject= ["Eng","Math","Phy","Che","Bio"]
marks=[85,90,70,86,82]
marks1=[20,30,40,50,40]
width=0.2
p=np.arange(len(subject))
p1=[j+width for j in p]
plt.xlabel("Subject",fontsize=10)  #if you want to size charcter
plt.ylabel("Marks",fontsize=10)
plt.title("Student marks avg",fontsize=10)
plt.bar(p,marks,width,color="r",label="Student avg")   #alpha is given dull value
plt.bar(p1,marks1,width,color="y",label="Student avg1")
# plt.xticks(p+width/2,subject)   by adding this line give subject name
# plt.xticks(p+width/2,subject,rotation=10)   give sunject name rotate
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
subject= ["Eng","Math","Phy","Che","Bio"]
marks=[85,90,70,86,82]
marks1=[20,30,40,50,40]
width=0.2
p=np.arange(len(subject))
p1=[j+width for j in p]
plt.xlabel("Subject",fontsize=10)  #if you want to size charcter
plt.ylabel("Marks",fontsize=10)
plt.title("Student marks avg",fontsize=10)
plt.barh(p,marks,width,color="r",label="Student avg")   #alpha is given dull value
plt.bar(p1,marks1,width,color="y",label="Student avg1")  # by adding barh both give horizontal
# plt.xticks(p+width/2,subject)   by adding this line give subject name
# plt.xticks(p+width/2,subject,rotation=10)   give sunject name rotate
plt.legend()
plt.show()



import matplotlib.pyplot as plt
regions= ["Islamabad","Lahore","Karachi","Multan"]
revenue=[200,300,400,500]
plt.pie(revenue,labels=regions,autopct="%1.1f%%",colors=["gold","green","yellow","blue"])
plt.title("Revenue contribution")
plt.show()


import matplotlib.pyplot as plt
marks=[33,44,55,66,33,64,71]
plt.hist(marks,bins=5,color="purple",edgecolor="black")
plt.xlabel("marks")
plt.ylabel("Subject")
plt.title("Student avg")
plt.show()