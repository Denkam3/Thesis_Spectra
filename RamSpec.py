import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("ams_5_256_100.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

data = pd.read_csv("jj_5_256_100.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

data = pd.read_csv("rave_5_256_100.csv", sep = ";", header = None)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y - 100
plt.plot(x, y, linestyle='-', linewidth = 1)

plt.legend(["Amsterdam", "JungleJuice", "Rave"], fontsize = 18)
plt.xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Intenzita", fontsize = 20)
plt.title("IČ")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()