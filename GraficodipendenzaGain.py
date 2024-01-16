from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import os

# Definisci la cartella delle immagini FITS
cartella_immagini = '/SunhalphaStageOATO/Ottimizzazione_parametri_camera/SET2/AS_P50'

# Otteniamo la lista di file FITS nella cartella
elenco_immagini = [f for f in os.listdir(cartella_immagini) if f.endswith('.fit')]

# Inizializza le liste per i valori di gain e intensità del pixel centrale
gain_values = []
intensity_values = []

# Ciclo attraverso ciascuna immagine FITS nella cartella
for immagine_nome in elenco_immagini:
    immagine_path = os.path.join(cartella_immagini, immagine_nome)
    
    # Apri l'immagine FITS
    hdul = fits.open(immagine_path)
    
    # Estrai il dato dell'immagine
    immagine_data = hdul[0].data
    
    # Estrai le dimensioni dell'immagine
    height, width, x = immagine_data.shape
    
    # Calcola il pixel centrale
    center_pixel_value = immagine_data[height // 2, width // 2, x // 2]
    
    # Aggiungi il valore del gain e l'intensità del pixel centrale alle liste
    header = hdul[0].header
    gain_values = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]  # Sostituisci 'GAIN' con il nome dell'header FITS che contiene il gain
    intensity_values.append(center_pixel_value)
    
    # Chiudi il file FITS
    hdul.close()
    
    SNR2= ((np.exp(9733.2295))*9733.2295)/991.073
print(SNR2)
print(intensity_values)
# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(gain_values, intensity_values, 'b', label='Intensità del pixel centrale')
plt.xlabel('Gain')
plt.ylabel('Intensità del pixel centrale')
plt.title('Relazione tra Gain e Intensità del pixel centrale')
plt.yscale('log')
plt.grid(True)

plt.legend()

# Mostra il grafico
plt.show()
