import cv2

# Read the image
image = cv2.imread("Open CV photos and Videos/Ducks_new.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Apply Canny edge detection to grayscale image
edges = cv2.Canny(gray, 100, 200)

# Display all images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("Edges", edges)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()