import cv2

# Read the image
image = cv2.imread("Open CV photos and Videos/Ducks.jpg")


# 1. Resize the image
resized = cv2.resize(image, (500, 400))


# 2. Crop a specific region
cropped = image[100:400, 100:500]


# 3. Flip the image horizontally
flipped = cv2.flip(image, 1)


# 4. Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Cropped Image", cropped)
cv2.imshow("Flipped Image", flipped)


# 5. Save the results
cv2.imwrite("Open CV photos and Videos/Ducks_resized.jpg", resized)
cv2.imwrite("Open CV photos and Videos/Ducks_cropped.jpg", cropped)
cv2.imwrite("Open CV photos and Videos/Ducks_flipped.jpg", flipped)


# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()
