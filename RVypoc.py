from brokenaxes import brokenaxes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def filter_data(data, threshold=0):
    """Odfiltruj ľavú stranu"""
    return data[data[:, 0] >= threshold]

def remove_x_range(data, low=1850, high=2800):
    """Odstráni dáta v intervale x od 'low' po 'high'."""
    return data[(data[:, 0] < low) | (data[:, 0] > high)]

file_path = "pvTz_Mol1_Ram"
data = np.loadtxt(file_path)
# data = filter_data(data)
# data = remove_x_range(data)

x, y = data[:, 0], data[:, 1]

file_path_2 = "pvTz_Mol2_Ram"
data_2 = np.loadtxt(file_path_2)
# data_2 = filter_data(data_2)
# data_2 = remove_x_range(data_2)

x2, y2 = data_2[:, 0], data_2[:, 1]

file_path_3 = "pvTz_Mol3_Ram"
data_3 = np.loadtxt(file_path_3)
# data_3 = filter_data(data_3)
# data_3 = remove_x_range(data_3)

x3, y3 = data_3[:, 0], data_3[:, 1]

file_path_4 = "pvTz_Mol4_Ram"
data_4 = np.loadtxt(file_path_4)
# data_4 = filter_data(data_4)
# data_4 = remove_x_range(data_4)

x4, y4 = data_4[:, 0], data_4[:, 1]

file_path_5 = "pvTz_Mol5_Ram"
data_5 = np.loadtxt(file_path_5)
# data_5 = filter_data(data_5)
# data_5 = remove_x_range(data_5)

x5, y5 = data_5[:, 0], data_5[:, 1]

# Vytvorenie grafu s prerušením osi
fig = plt.figure(figsize=(10, 6))
bax = brokenaxes(xlims=((0, 1800), (2800, 3500)), hspace=0.05)

# Vykresli
bax.plot(x, y, linestyle='-', linewidth=2, label="1")
bax.plot(x2, y2, linestyle='-', linewidth=2, label="2")
bax.plot(x3, y3, linestyle='-', linewidth=2, label="3")
bax.plot(x4, y4, linestyle='-', linewidth=2, label="4")
bax.plot(x5, y5, linestyle='-', linewidth=2, label="5")

# POPIS
bax.set_xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize=20, labelpad=40)
bax.set_ylabel("Intenzita", fontsize=20, labelpad = 5)
bax.legend(fontsize=20, loc='upper right')

bax.axs[0].xaxis.set_major_locator(MultipleLocator(200))
bax.axs[0].xaxis.set_minor_locator(MultipleLocator(50))

bax.axs[1].xaxis.set_major_locator(MultipleLocator(200)) 
bax.axs[1].xaxis.set_minor_locator(MultipleLocator(50))

bax.axs[0].tick_params(axis='y', labelleft=False, length=0) 
bax.axs[1].tick_params(axis='y', labelleft=False, length=0)  

# Prispôsobenie vzhľadu čiark na osi x
bax.axs[0].tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
bax.axs[0].tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky

bax.axs[1].tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
bax.axs[1].tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky

plt.tight_layout()

plt.show()
