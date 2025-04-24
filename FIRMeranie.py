import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

def filter_data(data, threshold=400):
    """Odstráni dáta s nízkym vlnočtom bez významných pásov."""
    return data[data.iloc[:, 0] >= threshold]

def cut_data(data, threshold=1750):
    """Odstráni dáta s vlnočtom nad fingerprint region."""
    return data[data.iloc[:, 0] <= threshold]

file_paths = ["JungleJuiceLR.csv", "AmsterdamLR.csv", "RaveLR.csv"]
offsets = [0, 0.2, 0.4]
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = pd.read_csv(file_path, sep = ";", header = None )
    data = filter_data(data)
    x, y = data.iloc[:, 0], data.iloc[:, 1] + offset
    data_list.append((x, y))

fig, ax = plt.subplots(figsize=(10, 7))

labels = ["Jungle Juice", "Amsterdam", "Rave"]
for (x, y), label in zip(data_list, labels):
    ax.plot(x, y, linestyle='-', linewidth=2, label=label)

ax.set_xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize=20, labelpad = 10)
ax.set_ylabel("Absorbancia", fontsize=20, labelpad = 5)
ax.legend(fontsize=20, loc='upper left')

ax.xaxis.set_major_locator(MultipleLocator(200))
ax.xaxis.set_minor_locator(MultipleLocator(50))

ax.tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)
ax.tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)
ax.tick_params(axis='y', labelleft=False, length=0)

plt.tight_layout()
plt.show()
