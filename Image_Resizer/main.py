import cv2

# Load the image
src = cv2.imread("/Users/ayushmangupta/PycharmProjects/Image_Resizer/sunflower.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("image", src)

# Percentage by which the image is resized
scale_percent = 50

# Calculating 50% of original dimension
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# Reduced size
dim = (width, height)

# Final output
output = cv2.resize(src, dim)

cv2.imwrite('/Users/ayushmangupta/Downloads/resized_sunflower.jpg', output )
cv2.waitKey(0)