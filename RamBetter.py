import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_data(data, threshold = 150):
    return data[data.iloc[:,0] >= threshold]

def filter_experiment(data, threshold = 1800):
    return data[data.iloc[:,0] <= threshold]

def filter_cal(data, threshold = 1800):
    return data[data[:,0] <= threshold]

"""data = pd.read_csv("Amsterdam500mW.csv", sep = ";", header = None)
# data = filter_data(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)"""

data = pd.read_csv("JungleJuice500mW.csv", sep = ";", header = None)
data = filter_data(data)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 500
y = y - 20
plt.plot(x, y, linestyle='-', linewidth = 1)

"""data = pd.read_csv("Rave500mW.csv", sep = ";", header = None)
# data = filter_data(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y + 0.4
plt.plot(x, y, linestyle='-', linewidth = 1)"""

file_path = "Mol1Ram" 
data = np.loadtxt(file_path)
data = filter_cal(data)

x, y = data[:, 0], data[:, 1]
y = y + 30
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol2Ram"
data = np.loadtxt(file_path)
data = filter_cal(data)

x, y = data[:, 0], data[:, 1]
y = y + 60
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol3Ram" 
data = np.loadtxt(file_path)
data = filter_cal(data)

x, y = data[:, 0], data[:, 1]
y = y + 90
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol4Ram" 
data = np.loadtxt(file_path)
data = filter_cal(data)

x, y = data[:, 0], data[:, 1]
y = y + 120
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol5Ram" 
data = np.loadtxt(file_path)
data = filter_cal(data)

x, y = data[:, 0], data[:, 1]
y = y + 150
plt.plot(x, y, linestyle='-', linewidth = 1)

plt.legend(["Jungle Juice", "Konformér 1", "Konformér 2", "Konformér 3", "Konformér 4", "Konformér 5"], fontsize = 18)
plt.xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Relatívna intenzita", fontsize = 20)
plt.title("IČ")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()