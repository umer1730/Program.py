import matplotlib.pyplot as plt
matches=[1,2,3,4,5]
scores=[5,100,70,20,48]  # if you add label then these score and matches print
plt.plot(matches,scores)
plt.show()

# differene 

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,100,70,20,48]  # if you add label then these score and matches print
plt.xlabel("matches")
plt.ylabel("scores")
plt.plot(x,y)
plt.show()