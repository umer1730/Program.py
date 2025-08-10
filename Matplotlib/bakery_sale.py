import matplotlib.pyplot as plt
x = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
y = [10,15,21,17,25,27,30]
plt.plot(x,y)
plt.title("Bakery sales this week")
plt.xlabel("Day of the week")
plt.ylabel("Sales of the week")
plt.show()