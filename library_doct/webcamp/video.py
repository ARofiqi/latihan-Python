import cv2

cap = cv2.VideoCapture(0)
i = 0

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('w'):
        cv2.imwrite(f"aro{i}.png", frame)
        print("Mengambil gambar")
        i+=1
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()