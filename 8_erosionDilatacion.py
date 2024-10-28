import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
Dilation: es usado unir para expandir las areas blancas de la imagen, la cual debe ser binaria.
dst =   cv.dilate(  src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )

Erosion: es usao para separar o reducir las areas blancas de la imagen, la cual debe ser binaria.
dst =   cv.erode(   src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )

src: es la imagen de entrada
kernel: es el kernel que se usara para la dilatacion (una imagen de 3x3 o 5x5 pixeles normalmente)
dst : es la imagen de salida
anchor: es el punto central del kernel, por defecto es (-1,-1) que significa que esta en el centro del kernel
iterations: numero de veces que se dilatara la imagen
borderType: tipo de borde que se usara
borderValue: valor de borde que se usara

'''
# Cargar imagen
image = cv2.imread('Elementos_2Week2\images\dilation_example.jpg')

# Crear kernel
kSize = (3,3)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kSize)
plt.imshow(kernel1)

''' DILATACION '''
# Dilatar la imagen
imageDilated = cv2.dilate(image, kernel1)
#imageDilated = cv2.dilate(image, kernel1,iterations=2)

# Mostrar Imagenes
cv2.imshow("OG1", image)
cv2.imshow("Dilated", imageDilated)


''' EROSION '''
image = cv2.imread('Elementos_2Week2\images\erosion_example.jpg')

# Erosionar la imagen
imageEroded = cv2.erode(image, kernel1)
#imageEroded = cv2.erode(image, kernel1,iterations=2)
# Mostrar Imagenes
cv2.imshow("OG2", image)
cv2.imshow("Eroded", imageEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

