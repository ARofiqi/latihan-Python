import cv2
import random

path = "./image-processing/Lenna.png"
img = cv2.imread(path)

img1 = cv2.cvtColor(img[0:128], 4)
img2 = cv2.cvtColor(img[128:256], 33)
img3 = cv2.cvtColor(img[256:384], 59)
img4 = cv2.cvtColor(img[384:512], 45)

path_1 = "./image-processing/img/1.png"
path_2 = "./image-processing/img/2.png"
path_3 = "./image-processing/img/3.png"
path_4 = "./image-processing/img/4.png"

cv2.imwrite(path_1, img1)
cv2.imwrite(path_2, img2)
cv2.imwrite(path_3, img3)
cv2.imwrite(path_4, img4)

i1 = cv2.imread(path_1)
i2 = cv2.imread(path_2)
i3 = cv2.imread(path_3)
i4 = cv2.imread(path_4)

imgFull = cv2.vconcat([i1,i2,i3,i4])
path_full = "./image-processing/Hasil.png"
cv2.imwrite(path_full, imgFull)

cv2.imshow("Gambar Lenna sebelum diubah", img)
cv2.waitKey(0)
cv2.imshow("Gambar Lenna setelah diubah", imgFull)
cv2.waitKey(0)
cv2.destroyAllWindows()