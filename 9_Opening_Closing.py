import cv2
import numpy as np
'''OPENING'''
# Cargar imagen
image = cv2.imread('Elementos_2Week2\images\opening.png')

# Crear kernel
kSize = 3
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*kSize+1, 2*kSize+1), (kSize, kSize))
'''OPEN Metodo 1'''
# Perform Erosion
imEroded = cv2.erode(image, kernel, iterations=3)
# Perform Dilation
imOpen = cv2.dilate(imEroded, kernel, iterations=3)

'''OPEN Metodo 2'''
imageMorphOpened = cv2.morphologyEx(image, cv2.MORPH_OPEN, 
                        kernel,iterations=3)
# Mostrar Imagenes
cv2.imshow("OG", image)
cv2.imshow("Eroded", imEroded)
cv2.imshow("Opened", imOpen)
cv2.imshow("Opened2", imageMorphOpened)

'''CLOSING'''
# Cargar imagen
image2 = cv2.imread('Elementos_2Week2\images\closing.png')

'''CLOSE Metodo 1'''
# Perform Dilation
imDilated = cv2.dilate(image2, kernel,iterations=4)
# Perform Erosion
imClose = cv2.erode(imDilated, kernel,iterations=4)
'''CLOSE Metodo 2'''
imageMorphClosed = cv2.morphologyEx(image2,
                                    cv2.MORPH_CLOSE, kernel,iterations=4)

# Mostrar Imagenes
cv2.imshow("OG2", image2)
cv2.imshow("Dilated", imDilated)
cv2.imshow("Closed", imClose)
cv2.imshow("Closed2", imageMorphClosed)
cv2.waitKey(0)
cv2.destroyAllWindows()