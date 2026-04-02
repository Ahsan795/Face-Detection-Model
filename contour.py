import cv2

image = cv2.imread("AI\ML\images.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, -1, (0,255,0), 3)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
       shape_name = "triangle"

    elif corners == 4:
       shape_name = "Rectangle"

    elif corners == 5:
       shape_name = "Pentagon"

    elif corners > 5:
       shape_name = "circle"

    else:
       shape_name = "unknown"

    cv2.drawContours(image, [approx], 0, (0,255,0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] -10
    cv2.putText(image, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 3)

cv2.imshow("contour", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
