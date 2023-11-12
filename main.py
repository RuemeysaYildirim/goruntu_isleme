import cv2
import matplotlib.pyplot as plt
import numpy as np
#Fotoğraf açılıp okunuyor
foto=cv2.imread("bulut.webp")
cv2.imshow("bulut.webp",foto)

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]


from matplotlib import pyplot as plt
#Fotoğrafı grileştiriyoruz
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()


#Fotoğrafın histogramını hesaplıyoruz
histog = np.zeros(256)
for i in range(foto.shape[0]):
    for j in range(foto.shape[1]):
        pixel_deg= foto[i, j]
        histog[pixel_deg] += 1

plt.bar(range(256), histog)
plt.show()