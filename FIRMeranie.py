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

# Načítanie dát pre jednotlivé čiary
file_paths = ["JungleJuiceLR.csv", "AmsterdamLR.csv", "RaveLR.csv"]
offsets = [0, 0.2, 0.4]  # Posuny pre jednotlivé dataset-y
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = pd.read_csv(file_path, sep = ";", header = None )
    data = filter_data(data)
    x, y = data.iloc[:, 0], data.iloc[:, 1] + offset
    data_list.append((x, y))

# Vytvorenie grafu
fig, ax = plt.subplots(figsize=(10, 7))

# Vykreslenie čiar
labels = ["Jungle Juice", "Amsterdam", "Rave"]
for (x, y), label in zip(data_list, labels):
    ax.plot(x, y, linestyle='-', linewidth=2, label=label)

# Nastavenie popisov
ax.set_xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize=20, labelpad = 10)
ax.set_ylabel("Absorbancia", fontsize=20, labelpad = 5)
ax.legend(fontsize=20, loc='upper left')

# Nastavenie hlavných a vedľajších čiark na os x
ax.xaxis.set_major_locator(MultipleLocator(200))  # Hlavné čiarky každých 200 jednotiek
ax.xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Prispôsobenie vzhľadu čiark
ax.tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
ax.tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky
ax.tick_params(axis='y', labelleft=False, length=0)  # Odstránenie čísel a čiark na osi y

plt.tight_layout()
plt.show()