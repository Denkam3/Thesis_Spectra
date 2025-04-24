import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_data(data, threshold = 150):
    return data[data[:,0] >= threshold]

def filter_low(data, threshold = 550):
    return data[data.iloc[:,0] >= threshold]

def filter_experiment(data, low = 550, high = 3500):
    return data[(data.iloc[:,0] >= low) & (data.iloc[:,0] <= high)]

def remove_x_range(data, low=2000, high=2700):
    """Odstráni dáta v intervale x od 'low' po 'high'."""
    return data[(data[:, 0] < low) | (data[:, 0] > high)]

"""file_path = "B3LYP_Mol1" 
data = np.loadtxt(file_path)
data = filter_data(data)
data = remove_x_range(data)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 2, color = "darkblue")

file_path = "pvDz_Mol1"
data = np.loadtxt(file_path)
data = filter_data(data)
data = remove_x_range(data)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 2, color = "crimson")"""

file_path = "pvTz_Mol1_Ram" 
data = np.loadtxt(file_path)
# data = filter_data(data)
# data = remove_x_range(data)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 2, color = "green")

"""file_path = "pvTz_Mol2" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 100
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol3" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 200
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol4" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 300
plt.plot(x, y, linestyle='-', linewidth = 2)

file_path = "pvTz_Mol5" 
data = np.loadtxt(file_path)
data = filter_data(data)

x, y = data[:, 0], data[:, 1]
y = y + 400
plt.plot(x, y, linestyle='-', linewidth = 2)

data = pd.read_csv("Amsterdam_MIR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y - 100
plt.plot(x, y, linestyle='-', linewidth = 2,)

data = pd.read_csv("Jungle Juice_MIR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y - 200
plt.plot(x, y, linestyle='-', linewidth = 2)

data = pd.read_csv("Rave_MIR.csv", sep = ";", header = None)
data = filter_experiment(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]
y = y * 1000
y = y - 300
plt.plot(x, y, linestyle='-', linewidth = 2)"""

"""legend1 = plt.legend(["1", "2", "3", "4", "5"], loc = "upper left", fontsize = 16)
lines = plt.gca().get_lines()
legend2 = plt.legend([lines[5], lines[6], lines[7]],
                     ["Amsterdam", "Jungle Juice", "Rave"], 
                     loc = "upper right", fontsize = 16)
plt.gca().add_artist(legend1)"""

# plt.legend(["1", "2", "3", "4", "5", "Amsterdam", "JungleJuice", "Rave"], fontsize = 16)
# plt.legend(["1", "2", "3", "4", "5"], fontsize = 20)
plt.legend(["B3LYP/6-311++G", "MP2/cc-pVDZ", "MP2/cc-pVTZ"], fontsize = 20)
plt.xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Absorbancia", fontsize = 20)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(200))
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(50))
plt.gca().xaxis.set_minor_formatter(plt.NullFormatter()) 
plt.grid(False)
plt.tick_params(axis='x', labelsize=15)
plt.yticks([])
plt.show()