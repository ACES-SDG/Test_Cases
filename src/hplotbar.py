
import matplotlib.pyplot as plt
y=['one', 'two', 'three', 'four', 'five']
 
# getting values against each value of y
x=[5]
plt.barh(x,width=1)
 
# setting label of y-axis
plt.ylabel("pen sold")
 
# setting label of x-axis
plt.xlabel("price")
plt.title("Horizontal bar graph")
plt.show()