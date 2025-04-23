import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def filter_data(data, threshold=0):
    """Odstráni dáta s nízkym vlnočtom bez významných pásov."""
    return data[data[:, 0] >= threshold]

def cut_data(data, threshold=1750):
    """Odstráni dáta s vlnočtom nad fingerprint region."""
    return data[data[:, 0] <= threshold]

# Načítanie dát pre jednotlivé čiary
file_paths = ["pvTz_Mol1_Ram", "pvTz_Mol2_Ram", "pvTz_Mol3_Ram", "pvTz_Mol4_Ram", "pvTz_Mol5_Ram"]
offsets = [0, 10, 20, 30, 40]  # Posuny pre jednotlivé dataset-y
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = np.loadtxt(file_path)
    data = filter_data(data)
    data = cut_data(data)
    x, y = data[:, 0], data[:, 1] + offset
    data_list.append((x, y))

# Vytvorenie grafu
fig, ax = plt.subplots(figsize=(10, 6))

# Vykreslenie čiar
labels = ["1", "2", "3", "4", "5"]
for (x, y), label in zip(data_list, labels):
    ax.plot(x, y, linestyle='-', linewidth=2, label=label)

# Nastavenie popisov
ax.set_xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize=20)
ax.set_ylabel("Relatívna intenzita", fontsize=20)
# ax.legend(fontsize=20, loc='upper left')

# Nastavenie hlavných a vedľajších čiark na os x
ax.xaxis.set_major_locator(MultipleLocator(200))  # Hlavné čiarky každých 200 jednotiek
ax.xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Prispôsobenie vzhľadu čiark
ax.tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
ax.tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky
ax.tick_params(axis='y', labelleft=False, length=0)  # Odstránenie čísel a čiark na osi y

plt.legend(fontsize=18)
plt.tight_layout()
plt.show()