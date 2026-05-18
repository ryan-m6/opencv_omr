import cv2
print(cv2.__version__)


# Path to image
path= "images/sample1.jpg"

# Read image
img = cv2.imread(path)

# Check if image loaded
if img is None:
    print("Failed to load image")
    exit()

# Print debugging information
print("Image loaded successfully")
print("Shape:", img.shape)
print("Data type:", img.dtype)

# Display image
cv2.imshow("Sample Image", img)

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()