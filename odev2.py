import cv2
import numpy as np

def main():
    # Kamera başlatma
    cap = cv2.VideoCapture(0)

    while True:
        # Bir kare alma
        ret, frame = cap.read()

        # Kareyi BGR renk uzayından HSV renk uzayına dönüştürme
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Kırmızı renk aralığı
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        lower_red2 = np.array([170, 50, 50])
        upper_red2 = np.array([180, 255, 255])

        # Renk aralığına göre maskeleme
        mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
        mask_red2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
        mask_red_combined = cv2.bitwise_or(mask_red, mask_red2)

        # Orijinal görüntüyü filtrelenmiş görüntüyle birleştirme
        filtered_frame = cv2.bitwise_and(frame, frame, mask=mask_red_combined)

        # Görüntüleri gösterme
        cv2.imshow('Original', frame)
        cv2.imshow('Filtered', filtered_frame)

        # 'w' basınca kameradan/programdan çık
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break

    # Kamerayı kapat
    cap.release()

    # Pencereleri kapat
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()