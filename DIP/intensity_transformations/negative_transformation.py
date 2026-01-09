import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths
image_path = r'c:\Users\pathi\OneDrive\Desktop\DIP\profile pic.jpg'
output_dir = r'c:\Users\pathi\OneDrive\Desktop\DIP\intensity_transformations'
output_file = os.path.join(output_dir, 'negative_transformation_output.png')

# Load image
img = cv2.imread(image_path, 0)
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Negative Transformation: s = L - 1 - r
# For 8-bit image, L-1 = 255
negative_img = 255 - img

# Histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_negative = cv2.calcHist([negative_img], [0], None, [256], [0, 256])

# Visualization
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Negative Image")
plt.imshow(negative_img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Original Histogram")
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.title("Negative Histogram")
plt.plot(hist_negative, color='orange')
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig(output_file)
print(f"Negative transformation result saved to {output_file}")
# plt.show()
