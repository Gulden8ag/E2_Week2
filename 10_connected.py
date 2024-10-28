import cv2
import numpy as np

# Cargar imagen
image = cv2.imread('Elementos_2Week2/images/truth.png',cv2.IMREAD_GRAYSCALE)

th, imThresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

nlables, imLabels = cv2.connectedComponents(imThresh)

# Mostrar Imagenes
cv2.imshow("OG", image)
cv2.imshow("Threshold", imThresh)
cv2.imshow("Connected", imLabels.astype(np.uint8) * 50)

print("Numero de componentes conectados: ", nlables)# Numero de componentes conectados mas fondo
for label in range(1, nlables):
    component_mask = (imLabels == label).astype(np.uint8) * 50  # Convert mask to 0-255 for visibility
    # Mostrar el componente en una nueva ventana
    cv2.imshow(f"Component {label}", component_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
