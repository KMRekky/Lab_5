from PIL import Image
# Otwieranie obrzu
img = Image.open('test.jpg')
img.show()

# Zmiana rozmiaru i zapis
resized = img.resize((2000, 1000))
resized.save('test.jpg')

from PIL import Image, ImageFilter
img = Image.open("test.jpg")

# Rozmycie
blurred = img.filter(ImageFilter.GaussianBlur(5))
blurred.save("test_blurred.jpg")

# Nadanie skali szarości
gray = img.convert("L")
gray.save("test_gray.jpg")

import cv2
# Detekcja krawędzi
img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)
cv2.imwrite("test_edges.jpg", edges)

import cv2
img = cv2.imread("test.jpg")
(h, w) = img.shape[:2]

# Środek obrazu
center = (w // 2, h // 2)

# Obrót o 45 stopni
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imwrite("test_rotated.jpg", rotated)
