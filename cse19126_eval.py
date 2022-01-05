import cv2
import sys

#get image paths
path1 = sys.argv[1]
path2 = sys.argv[2]

#get images using imread 
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

#checking is images are valid
if img1 is None:
	print("Image 1 is not valid")
if img2 is None:
	print("Image 2 is not valid")


diff_image = cv2.absdiff(img1, img2)


cv2.imwrite('diff_result.jpg', diff_image)