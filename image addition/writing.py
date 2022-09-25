import cv2 
image=cv2.imread("star-1-300x168.jpg")
font=cv2.FONT_HERSHEY_COMPLEX
org=(50,50)
fontscale=1
color=(255,0,0)
thickness=2
newimage=cv2.putText(image,"Robbie",org,font,fontscale,color,thickness,cv2.LINE_AA)
cv2.imwrite("lineimage.jpg",newimage)
cv2.destroyAllWindows()