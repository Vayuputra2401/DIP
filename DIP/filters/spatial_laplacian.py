import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\filters'
output_file = os.path.join(output_dir, 'output_spatial_laplacian.png')

# Load image
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Convert to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Laplacian Filter
# Convert to gray first for edge detection often, but can do on color channels too. 
# We'll apply to gray for clearer edge visualization, or each channel.
# Let's apply to grayscale version for standard edge detection demo.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ddepth = cv2.CV_16S to avoid overflow (negative values), then convert back
laplacian = cv2.Laplacian(gray_img, cv2.CV_16S, ksize=3)
abs_laplacian = cv2.convertScaleAbs(laplacian)

# Save result
cv2.imwrite(output_file, abs_laplacian)
print(f"Laplacian filter result saved to {output_file}")

# Display
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Laplacian Edge Detection")
plt.imshow(abs_laplacian, cmap='gray')
plt.axis('off')

plt.show()
