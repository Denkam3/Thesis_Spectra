from brokenaxes import brokenaxes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

# Načítanie dát pre jednotlivé čiary
file_paths = ["Jungle Juice_MIR.csv", "Amsterdam_MIR.csv", "Rave_MIR.csv"]
offsets = [-300, -450, -600]  # Posuny pre jednotlivé dataset-y
file_paths_cal = ["pvTz_Mol1", "pvTz_Mol2", "pvTz_Mol3", "pvTz_Mol4", "pvTz_Mol5"]
offsets_cal = [-100, 50, 200, 350, 500]  # Posuny pre jednotlivé dataset-y
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = pd.read_csv(file_path, sep = ";", header = None )
    x, y = data.iloc[:, 0], data.iloc[:, 1] * 1000 + offset
    data_list.append((x, y))

for file_path, offset in zip(file_paths_cal, offsets_cal):
    data = np.loadtxt(file_path)
    x, y = data[:, 0], data[:, 1] + offset
    data_list.append((x,y))

# Vytvorenie grafu s prerušením osi pomocou brokenaxes
fig = plt.figure(figsize=(6, 9))
bax = brokenaxes(xlims=((400, 1800), (2800, 3300)), hspace=0.05)  # Nastavenie prerušenia osi x

# Vykreslenie čiar
labels = ["Jungle Juice", "Amsterdam", "Rave", "1", "2", "3", "4", "5"]
for (x, y), label in zip(data_list, labels):
    bax.plot(x, y, linestyle='-', linewidth=2, label= label)

# Nastavenie popisov
bax.set_xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize=20, labelpad = 40)
bax.set_ylabel("Relatívna absorbancia", fontsize=20, labelpad = 5)
bax.legend(fontsize=15, loc='upper right', bbox_to_anchor = (0.85, 0.9))

# Nastavenie hlavných a vedľajších čiark na os x pre ľavú časť grafu (bax.axs[0])
bax.axs[0].xaxis.set_major_locator(MultipleLocator(150))  # Hlavné čiarky každých 200 jednotiek
bax.axs[0].xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Nastavenie hlavných a vedľajších čiark na os x pre pravú časť grafu (bax.axs[1])
bax.axs[1].xaxis.set_major_locator(MultipleLocator(150))  # Hlavné čiarky každých 200 jednotiek
bax.axs[1].xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Prispôsobenie vzhľadu čiark a odstránenie čísel a čiark na osi y
bax.axs[0].tick_params(axis='y', labelleft=False, length=0)  # Odstránenie čísel a čiark na osi y pre ľavú časť grafu
bax.axs[1].tick_params(axis='y', labelleft=False, length=0)  # Odstránenie čísel a čiark na osi y pre pravú časť grafu

# Prispôsobenie vzhľadu čiark na osi x
bax.axs[0].tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
bax.axs[0].tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky

bax.axs[1].tick_params(axis='x', which='major', length=10, width=1.5, labelsize=20)  # Hlavné čiarky
bax.axs[1].tick_params(axis='x', which='minor', length=5, width=1, labelsize=12)     # Vedľajšie čiarky

plt.tight_layout()
plt.show()