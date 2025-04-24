import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_experiment(data, threshold = 400):
    return data[data.iloc[:,0] >= threshold]

def filter_high(data, threshold = 1000):
    return data[data.iloc[:,0] <= threshold]

data = pd.read_csv("AmsterdamHR.csv", sep = ";", header = None)
data = filter_experiment(data)
data = filter_high(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
plt.plot(x, y, linestyle='-', linewidth = 2)

data = pd.read_csv("JungleJuiceHR.csv", sep = ";", header = None)
data = filter_experiment(data)
data = filter_high(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 100
plt.plot(x, y, linestyle='-', linewidth = 2)

data = pd.read_csv("RaveHR.csv", sep = ";", header = None)
data = filter_experiment(data)
data = filter_high(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y + 200
plt.plot(x, y, linestyle='-', linewidth = 2)

plt.legend(["Amsterdam", "Jungle Juice", "Rave"], fontsize = 20)
plt.xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Absorbancia", fontsize = 20)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(200))
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(50))
plt.gca().xaxis.set_minor_formatter(plt.NullFormatter()) 
plt.grid(False)
plt.tick_params(axis='x', labelsize=15)
plt.yticks([])
plt.show()