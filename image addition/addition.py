import cv2
image1=cv2.imread("1-500x250-3.jpg")
image2=cv2.imread("2-500x250-2.jpg")
newimage=cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imwrite("added.jpg", newimage)
cv2.destroyAllWindows()
