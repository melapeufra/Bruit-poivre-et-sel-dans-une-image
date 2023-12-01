import numpy as np
from imageio.v2 import imread
from scipy import stats
import matplotlib.pyplot as plt
from  PIL  import  Image
from  PIL  import  ImageFilter 

# Charger l'image
Z = np.array(imread("cameraman-bruite.jpg"))

# Convertir l'image en une séquence de 0 et 255 (noir et blanc)
binary_image = (Z == 255).astype(int)

# Estimer la probabilité p (niveau de bruit) par la moyenne empirique
p_estimate = np.mean(binary_image)

# Calculer l'intervalle de confiance pour la proportion binomiale
alpha = 0.05  # Niveau de confiance à 95%
n = np.sum(binary_image)  # Nombre total de pixels affectés par le bruit
std_error = np.sqrt(p_estimate * (1 - p_estimate) / n)

conf_interval = stats.norm.interval(1 - alpha, loc=p_estimate, scale=std_error)

# Afficher les résultats
print(f"Estimation du niveau de bruit : {p_estimate:.4f}")
print(f"Intervalle de confiance à {100*(1-alpha)}% : ({conf_interval[0]:.4f}, {conf_interval[1]:.4f})")

# Charger l'image en couleur
image_color = imread("cameraman-bruite.jpg")

# Afficher l'image en couleur
plt.figure(figsize=(8, 8))
plt.imshow(image_color)
plt.title("Image en couleur")
plt.show()


img1=Image.open("cameraman-bruite.jpg")
img2=Image.open("cameraman-bruite.jpg")
img1.show()
img2.show()
img2.filter(ImageFilter.MedianFilter(size=1)).show()
img2.filter(ImageFilter.MedianFilter(size=3)).show()
img2.filter(ImageFilter.MedianFilter(size=5)).show()