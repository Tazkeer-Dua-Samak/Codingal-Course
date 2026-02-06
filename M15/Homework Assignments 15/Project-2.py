import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Penguins Data.csv")

culmen_length = data["Culmen Length (mm)"].dropna()
culmen_depth = data["Culmen Depth (mm)"].dropna()
flipper_length = data["Flipper Length (mm)"].dropna()
body_mass = data["Body Mass (g)"].dropna()

plt.hist(culmen_length, bins=20, rwidth=0.9, color='b')
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Frequency")
plt.title("Culmen Length Histogram")
plt.show()

plt.hist(culmen_depth, bins=20, rwidth=0.9, color='g')
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Frequency")
plt.title("Culmen Depth Histogram")
plt.show()

plt.hist(flipper_length, bins=20, rwidth=0.9, color='r')
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.title("Flipper Length Histogram")
plt.show()

plt.hist(body_mass, bins=20, rwidth=0.9, color='m')
plt.xlabel("Body Mass (g)")
plt.ylabel("Frequency")
plt.title("Body Mass Histogram")
plt.show()
