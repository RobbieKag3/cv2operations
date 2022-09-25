import cv2 
image1=cv2.imread("star-1-300x168.jpg")
image2=cv2.imread("dot-300x168.jpg")
newimage=cv2.subtract(image1,image2)
cv2.imwrite("subtractedimage.jpg", newimage)
cv2.destroyAllWindows()