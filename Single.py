from brokenaxes import brokenaxes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def filter_data(data, threshold=150):
    return data[data[:, 0] >= threshold]

def remove_x_range(data, low=1850, high=2800):
    """Odstráni dáta v intervale x od 'low' po 'high'."""
    return data[(data[:, 0] < low) | (data[:, 0] > high)]

# Načítanie dát pre prvú čiaru
file_path = "pvTz_Mol1"
data = np.loadtxt(file_path)
data = filter_data(data)
data = remove_x_range(data)

x, y = data[:, 0], data[:, 1]

# Vytvorenie grafu s prerušením osi pomocou brokenaxes
fig = plt.figure(figsize=(10, 6))
bax = brokenaxes(xlims=((150, 1850), (2800, 3500)), hspace=0.05)  # Nastavenie prerušenia osi x

# Vykreslenie prvej čiary
bax.plot(x, y, linestyle='-', linewidth=2, color="darkblue", label="Konformér 1")

# Nastavenie popisov
bax.set_xlabel(r'Vlnočet ($\text{cm}^{-1}$)', fontsize=20, labelpad=40)
bax.set_ylabel("Absorbancia", fontsize=20, labelpad = 5)
bax.legend(fontsize=20, loc='upper right')

# Nastavenie hlavných a vedľajších čiark na os x pre ľavú časť grafu (bax.axs[0])
bax.axs[0].xaxis.set_major_locator(MultipleLocator(200))  # Hlavné čiarky každých 200 jednotiek
bax.axs[0].xaxis.set_minor_locator(MultipleLocator(50))   # Vedľajšie čiarky každých 50 jednotiek

# Nastavenie hlavných a vedľajších čiark na os x pre pravú časť grafu (bax.axs[1])
bax.axs[1].xaxis.set_major_locator(MultipleLocator(200))  # Hlavné čiarky každých 200 jednotiek
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