import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("AmsterdamLR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
plt.plot(x, y, linestyle='-', linewidth = 2, color = "blue")

data = pd.read_csv("AmsterdamHR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
plt.plot(x, y, linestyle='-', linewidth = 1, color = "crimson")

data = pd.read_csv("JungleJuiceLR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 100
plt.plot(x, y, linestyle='-', linewidth = 1, color = "blue")

data = pd.read_csv("JungleJuiceHR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 100
plt.plot(x, y, linestyle='-', linewidth = 1, color = "crimson")

data = pd.read_csv("RaveLR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 200
plt.plot(x, y, linestyle='-', linewidth = 1, color = "blue")

data = pd.read_csv("RaveHR.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 200
plt.plot(x, y, linestyle='-', linewidth = 1, color = "crimson")



plt.legend(["AmsterdamLR", "AmsterdamHR", "JungleJuiceLR", "KJungleJuiceHR", "RaveLR", "RaveHR"], fontsize = 20)
plt.xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Absorbancia", fontsize = 20)
plt.title("IČ")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()