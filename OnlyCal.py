import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_data(data, threshold = 1800):
    return data[data[:,0] <= threshold]

def filter_experiment(data, threshold = 1800):
    return data[data.iloc[:,0] <= threshold]

file_path = "Mol1Ram" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y * 1000
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol2Ram"
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y * 1000
y = y + 15
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol3Ram" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y * 1000
y = y + 30
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol4Ram" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y * 1000
y = y + 45
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol5Ram" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y * 1000
y = y + 60
plt.plot(x, y, linestyle='-', linewidth = 1)

data = pd.read_csv("jj_5_256_100.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

plt.legend(["Konformér 1", "Konformér 2", "Konformér 3", "Konformér 4", "Konformér 5"], fontsize = 18)
plt.xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Relatívna intenzita", fontsize = 20)
plt.title("IČ")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()