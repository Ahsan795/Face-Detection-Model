import cv2

file_path = input("Enter the file path: ")

image = cv2.imread(file_path)

if image is None:
    print("Error: Image not found or invalid file path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
option = int(input("Enter 1 to show the image, or 2 to save the grayscale image: "))

if option == 1:
    # Show the image
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif option == 2:
    # Save the grayscale image
    name = input("Enter the name of the output file (with .jpg or .png extension): ")
    cv2.imwrite(name, gray)
    print(f"Image saved as {name}")

else:
    print("Invalid option selected.")
