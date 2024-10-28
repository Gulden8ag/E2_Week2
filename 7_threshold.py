import cv2, time
import numpy as np

image = cv2.imread("Elementos_2Week2/images/numbers.png")

thresh = 100
maxValue = 255

'''
cv2.threshold has the following syntax :

retval, dst = cv.threshold(src, thresh, maxval, type[, dst])

Where,

Input:

src is the input array ot image (multiple-channel, 8-bit or 32-bit floating point).
thresh is the threshold value.
maxval is the maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
type is thethresholding type ( THRESH_BINARY, THRESH_BINARY_INV, etc )

Output:

dst is the output array or image of the same size and type and the same number of channels as src.
retval is the threshold value if you use other thresholding types such as Otsu or Triangle


'''
# el thresh es el valor de corte
retval, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY)
#retval, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY_INV)
#retval, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TRUNC)
#retval, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO)
#retval, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO_INV)

'''
cv2.THRESH_BINARY (Umbral Binario)
Si el valor de un píxel es mayor que el valor de umbral (thresh), se asigna el valor máximo (maxValue) al píxel. Si no, se asigna un valor de 0.
Ejemplo: Si thresh = 127 y maxValue = 255, los píxeles mayores a 127 serán 255, y los menores o iguales serán 0.

cv2.THRESH_BINARY_INV (Umbral Binario Invertido)
Es similar al umbral binario, pero los valores están invertidos. Si el valor de un píxel es mayor que el umbral, se asigna 0; si es menor o igual, se asigna el valor máximo.

cv2.THRESH_TRUNC (Umbral Truncado)
Si el valor del píxel es mayor que el umbral, se trunca al valor del umbral, pero si es menor o igual, el valor del píxel se mantiene sin cambios.
Ejemplo: Si thresh = 127, cualquier valor de píxel mayor a 127 será convertido a 127.

cv2.THRESH_TOZERO (Umbral a Cero)
Si el valor del píxel es mayor que el umbral, el valor del píxel se mantiene. Si es menor o igual, el valor se convierte en 0.

cv2.THRESH_TOZERO_INV (Umbral a Cero Invertido)
Es lo opuesto a cv2.THRESH_TOZERO. Si el valor del píxel es mayor que el umbral, se convierte en 0, y si es menor o igual, se mantiene.

'''

cv2.imshow("Original", image)
cv2.imshow("Threshold", dst)


while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break

cv2.destroyAllWindows()