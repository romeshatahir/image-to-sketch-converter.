import cv2

#Read the image
image = cv2.imread("c:/users/mypc/desktop/romesha.jpg")

#Convert to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Invert the grayscale image
invert = cv2.bitwise_not(gray_img)

#Apply Gaussian blur
blur = cv2.GaussianBlur(invert, (21, 21), 0)

#Invert the blurred image
inverted_blur = cv2.bitwise_not(blur)

#Create the pencil sketch
sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

#Show the sketch
cv2.imshow ( "sketch",sketch)
cv2.waitKey(100000)
cv2.destroyAllwindows