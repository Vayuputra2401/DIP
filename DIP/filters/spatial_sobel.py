import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\filters'
output_file = os.path.join(output_dir, 'output_spatial_sobel.png')

# Load image
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Convert to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel Filter
# Sobel X
sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
abs_sobelx = cv2.convertScaleAbs(sobelx)

# Sobel Y
sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
abs_sobely = cv2.convertScaleAbs(sobely)

# Combined
sobel_combined = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)

# Save result
cv2.imwrite(output_file, sobel_combined)
print(f"Sobel filter result saved to {output_file}")

# Display
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("Sobel X")
plt.imshow(abs_sobelx, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title("Sobel Y")
plt.imshow(abs_sobely, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title("Sobel Combined")
plt.imshow(sobel_combined, cmap='gray')
plt.axis('off')

plt.show()
