import cv2
import numpy as np

# Cargar imagen
image = cv2.imread('Elementos_2Week2/images/Contour.png')
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''
findContours: se utiliza para detectar los contornos en una imagen binaria. Esta función devuelve una lista de contornos encontrados y una jerarquía opcional de contornos.

contours, hierarchy = cv.findContours(image, mode, method[, contours[, hierarchy[, offset]]])

Parámetros:

- image: Es la imagen de entrada, que debe estar en formato binario.
- mode: Modo de recuperación de contornos, puede ser:
  - `cv.RETR_EXTERNAL`: recupera solo los contornos externos.
  - `cv.RETR_LIST`: recupera todos los contornos sin organizar en jerarquía.
  - `cv.RETR_CCOMP`: organiza los contornos en dos niveles, el nivel externo y los huecos en él.
  - `cv.RETR_TREE`: recupera todos los contornos y crea una jerarquía completa de contornos anidados.
- method: Método de aproximación de contornos, que puede ser:
  - `cv.CHAIN_APPROX_NONE`: almacena todos los puntos del contorno.
  - `cv.CHAIN_APPROX_SIMPLE`: comprime segmentos horizontales, verticales y diagonales dejando solo los puntos finales.
- contours: Lista de contornos encontrados en la imagen. Cada contorno es un arreglo de puntos.
- hierarchy: Es una matriz opcional que contiene información de la relación jerárquica entre contornos.
- offset: Es opcional, y permite establecer un desplazamiento para los puntos en los contornos encontrados.

'''
contours, hierarchy = cv2.findContours(image_gs, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("OG", image)
#                donde, lista, cuales, color, grosor
cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
cv2.imshow("Contour", image)

''' CENTRO DE MASA '''

for cnt in contours:
    M = cv2.moments(cnt)
    #Formulas de centro a partir de momentos
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))
    # Marca el centro
    cv2.circle(image, (x,y), 3, (0,255,0), -1)

''' ENUMERAR CONTORNOS '''
for index,cnt in enumerate(contours):
    M = cv2.moments(cnt)
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))
    cv2.circle(image, (x,y), 10, (0,255,0), -1)
    # Marcar Texto
    cv2.putText(image, "{}".format(index + 1), (x-10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
'''BOUNDING BOX'''

for index,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    print("Contour #{} has area = {} and perimeter = {}".format(index+1,area,perimeter))

box1 = image.copy()
for cnt in contours:
    # pos x, pos y, ancho, alto
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(box1, (x,y), (x+w,y+h), (255,0,255), 2)

box2 = image.copy()
for cnt in contours:
    # Bounding box rotado
    box = cv2.minAreaRect(cnt)
    #sacar los puntos del rectangulo
    boxPts = np.int32(cv2.boxPoints(box))
    cv2.drawContours(box2, [boxPts], -1, (0,255,255), 2)
cv2.imshow("Contour_Centro", image)
cv2.imshow("Contour_Box", box1)
cv2.imshow("Contour_RotatedBox", box2)
cv2.waitKey(0)
cv2.destroyAllWindows()