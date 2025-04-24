import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def filter_data(data, threshold = 1800):
    return data[data[:,0] <= threshold]

def filter_experiment(data, threshold = 1800):
    return data[data.iloc[:,0] <= threshold]

file_path = "NewMin" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

plt.legend(["Konformér 1"], fontsize = 18)
plt.xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Intenzita", fontsize = 20)
plt.title("Raman")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()