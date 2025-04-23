from brokenaxes import brokenaxes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

# Načítanie dát pre jednotlivé čiary
file_paths = ["jj_5_256_100.csv", "ams_5_256_100.csv", "rave_5_256_100.csv"]
offsets = [0, 0, 0]  # Posuny pre jednotlivé dataset-y
data_list = []

for file_path, offset in zip(file_paths, offsets):
    data = pd.read_csv(file_path, sep = ";", header = None )
    x, y = data.iloc[:, 0], data.iloc[:, 1] + offset
    data_list.append((x, y))

# Vytvorenie grafu s prerušením osi pomocou brokenaxes
fig = plt.figure(figsize=(10, 6))
bax = brokenaxes(xlims=((200, 1800), (2550, 3200)), hspace=0.05)  # Nastavenie prerušenia osi x

# Vykreslenie čiar
labels = ["Jungle Juice", "Amsterdam", "Rave"]
for (x, y), label in zip(data_list, labels):
    bax.plot(x, y, linestyle='-', linewidth=2, label= label)

# Nastavenie popisov
bax.set_xlabel(r'Ramanov posun ($\text{cm}^{-1}$)', fontsize=20, labelpad=40)
bax.set_ylabel("Relatívna Intenzita", fontsize=20, labelpad = 5)
bax.legend(fontsize=20, loc='upper right', bbox_to_anchor=(0.85, 1))

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