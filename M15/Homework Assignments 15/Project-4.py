import matplotlib.pyplot as plt
 
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
new_births = [12, 15, 11, 9, 1, 9, 21]

plt.plot(day, new_births)
plt.title("Birth Rate of July")
plt.xlabel('Day')
plt.ylabel('Birth Rate')
plt.show()