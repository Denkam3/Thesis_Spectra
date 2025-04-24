import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

def filter_experiment(data, low = 300, high = 1800):
    """Odstráni dáta s nízkym a vysokým vlnočtom z experimentu bez významných pásov."""
    return data[(data.iloc[:,0] >= low) & (data.iloc[:,0] <= high)]

def filter_data(data, low = 300, high = 1800):
    """Odstráni dáta s nízkym a vysokým vlnočtom z výpočtov bez významných pásov."""
    return data[(data[:,0] >= low) & (data[:,0] <= high)]

# Načítanie dát pre jednotlivé čiary
# Načítanie dát pre jednotlivé čiary
file_paths = ["JungleJuiceLR.csv"]
offsets = [-300]  # Posuny pre jednotlivé dataset-y
file_paths_cal = ["pvTz_Mol1", "pvTz_Mol2", "pvTz_Mol3", "pvTz_Mol4", "pvTz_Mol5"]
offsets_cal = [-100, 50, 200, 350, 500]  # Posuny pre jednotlivé dataset-y
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = pd.read_csv(file_path, sep = ";", header = None )
    data = filter_experiment(data)
    x, y = data.iloc[:, 0], data.iloc[:, 1] * 1000 + offset
    data_list.append((x, y))

for file_path, offset in zip(file_paths_cal, offsets_cal):
    data = np.loadtxt(file_path)
    data = filter_data(data)
    x, y = data[:, 0], data[:, 1] + offset
    data_list.append((x,y))

# Vytvorenie grafu s prerušením osi pomocou brokenaxes
fig, ax = plt.subplots(figsize=(10, 7))

# Vykreslenie čiar
labels = ["Jungle Juice", "1", "2", "3", "4", "5"]
for (x, y), label in zip(data_list, labels):
    ax.plot(x, y, linestyle='-', linewidth=2, label= label)

# Nastavenie popisov
ax.set_xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize=20, labelpad = 10)
ax.set_ylabel("Relatívna absorbancia", fontsize=20, labelpad = 5)
ax.legend(fontsize=15, loc='upper left')

# Nastavenie hlavných a vedľajších čiark na os x
ax.xaxis.set_major_locator(MultipleLocator(200))  # Hlavné čiarky každých 200 jednotiek
ax.xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Prispôsobenie vzhľadu čiark
ax.tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
ax.tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky
ax.tick_params(axis='y', labelleft=False, length=0)  # Odstránenie čísel a čiark na osi y

plt.tight_layout()
plt.show()