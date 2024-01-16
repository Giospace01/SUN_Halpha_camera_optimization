from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import os

# Define fits folder
cartella_immagini = '/SunhalphaStageOATO/Ottimizzazione_parametri_camera/SET1/AS_P50'

# Optain fits file from folder
elenco_immagini = [f for f in os.listdir(cartella_immagini) if f.endswith('.fit')]

# Inizialize the list of gain and intensity for the central pixel
intensity_values = []


for immagine_nome in elenco_immagini:
    immagine_path = os.path.join(cartella_immagini, immagine_nome)
    
    # Open Fits
    hdul = fits.open(immagine_path)
    
    # Extract data
    immagine_data = hdul[0].data
    
    # Extract dimension
    height, width, x = immagine_data.shape
    
    # estimeta the central pixel
    center_pixel_value = immagine_data[height // 2, width // 2, x // 2]
    
    
    header = hdul[0].header
    exp_values = [0.1, 0.2, 0.3, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]  # Sostituisci 'GAIN' con il nome dell'header FITS che contiene il gain
    intensity_values.append(center_pixel_value)
    
    
    hdul.close()


plt.figure(figsize=(8, 6))
plt.plot(exp_values, intensity_values, 'b', label='Intensità del pixel centrale')
plt.xlabel('Exp')
plt.ylabel('Intensità del pixel centrale')
plt.title('Relazione tra Exp e Intensità del pixel centrale')
plt.grid(True)
plt.legend()

plt.show()
