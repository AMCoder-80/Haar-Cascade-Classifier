import cv2

cascade_path = './cascade.xml' 
cascade = cv2.CascadeClassifier(cascade_path)

image_path = './ducks.jpg'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 4)

cv2.imshow('Object Detection', image)

cv2.waitKey(0)
cv2.destroyAllWindows()