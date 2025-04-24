import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_data(data, threshold = 1800):
    return data[data[:,0] <= threshold]

def filter_experiment(data, threshold = 200):
    return data[data.iloc[:,0] >= threshold]

file_path = "pvTz_Mol1" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol2"
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 150
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol3" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 300
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol4" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 450
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol5" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 600
plt.plot(x, y, linestyle='-', linewidth = 2)

"""data = pd.read_csv("AmsterdamLR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 2)"""

data = pd.read_csv("JungleJuiceLR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y - 150
plt.plot(x, y, linestyle='-', linewidth = 2)

"""data = pd.read_csv("RaveLR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y + 0.4
plt.plot(x, y, linestyle='-', linewidth = 2)"""

# plt.legend(["Konformér 1", "Konformér 2", "Konformér 3", "Konformér 4", "Konformér 5", "Amsterdam", "JungleJuice_FIR", "Rave"], fontsize = 18)
plt.legend(["1", "2", "3", "4", "5", "JungleJuice"], fontsize = 16)
plt.xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Absorbancia", fontsize = 20)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(200))
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(50))
plt.gca().xaxis.set_minor_formatter(plt.NullFormatter()) 
plt.grid(False)
plt.tick_params(axis='x', labelsize=15)
plt.yticks([])
plt.show()