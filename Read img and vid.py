import cv2

# Read the image
image = cv2.imread("Open CV photos and Videos/Ducks.jpg")

# Display the image
cv2.imshow("Ducks", image)

# Get image properties
height, width, channels = image.shape

print("Height:", height)
print("Width:", width)
print("Number of channels:", channels)

# Save the image with a different filename
cv2.imwrite("Open CV photos and Videos/Ducks_new.jpg", image)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()