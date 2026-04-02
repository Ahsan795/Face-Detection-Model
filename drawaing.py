import cv2

image = cv2.imread("AI\ML\minhas.png")

file_path = input("enter the image location: ")

if image is None:
    print("oops! image is not found")
    exit()

#pt1= (90,100)
#pt2 = (850,100)
#color = (255,0,0)
#thickness = 5
try:
    print("Enter the following values to draw a line on the image:")
    x1 = int(input("  x1: "))
    y1 = int(input("  y1: "))
    x2 = int(input("  x2: "))
    y2 = int(input("  y2: "))
    r = int(input("  Red (0-255): "))
    g = int(input("  Green (0-255): "))
    b = int(input("  Blue (0-255): "))
    thickness = int(input("  Thickness (e.g., 2, 5): "))
except ValueError:
    print("Invalid input. Please enter only integers.")
    exit()

pt1 = (x1, y1)
pt2 = (x2, y2)
color = (b, g, r)  # OpenCV uses BGR format
cv2.line(image, pt1, pt2, color, thickness)

#cv2.putText(image, "opencv is good for learning", (100,90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.0, (255,0,0), 4)
option = int(input("enter 1 to save the image, or enter 2 for not saving the image :"))
#option2 = int(input("enter 1 to show  the image, or enter 2 to save image:"))

if option == 1:
    cv2.imshow("image focusing text", image)
    cv2.imwrite("output.png", image)
    #cv2.imshow("line image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif option == 2:
    name = input("enter the name of the output file (with .png or .jpg extension):")
    cv2.imwrite(name, image)
    print(f"image saved as {name}")

else:
    print("inavlid option selected...")
