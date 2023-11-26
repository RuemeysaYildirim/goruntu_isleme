import cv2

image = cv2.imread("9pirinc.jpg")

# Görüntüyü griye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşik değerini belirledim
threshold_value = 130


# Eşikleme işlemi
_, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Kontürleri bul
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısı
print("Pirinç sayısı:", len(contours))

# Eşiklenmiş görüntüyü göster
cv2.imshow("Eşiklenmiş Görüntü", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()