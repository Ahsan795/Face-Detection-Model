import cv2

image = cv2.imread("AI\ML\minhas.png")

if image is None:
    print("image is not load") 
else:
    flipped_vertically = cv2.flip(image, 0)
    flipped_horizontally = cv2.flip(image, 1)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("orignal image", image)
    cv2.imshow("vertically imgage", flipped_vertically)
    cv2.imshow("horizontally",flipped_horizontally)
    cv2.imshow("both", flipped_both)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
