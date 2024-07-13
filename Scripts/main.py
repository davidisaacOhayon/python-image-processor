import cv2 
import random


img = cv2.imread('Images/car.jpg', 1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


# Manipulate the colors of each pixel within a segment of the image.
# for j in range(0,255):
#     for x in range(500):
#         img[j][x] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]


someTag = img[500:600, 800:900]

img[100:200, 600:]


cv2.imshow('Image', img);
cv2.waitKey(0)
cv2.destroyAllWindows();