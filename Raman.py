import matplotlib.pyplot as plt
import numpy as np

file_path = "Mol1Ram" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol2Ram" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol3Ram" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol4Ram" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)

file_path = "Mol5Ram" 
data = np.loadtxt(file_path)

x, y = data[:, 0], data[:, 1]
plt.plot(x, y, linestyle='-', linewidth = 1)


plt.legend(["Konformér 1", "Konformér 2", "Konformér 3", "Konformér 4", "Konformér 5"], fontsize = 20)
plt.xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize = 20)
plt.ylabel("Intenzita", fontsize = 20)
plt.title("Raman")
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(250))
plt.grid(True)
plt.yticks([])
plt.show()
